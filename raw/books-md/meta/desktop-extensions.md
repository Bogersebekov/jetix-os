---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: meta-expert
priority: P2
quality_grade: A
slug: desktop-extensions
subcategory: meta
tags:
- meta
title: Desktop Extensions
word_count: 2846
---

<div id="main-content" role="main">

<div class="section page-wrapper HeroEngineering-module-scss-module__j1ivRa__hero"
aria-label="Engineering Article Hero">

<a href="../engineering.html"
class="body-2 bold HeroEngineering-module-scss-module__j1ivRa__hubLink">Engineering
at Anthropic</a>

<div class="HeroEngineering-module-scss-module__j1ivRa__content">

<div class="HeroEngineering-module-scss-module__j1ivRa__header">

<div class="HeroEngineering-module-scss-module__j1ivRa__heroImage">

<img
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/1d7118b992792989576d23bb279bbf3e38c37618-1000x1000.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="1000" height="1000" />

</div>

# Desktop Extensions: One-click MCP server installation for Claude Desktop

</div>

<div class="HeroEngineering-module-scss-module__j1ivRa__metadata">

Published Jun 26, 2025

Desktop Extensions make installing MCP servers as easy as clicking a
button. We share the technical architecture and tips for creating good
extensions.

</div>

</div>

</div>

<div class="page-wrapper">

<div>

<div class="Body-module-scss-module__z40yvW__body" theme="ivory">

<div class="Body-module-scss-module__z40yvW__reading-column">

- <div class="body-3 LatestUpdates-module-scss-module__sg7Vka__headline">

  File extension update

  Sep 11, 2025

  </div>

  Claude Desktop Extensions now use the .mcpb (MCP Bundle) file
  extension instead of .dxt. Existing .dxt extensions will continue to
  work, but we recommend developers use .mcpb for new extensions going
  forward. All functionality remains the same - this is purely a naming
  convention update.

</div>

—

When we released the Model Context Protocol (MCP) last year, we saw
developers build amazing local servers that gave Claude access to
everything from file systems to databases. But we kept hearing the same
feedback: installation was too complex. Users needed developer tools,
had to manually edit configuration files, and often got stuck on
dependency issues.

Today, we're introducing Desktop Extensions—a new packaging format that
makes installing MCP servers as simple as clicking a button.

### Addressing the MCP installation problem

Local MCP servers unlock powerful capabilities for Claude Desktop users.
They can interact with local applications, access private data, and
integrate with development tools—all while keeping data on the user's
machine. However, the current installation process creates significant
barriers:

- **Developer tools required**: Users need Node.js, Python, or other
  runtimes installed
- **Manual configuration**: Each server requires editing JSON
  configuration files
- **Dependency management**: Users must resolve package conflicts and
  version mismatches
- **No discovery mechanism**: Finding useful MCP servers requires
  searching GitHub
- **Update complexity**: Keeping servers current means manual
  reinstallation

These friction points meant that MCP servers, despite their power,
remained largely inaccessible to non-technical users.

### Introducing Desktop Extensions

Desktop Extensions (`.mcpb` files) solve these problems by bundling an
entire MCP server—including all dependencies—into a single installable
package. Here's what changes for users:

**Before:**

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
# Install Node.js first 
npm install -g @example/mcp-server 
# Edit ~/.claude/claude_desktop_config.json manually 
# Restart Claude Desktop 
# Hope it works
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

**After:**

1.  Download a `.mcpb` file
2.  Double-click to open with Claude Desktop
3.  Click "Install"

That's it. No terminal, no configuration files, no dependency conflicts.

## Architecture overview

A Desktop Extension is a zip archive containing the local MCP server as
well as a `manifest.json`, which describes everything Claude Desktop and
other apps supporting desktop extensions need to know.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
extension.mcpb (ZIP archive)
├── manifest.json         # Extension metadata and configuration
├── server/               # MCP server implementation
│   └── [server files]    
├── dependencies/         # All required packages/libraries
└── icon.png             # Optional: Extension icon

# Example: Node.js Extension
extension.mcpb
├── manifest.json         # Required: Extension metadata and configuration
├── server/               # Server files
│   └── index.js          # Main entry point
├── node_modules/         # Bundled dependencies
├── package.json          # Optional: NPM package definition
└── icon.png              # Optional: Extension icon

