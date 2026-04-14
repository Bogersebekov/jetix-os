import { Routes, Route, Navigate } from 'react-router-dom';
import { ToastProvider } from './components/ui/Toast';
import { WsProvider } from './hooks/useWebSocket';
import ErrorBoundary from './components/ErrorBoundary';
import Layout from './components/Layout';
import HQ from './pages/HQ';
import Agents from './pages/Agents';
import Dashboard from './pages/Dashboard';
import Kanban from './pages/Kanban';
import Knowledge from './pages/Knowledge';
import Settings from './pages/Settings';
import NotFound from './pages/NotFound';

export default function App() {
  return (
    <WsProvider>
      <ToastProvider>
        <Layout>
          <ErrorBoundary>
            <Routes>
              <Route path="/" element={<Navigate to="/hq" replace />} />
              <Route path="/hq" element={<HQ />} />
              <Route path="/agents" element={<Agents />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/kanban" element={<Kanban />} />
              <Route path="/knowledge" element={<Knowledge />} />
              <Route path="/settings" element={<Settings />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </ErrorBoundary>
        </Layout>
      </ToastProvider>
    </WsProvider>
  );
}
