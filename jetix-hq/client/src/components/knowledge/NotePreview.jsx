import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeHighlight from 'rehype-highlight';
import { FileWarning, Hash, Calendar, Type } from 'lucide-react';
import { EmptyState } from '../ui';

// Transform [[wikilinks]] into clickable spans
function processWikilinks(content, onNavigate) {
  if (!content) return content;
  return content.replace(
    /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g,
    (_, target, label) => `[${label || target}](#wiki:${target})`
  );
}

export default function NotePreview({ file, loading, onNavigate }) {
  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <p className="text-xs text-ctp-overlay0 animate-pulse">Loading...</p>
      </div>
    );
  }

  if (!file) {
    return (
      <div className="flex items-center justify-center h-full">
        <EmptyState title="Select a file" description="Choose a markdown file from the tree to preview" />
      </div>
    );
  }

  if (file.tooLarge) {
    return (
      <div className="flex items-center justify-center h-full">
        <EmptyState
          icon={FileWarning}
          title="File too large"
          description={`${(file.size / 1024).toFixed(0)} KB — files over 1MB cannot be previewed`}
        />
      </div>
    );
  }

  const processed = processWikilinks(file.content, onNavigate);

  return (
    <div className="flex flex-col h-full">
      {/* Metadata bar */}
      <div className="px-4 py-2 border-b-2 border-ctp-surface0 bg-ctp-mantle/50 flex flex-wrap items-center gap-3 shrink-0">
        <span className="font-pixel text-[10px] text-ctp-text">{file.name?.replace('.md', '')}</span>

        {file.wordCount > 0 && (
          <span className="flex items-center gap-1 text-[10px] text-ctp-overlay0 font-mono">
            <Type size={10} /> {file.wordCount} words
          </span>
        )}

        {file.modified && (
          <span className="flex items-center gap-1 text-[10px] text-ctp-overlay0 font-mono">
            <Calendar size={10} /> {file.modified.slice(0, 10)}
          </span>
        )}

        {file.frontmatter?.tags && (
          <span className="flex items-center gap-1 text-[10px] text-ctp-overlay0 font-mono">
            <Hash size={10} /> {file.frontmatter.tags}
          </span>
        )}

        {file.wikilinks?.length > 0 && (
          <span className="text-[10px] text-ctp-overlay0 font-mono">
            {file.wikilinks.length} links
          </span>
        )}
      </div>

      {/* Markdown content */}
      <div className="flex-1 overflow-y-auto p-6">
        <article className="prose-ctp max-w-none">
          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            rehypePlugins={[rehypeHighlight]}
            components={{
              a({ href, children, ...props }) {
                if (href?.startsWith('#wiki:')) {
                  const target = href.slice(6);
                  return (
                    <button
                      onClick={() => onNavigate?.(target)}
                      className="text-ctp-blue hover:text-ctp-sapphire underline decoration-ctp-blue/30 hover:decoration-ctp-blue cursor-pointer"
                    >
                      {children}
                    </button>
                  );
                }
                return <a href={href} className="text-ctp-blue hover:underline" {...props}>{children}</a>;
              },
              code({ className, children, ...props }) {
                const isInline = !className;
                if (isInline) {
                  return <code className="bg-ctp-surface0 text-ctp-peach px-1 py-0.5 text-xs font-mono" {...props}>{children}</code>;
                }
                return (
                  <code className={`${className} text-xs`} {...props}>{children}</code>
                );
              },
              pre({ children }) {
                return <pre className="bg-ctp-crust border border-ctp-surface0 p-3 overflow-x-auto text-xs">{children}</pre>;
              },
              h1({ children }) { return <h1 className="font-pixel text-lg text-ctp-text mb-4 mt-6">{children}</h1>; },
              h2({ children }) { return <h2 className="font-pixel text-sm text-ctp-text mb-3 mt-5">{children}</h2>; },
              h3({ children }) { return <h3 className="text-sm font-bold text-ctp-subtext1 mb-2 mt-4">{children}</h3>; },
              p({ children }) { return <p className="text-sm text-ctp-subtext0 leading-relaxed mb-3">{children}</p>; },
              ul({ children }) { return <ul className="list-disc list-inside text-sm text-ctp-subtext0 mb-3 space-y-1">{children}</ul>; },
              ol({ children }) { return <ol className="list-decimal list-inside text-sm text-ctp-subtext0 mb-3 space-y-1">{children}</ol>; },
              blockquote({ children }) { return <blockquote className="border-l-4 border-ctp-mauve pl-4 text-sm text-ctp-overlay1 italic mb-3">{children}</blockquote>; },
              table({ children }) { return <table className="w-full text-xs border-collapse mb-3">{children}</table>; },
              th({ children }) { return <th className="border border-ctp-surface1 px-3 py-1.5 bg-ctp-surface0 text-left text-ctp-subtext1 font-mono">{children}</th>; },
              td({ children }) { return <td className="border border-ctp-surface0 px-3 py-1.5 text-ctp-subtext0">{children}</td>; },
              hr() { return <hr className="border-ctp-surface1 my-4" />; },
            }}
          >
            {processed}
          </ReactMarkdown>
        </article>
      </div>
    </div>
  );
}