# Example: Python Extension
extension.mcpb (ZIP file)
├── manifest.json         # Required: Extension metadata and configuration
├── server/               # Server files
│   ├── main.py           # Main entry point
│   └── utils.py          # Additional modules
├── lib/                  # Bundled Python packages
├── requirements.txt      # Optional: Python dependencies list
└── icon.png              # Optional: Extension icon
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

The only required file in a Desktop Extension is a manifest.json. Claude
Desktop handles all the complexity:

- **Built-in runtime**: We ship Node.js with Claude Desktop, eliminating
  external dependencies
- **Automatic updates**: Extensions update automatically when new
  versions are available
- **Secure secrets**: Sensitive configuration like API keys are stored
  in the OS keychain

The manifest contains human-readable information (like the name,
description, or author), a declaration of features (tools, prompts),
user configuration, and runtime requirements. Most fields are optional,
so the minimal version is quite short, although in practice, we expect
all three supported extension types (Node.js, Python, and classic
binaries/executables) to include files:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
{
  "mcpb_version": "0.1",                    // MCPB spec version this manifest conforms to
  "name": "my-extension",                   // Machine-readable name (used for CLI, APIs)
  "version": "1.0.0",                       // Semantic version of your extension
  "description": "A simple MCP extension",  // Brief description of what the extension does
  "author": {                               // Author information (required)
    "name": "Extension Author"              // Author's name (required field)
  },
  "server": {                               // Server configuration (required)
    "type": "node",                         // Server type: "node", "python", or "binary"
    "entry_point": "server/index.js",       // Path to the main server file
    "mcp_config": {                         // MCP server configuration
      "command": "node",                    // Command to run the server
      "args": [                             // Arguments passed to the command
        "${__dirname}/server/index.js"      // ${__dirname} is replaced with the extension's directory
      ]                              
    }
  }
}
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

There are a number of convenience options [available in the manifest
spec](https://github.com/anthropics/dxt/blob/main/MANIFEST.md) that aim
to make the installation and configuration of local MCP servers easier.
The server configuration object can be defined in a way that makes room
both for user-defined configuration in the form of template literals as
well as platform-specific overrides. Extension developers can define, in
detail, what kind of configuration they want to collect from users.

Let’s take a look at a concrete example of how the manifest aids with
configuration. In the manifest below, the developer declares that the
user needs to supply an `api_key`. Claude will not enable the extension
until the user has supplied that value, keep it automatically in the
operating system’s secret vault, and transparently replace the
`${user_config.api_key}` with the user-supplied value when launching the
server. Similarly, `${__dirname}` will be replaced with the full path to
the extension’s unpacked directory.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
{
  "mcpb_version": "0.1",
  "name": "my-extension",
  "version": "1.0.0",
  "description": "A simple MCP extension",
  "author": {
    "name": "Extension Author"
  },
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"],
      "env": {
        "API_KEY": "${user_config.api_key}"
      }
    }
  },
  "user_config": {
    "api_key": {
      "type": "string",
      "title": "API Key",
      "description": "Your API key for authentication",
      "sensitive": true,
      "required": true
    }
  }
}
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

