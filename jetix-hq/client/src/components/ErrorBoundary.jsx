import { Component } from 'react';
import { AlertTriangle, RotateCcw } from 'lucide-react';

export default class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('[ErrorBoundary]', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex items-center justify-center h-full min-h-[200px]">
          <div className="text-center">
            <div className="p-4 bg-ctp-surface0 rpg-clip inline-block mb-4">
              <AlertTriangle size={32} className="text-ctp-red" />
            </div>
            <h3 className="font-pixel text-[10px] text-ctp-red mb-2">SOMETHING BROKE</h3>
            <p className="text-xs text-ctp-overlay1 max-w-xs mb-4">
              {this.state.error?.message || 'An unexpected error occurred'}
            </p>
            <button
              onClick={() => this.setState({ hasError: false, error: null })}
              className="inline-flex items-center gap-2 px-4 py-2 bg-ctp-surface1 text-ctp-text text-xs rpg-clip hover:bg-ctp-surface2 transition-colors"
            >
              <RotateCcw size={12} /> Try Again
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
