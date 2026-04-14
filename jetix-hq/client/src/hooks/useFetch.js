import { useState, useEffect, useCallback, useRef } from 'react';

const API_BASE = import.meta.env.VITE_API_URL || '';

export default function useFetch(path, { interval = 0, enabled = true } = {}) {
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

  useEffect(() => {
    setLoading(true);
    fetchData();
  }, [fetchData]);

  useEffect(() => {
    if (!interval || !enabled) return;
    const id = setInterval(fetchData, interval);
    return () => clearInterval(id);
  }, [fetchData, interval, enabled]);

  return { data, error, loading, refetch: fetchData };
}