A full `manifest.json` with most of the optional fields might look like
this:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
{
  "mcpb_version": "0.1",
  "name": "My MCP Extension",
  "display_name": "My Awesome MCP Extension",
  "version": "1.0.0",
  "description": "A brief description of what this extension does",
  "long_description": "A detailed description that can include multiple paragraphs explaining the extension's functionality, use cases, and features. It supports basic markdown.",
  "author": {
    "name": "Your Name",
    "email": "yourname@example.com",
    "url": "https://your-website.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/your-username/my-mcp-extension"
  },
  "homepage": "https://example.com/my-extension",
  "documentation": "https://docs.example.com/my-extension",
  "support": "https://github.com/your-username/my-extension/issues",
  "icon": "icon.png",
  "screenshots": [
    "assets/screenshots/screenshot1.png",
    "assets/screenshots/screenshot2.png"
  ],
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"],
      "env": {
        "ALLOWED_DIRECTORIES": "${user_config.allowed_directories}"
      }
    }
  },
  "tools": [
    {
      "name": "search_files",
      "description": "Search for files in a directory"
    }
  ],
  "prompts": [
    {
      "name": "poetry",
      "description": "Have the LLM write poetry",
      "arguments": ["topic"],
      "text": "Write a creative poem about the following topic: ${arguments.topic}"
    }
  ],
  "tools_generated": true,
  "keywords": ["api", "automation", "productivity"],
  "license": "MIT",
  "compatibility": {
    "claude_desktop": ">=1.0.0",
    "platforms": ["darwin", "win32", "linux"],
    "runtimes": {
      "node": ">=16.0.0"
    }
  },
  "user_config": {
    "allowed_directories": {
      "type": "directory",
      "title": "Allowed Directories",
      "description": "Directories the server can access",
      "multiple": true,
      "required": true,
      "default": ["${HOME}/Desktop"]
    },
    "api_key": {
      "type": "string",
      "title": "API Key",
      "description": "Your API key for authentication",
      "sensitive": true,
      "required": false
    },
    "max_file_size": {
      "type": "number",
      "title": "Maximum File Size (MB)",
      "description": "Maximum file size to process",
      "default": 10,
      "min": 1,
      "max": 100
    }
  }
}
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

