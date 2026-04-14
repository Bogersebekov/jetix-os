import { useEffect, useRef, useState, useCallback, createContext, useContext } from 'react';

const WS_URL = `ws://${window.location.hostname}:3001/ws`;
const CHANNELS = ['agents', 'kanban', 'resources', 'company', 'comms'];
const MAX_BACKOFF = 30000;

const WsContext = createContext(null);

// Event emitter for WS messages
function createEventBus() {
  const listeners = new Map();
  return {
    on(event, fn) {
      if (!listeners.has(event)) listeners.set(event, new Set());
      listeners.get(event).add(fn);
      return () => listeners.get(event)?.delete(fn);
    },
    emit(event, data) {
      listeners.get(event)?.forEach((fn) => fn(data));
      listeners.get('*')?.forEach((fn) => fn({ event, data }));
    },
  };
}

export function WsProvider({ children }) {
  const [connected, setConnected] = useState(false);
  const wsRef = useRef(null);
  const busRef = useRef(createEventBus());
  const backoffRef = useRef(1000);
  const reconnectTimer = useRef(null);
  const fallbackTimer = useRef(null);
  const mountedRef = useRef(true);

  const connect = useCallback(() => {
    if (wsRef.current?.readyState === WebSocket.OPEN) return;

    try {
      const ws = new WebSocket(WS_URL);
      wsRef.current = ws;

      ws.onopen = () => {
        if (!mountedRef.current) return;
        console.log('[ws] connected');
        setConnected(true);
        backoffRef.current = 1000;
        // Stop fallback polling
        if (fallbackTimer.current) {
          clearInterval(fallbackTimer.current);
          fallbackTimer.current = null;
        }
        // Subscribe to all channels
        ws.send(JSON.stringify({ type: 'subscribe', channels: CHANNELS }));
      };

      ws.onmessage = (e) => {
        try {
          const msg = JSON.parse(e.data);
          busRef.current.emit(msg.type, msg);
        } catch { /* ignore malformed */ }
      };

      ws.onclose = () => {
        if (!mountedRef.current) return;
        console.log('[ws] disconnected');
        setConnected(false);
        scheduleReconnect();
        startFallbackPolling();
      };

      ws.onerror = () => {
        ws.close();
      };
    } catch {
      scheduleReconnect();
    }
  }, []);

  function scheduleReconnect() {
    if (reconnectTimer.current) return;
    const delay = backoffRef.current;
    console.log(`[ws] reconnecting in ${delay}ms`);
    reconnectTimer.current = setTimeout(() => {
      reconnectTimer.current = null;
      backoffRef.current = Math.min(backoffRef.current * 2, MAX_BACKOFF);
      connect();
    }, delay);
  }

  function startFallbackPolling() {
    if (fallbackTimer.current) return;
    console.log('[ws] starting fallback polling (30s)');
    fallbackTimer.current = setInterval(() => {
      busRef.current.emit('fallback:poll', { ts: Date.now() });
    }, 30000);
  }

  const send = useCallback((msg) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(msg));
    }
  }, []);

  useEffect(() => {
    mountedRef.current = true;
    connect();
    return () => {
      mountedRef.current = false;
      if (reconnectTimer.current) clearTimeout(reconnectTimer.current);
      if (fallbackTimer.current) clearInterval(fallbackTimer.current);
      wsRef.current?.close();
    };
  }, [connect]);

  const value = { connected, send, on: busRef.current.on, emit: busRef.current.emit };

  return <WsContext.Provider value={value}>{children}</WsContext.Provider>;
}

export function useWs() {
  const ctx = useContext(WsContext);
  if (!ctx) throw new Error('useWs must be used within WsProvider');
  return ctx;
}

// Subscribe to specific WS events and trigger callback
export function useWsEvent(eventType, callback) {
  const { on } = useWs();
  useEffect(() => {
    return on(eventType, callback);
  }, [on, eventType, callback]);
}
