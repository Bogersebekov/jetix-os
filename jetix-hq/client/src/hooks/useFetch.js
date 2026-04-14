import { useState, useEffect, useCallback, useRef } from 'react';

const API_BASE = import.meta.env.VITE_API_URL || '';

/**
 * @param {string} path - API path
 * @param {object} opts
 * @param {number} opts.interval - polling interval (fallback), 0 = off
 * @param {boolean} opts.enabled - enable/disable
 * @param {string[]} opts.wsEvents - WS event types that trigger refetch
 * @param {function} opts.onWs - WS context's `on` function (from useWs)
 */
export default function useFetch(path, { interval = 0, enabled = true, wsEvents, onWs } = {}) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);
  const retried = useRef(false);

  const fetchData = useCallback(async () => {
    if (!enabled) return;
    try {
      const res = await fetch(`${API_BASE}${path}`);
      if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
      const json = await res.json();
      setData(json);
      setError(null);
      retried.current = false;
    } catch (err) {
      if (!retried.current) {
        retried.current = true;
        setTimeout(fetchData, 1000);
        return;
      }
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [path, enabled]);

  // Initial fetch
  useEffect(() => {
    setLoading(true);
    fetchData();
  }, [fetchData]);

  // Polling fallback
  useEffect(() => {
    if (!interval || !enabled) return;
    const id = setInterval(fetchData, interval);
    return () => clearInterval(id);
  }, [fetchData, interval, enabled]);

  // WS-triggered refetch
  useEffect(() => {
    if (!wsEvents?.length || !onWs) return;
    const unsubs = wsEvents.map((evt) => onWs(evt, fetchData));
    // Also listen to fallback polling
    const unsubFallback = onWs('fallback:poll', fetchData);
    return () => {
      unsubs.forEach((u) => u());
      unsubFallback();
    };
  }, [wsEvents, onWs, fetchData]);

  return { data, error, loading, refetch: fetchData };
}