To see an extension and manifest, please refer [to the examples in the
MCPB repository](https://github.com/anthropics/dxt/tree/main/examples).

The full specification for all required and optional fields in the
`manifest.json` can be found as part of our [open-source
toolchain](https://github.com/anthropics/dxt/blob/main/MANIFEST.md).

### Building your first extension

Let's walk through packaging an existing MCP server as a Desktop
Extension. We'll use a simple file system server as an example.

#### Step 1: Create the manifest

First, initialize a manifest for your server:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
npx @anthropic-ai/mcpb init
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

This interactive tool asks about your server and generates a complete
manifest.json. If you want to speed-run your way to the most basic
manifest.json, you can run the command with a --yes parameter.

#### Step 2: Handle user configuration

If your server needs user input (like API keys or allowed directories),
declare it in the manifest:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
"user_config": {
  "allowed_directories": {
    "type": "directory",
    "title": "Allowed Directories",
    "description": "Directories the server can access",
    "multiple": true,
    "required": true,
    "default": ["${HOME}/Documents"]
  }
}
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

Claude Desktop will:

- Display a user-friendly configuration UI
- Validate inputs before enabling the extension
- Securely store sensitive values
- Pass configuration to your server either as arguments or environment
  variables, depending on developer configuration

In the example below, we’re passing the user configuration as an
environment variable, but it could also be an argument.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
"server": {
   "type": "node",
   "entry_point": "server/index.js",
   "mcp_config": {
   "command": "node",
   "args": ["${__dirname}/server/index.js"],
   "env": {
      "ALLOWED_DIRECTORIES": "${user_config.allowed_directories}"
   }
   }
}
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

#### Step 3: Package the extension

Bundle everything into a `.mcpb` file:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
npx @anthropic-ai/mcpb pack
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

This command:

1.  Validates your manifest
2.  Generates the `.mcpb` archive

#### Step 4: Test locally

Drag your `.mcpb` file into Claude Desktop's Settings window. You'll
see:

- Human-readable information about your extension
- Required permissions and configuration
- A simple "Install" button

### Advanced features

#### Cross-platform support

Extensions can adapt to different operating systems:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
"server": {
  "type": "node",
  "entry_point": "server/index.js",
  "mcp_config": {
    "command": "node",
    "args": ["${__dirname}/server/index.js"],
    "platforms": {
      "win32": {
        "command": "node.exe",
        "env": {
          "TEMP_DIR": "${TEMP}"
        }
      },
      "darwin": {
        "env": {
          "TEMP_DIR": "${TMPDIR}"
        }
      }
    }
  }
}
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

#### Dynamic configuration

Use template literals for runtime values:

- `${__dirname}`: Extension's installation directory
- `${user_config.key}`: User-provided configuration
- `${HOME}, ${TEMP}`: System environment variables

#### Feature declaration

Help users understand capabilities upfront:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
"tools": [
  {
    "name": "read_file",
    "description": "Read contents of a file"
  }
],
"prompts": [
  {
    "name": "code_review",
    "description": "Review code for best practices",
    "arguments": ["file_path"]
  }
]
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

### The extension directory

We're launching with a curated directory of extensions built into Claude
Desktop. Users can browse, search, and install with one click—no
searching GitHub or vetting code.

While we expect both the Desktop Extension specification and the
implementation in Claude for macOS and Windows to evolve over time, we
look forward to seeing the many ways in which extensions can be used to
expand the capabilities of Claude in creative ways.

To submit your extension:

1.  Ensure it follows the guidelines found in the submission form
2.  Test across Windows and macOS
3.  [Submit your
    extension](https://docs.google.com/forms/d/14_Dmcig4z8NeRMB_e7TOyrKzuZ88-BLYdLvS6LPhiZU/edit)
4.  Our team reviews for quality and security

### Building an open ecosystem

We are committed to the open ecosystem around MCP servers and believe
that its ability to be universally adopted by multiple applications and
services has benefitted the community. In line with this commitment,
we’re open-sourcing the Desktop Extension specification, toolchain, and
the schemas and key functions used by Claude for macOS and Windows to
implement its own support of Desktop Extensions. It is our hope that the
MCPB format doesn’t just make local MCP servers more portable for
Claude, but other AI desktop applications, too.

We're open-sourcing:

- The complete MCPB specification
- Packaging and validation tools
- Reference implementation code
- TypeScript types and schemas

This means:

- **For MCP server developers**: Package once, run anywhere that
  supports MCPB
- **For app developers**: Add extension support without building from
  scratch
- **For users**: Consistent experience across all MCP-enabled
  applications

The specification and toolchain is on purpose versioned as 0.1, as we
are looking forward to working with the greater community on evolving
and changing the format. We look forward to hearing from you.

### Security and enterprise considerations

We understand that extensions introduce new security considerations,
particularly for enterprises. We've built in several safeguards with the
preview release of Desktop Extensions:

#### For users

- Sensitive data stays in the OS keychain
- Automatic updates
- Ability to audit what extensions are installed

#### For enterprises

- Group Policy (Windows) and MDM (macOS) support
- Ability to pre-install approved extensions
- Blocklist specific extensions or publishers
- Disable the extension directory entirely
- Deploy private extension directories

For more information about how to manage extensions within your
organization, see our
[documentation](https://support.anthropic.com/en/articles/10949351-getting-started-with-model-context-protocol-mcp-on-claude-for-desktop).

### Getting started

Ready to build your own extension? Here's how to start:

**For MCP server developers**: Review our [developer
documentation](https://github.com/anthropics/dxt) – or dive right in by
running the following commands in your local MCP servers’ directory:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
npm install -g @anthropic-ai/mcpb
mcpb init
mcpb pack
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

**For Claude Desktop users**: Update to the latest version and look for
the Extensions section in Settings

**For enterprises**: Review our enterprise documentation for deployment
options

### Building with Claude Code

Internally at Anthropic, we have found that Claude is great at building
extensions with minimal intervention. If you too want to use Claude
Code, we recommend that you briefly explain what you want your extension
to do and then add the following context to the prompt:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
I want to build this as a Desktop Extension, abbreviated as "MCPB". Please follow these steps:

1. **Read the specifications thoroughly:**
   - https://github.com/anthropics/mcpb/blob/main/README.md - MCPB architecture overview, capabilities, and integration patterns
   - https://github.com/anthropics/mcpb/blob/main/MANIFEST.md - Complete extension manifest structure and field definitions
   - https://github.com/anthropics/mcpb/tree/main/examples - Reference implementations including a "Hello World" example

2. **Create a proper extension structure:**
   - Generate a valid manifest.json following the MANIFEST.md spec
   - Implement an MCP server using @modelcontextprotocol/sdk with proper tool definitions
   - Include proper error handling and timeout management

3. **Follow best development practices:**
   - Implement proper MCP protocol communication via stdio transport
   - Structure tools with clear schemas, validation, and consistent JSON responses
   - Make use of the fact that this extension will be running locally
   - Add appropriate logging and debugging capabilities
   - Include proper documentation and setup instructions

4. **Test considerations:**
   - Validate that all tool calls return properly structured responses
   - Verify manifest loads correctly and host integration works

Generate complete, production-ready code that can be immediately tested. Focus on defensive programming, clear error messages, and following the exact
MCPB specifications to ensure compatibility with the ecosystem.
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

### Conclusion

Desktop Extensions represent a fundamental shift in how users interact
with local AI tools. By removing installation friction, we're making
powerful MCP servers accessible to everyone—not just developers.

Internally, we’re using desktop extensions to share highly experimental
MCP servers - some fun, some useful.. One team experimented to see how
far our models could make it when directly connected to a GameBoy,
similar to our [“Claude plays Pokémon”
research](https://www.anthropic.com/news/visible-extended-thinking). We
used Desktop Extensions to package a single extension that opens up the
popular [PyBoy](https://github.com/Baekalfen/PyBoy) GameBoy emulator and
lets Claude take control. We believe that countless opportunities exist
to connect the model’s capabilities to the tools, data, and applications
users already have on their local machines.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd48f3ea1218a4b90450b9ab8134fa0e24db5a167-720x542.png&amp;w=1920&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd48f3ea1218a4b90450b9ab8134fa0e24db5a167-720x542.png&amp;w=750&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd48f3ea1218a4b90450b9ab8134fa0e24db5a167-720x542.png&amp;w=1920&amp;q=75;w=1920&amp;q=75 2x"
width="720" height="542"
alt="A desktop showing the PyBoy MCP with Super Mario Land start screen" />
</figure>

</div>

We can't wait to see what you build. The same creativity that brought us
thousands of MCP servers can now reach millions of users with just one
click. Ready to share your MCP server?
<a href="https://forms.gle/tyiAZvch1kDADKoP9" target="_blank"
rel="noopener noreferrer">Submit your extension for review</a>.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<a href="https://anthropic.skilljar.com/"
class="ToutCallout-module-scss-module__gZk6bG__root" rel="noopener"
target="_blank"></a>

<div class="ToutCallout-module-scss-module__gZk6bG__illustration bg-cactus">

<img
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="1000" height="1000"
alt="Interlocking puzzle piece with complex geometric shape and detailed surface texture" />

</div>

<div class="ToutCallout-module-scss-module__gZk6bG__content">

<div class="ToutCallout-module-scss-module__gZk6bG__textWrapper">

### Looking to learn more?

</div>

<div class="caption ToutCallout-module-scss-module__gZk6bG__cta">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiBUb3V0Q2FsbG91dC1tb2R1bGUtc2Nzcy1tb2R1bGVfX2daazZiR19faWNvbiIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiB2aWV3Ym94PSIwIDAgMTMgMTMiPjxwYXRoIGQ9Ik01Ljg1IDBDNi4wOTg1MyAwIDYuMyAwLjIwMTQ3MiA2LjMgMC40NUM2LjMgMC42OTg1MjggNi4wOTg1MyAwLjkgNS44NSAwLjlIMS4zNUMxLjEwMTQ3IDAuOSAwLjkgMS4xMDE0NyAwLjkgMS4zNVYxMS4yNUMwLjkgMTEuNDk4NSAxLjEwMTQ3IDExLjcgMS4zNSAxMS43SDExLjI1QzExLjQ5ODUgMTEuNyAxMS43IDExLjQ5ODUgMTEuNyAxMS4yNVY2Ljc1QzExLjcgNi41MDE0NyAxMS45MDE1IDYuMyAxMi4xNSA2LjNDMTIuMzk4NSA2LjMgMTIuNiA2LjUwMTQ3IDEyLjYgNi43NVYxMS4yNUMxMi42IDExLjk5NTYgMTEuOTk1NiAxMi42IDExLjI1IDEyLjZIMS4zNUMwLjYwNDQxNiAxMi42IDEuODExOTdlLTA4IDExLjk5NTYgMCAxMS4yNVYxLjM1QzAgMC42MDQ0MTYgMC42MDQ0MTYgMS40NDk1OWUtMDggMS4zNSAwSDUuODVaTTEyLjE1IDBDMTIuMTgzNiAtMi4zOTA2M2UtMDggMTIuMjE3MiAwLjAwMzkyODA5IDEyLjI1MDIgMC4wMTE0MjU4QzEyLjI3MTIgMC4wMTYyMjkyIDEyLjI5MTcgMC4wMjMwMzE3IDEyLjMxMTcgMC4wMzA3NjE3QzEyLjMxODMgMC4wMzMzMDYzIDEyLjMyNDYgMC4wMzY2ODMgMTIuMzMxMSAwLjAzOTU1MDhDMTIuMzQ5MiAwLjA0NzU0NjggMTIuMzY2OCAwLjA1NjQ0NyAxMi4zODM4IDAuMDY2Nzk2OUMxMi4zOTA3IDAuMDcxMDI3MSAxMi4zOTgyIDAuMDc0NDYzMiAxMi40MDQ5IDAuMDc5MTAxNkMxMi40Mjc0IDAuMDk0NTY3OCAxMi40NDg2IDAuMTEyMjQgMTIuNDY4MiAwLjEzMTgzNkwxMi41MjYyIDAuMjAyMTQ4QzEyLjUzNiAwLjIxNzA0NyAxMi41NDIgMC4yMzM4ODkgMTIuNTQ5OSAwLjI0OTYwOUMxMi41NTUgMC4yNTk3MTEgMTIuNTYxNCAwLjI2OTA0NSAxMi41NjU3IDAuMjc5NDkyQzEyLjU4MTEgMC4zMTY5MSAxMi41ODk5IDAuMzU1OTI2IDEyLjU5NDcgMC4zOTU1MDhDMTIuNTk2OSAwLjQxMzU3MyAxMi42IDAuNDMxNjEgMTIuNiAwLjQ1VjQuMDVDMTIuNiA0LjI5ODUzIDEyLjM5ODUgNC41IDEyLjE1IDQuNUMxMS45MDE1IDQuNSAxMS43IDQuMjk4NTMgMTEuNyA0LjA1VjEuNTM2MzNMNy45NjgxNiA1LjI2ODE2QzcuNzkyNDMgNS40NDM5IDcuNTA3NTcgNS40NDM5IDcuMzMxODQgNS4yNjgxNkM3LjE1NjEgNS4wOTI0MyA3LjE1NjEgNC44MDc1NyA3LjMzMTg0IDQuNjMxODRMMTEuMDYzNyAwLjlIOC41NUM4LjMwMTQ3IDAuOSA4LjEgMC42OTg1MjggOC4xIDAuNDVDOC4xIDAuMjAxNDcyIDguMzAxNDcgNC4yNTIyN2UtMDggOC41NSAwSDEyLjE1WiIgZmlsbD0iIzVFNUQ1OSIgLz48L3N2Zz4="
class="Icon-module-scss-module__lqbdHG__icon ToutCallout-module-scss-module__gZk6bG__icon" />Explore
courses

</div>

</div>

</div>

</div>

</div>

<div class="NewsletterSubscribe-module-scss-module__MOPAja__wrapper">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__content">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__text-content">

## Get the developer newsletter

<div class="NewsletterSubscribe-module-scss-module__MOPAja__body">

Product updates, how-tos, community spotlights, and more. Delivered
monthly to your inbox.

</div>

</div>

<div class="NewsletterSubscribe-module-scss-module__MOPAja__form-container">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__input-wrapper">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB2aWV3Ym94PSIwIDAgMjEgMjEiPjxwYXRoIGQ9Ik00LjE0NTg1IDkuODc0OTJMMTQuNDU4NCA5Ljg3NDkyTDkuNjA0MTkgNS4wNDE1OEwxMC41IDQuMTQ1NzVMMTYuODU0MiAxMC40OTk5TDEwLjUgMTYuODU0MUw5LjYwNDE5IDE1Ljk1ODNMMTQuNDU4NCAxMS4xMjQ5TDQuMTQ1ODUgMTEuMTI0OUw0LjE0NTg1IDkuODc0OTJaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+"
class="Icon-module-scss-module__lqbdHG__icon" />

</div>

Please provide your email address if you'd like to receive our monthly
developer newsletter. You can unsubscribe at any time.

</div>

</div>

</div>

</div>

</div>