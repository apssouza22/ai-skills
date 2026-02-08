---
name: excalidraw-artist
description: Create beautiful, elegant Excalidraw diagrams based on user intent. Use when user asks to draw, visualize, diagram, sketch, illustrate concepts, create flowcharts, architecture diagrams, mind maps, process flows, or any visual representation. Triggers on keywords like "draw", "diagram", "visualize", "sketch", "flowchart", "architecture", "mind map", "illustrate".
---

# Excalidraw Artist

Create elegant, high-quality Excalidraw diagrams and automatically preview in browser.

## ⚠️ CRITICAL: NO Crossing Lines

**Lines and arrows must NEVER cross each other.** This is the #1 rule for professional diagrams.

Before generating any diagram:
1. Plan node positions to avoid any line intersections
2. Use consistent flow direction (left-to-right OR top-to-bottom)
3. Rearrange nodes if needed to eliminate crossings
4. Use vertical/horizontal alignment to keep connections clean

## Workflow

1. **Analyze user intent** - Understand what they want to visualize
2. **Choose diagram type** - Flowchart, architecture, mind map, comparison, etc.
3. **Design element layout** - Plan positions, sizes, colors for visual harmony
4. **Generate HTML** - Create diagram using the template
5. **Auto-open browser** - Preview immediately

## Element Reference

See [references/elements.md](references/elements.md) for:
- Element types and properties
- Color palette recommendations
- Layout guidelines

See [references/diagram-patterns.md](references/diagram-patterns.md) for:
- Common diagram patterns
- Recommended dimensions
- Spacing guidelines

## Implementation

### Generate the HTML file

Write an HTML file with this structure, replacing the `elementsData` array with designed elements:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Excalidraw Preview</title>
  <link rel="stylesheet" href="https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.css" />
  <script>
    window.EXCALIDRAW_ASSET_PATH = "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/";
  </script>
  <script type="importmap">
    {
      "imports": {
        "react": "https://esm.sh/react@19.0.0",
        "react/jsx-runtime": "https://esm.sh/react@19.0.0/jsx-runtime",
        "react-dom": "https://esm.sh/react-dom@19.0.0",
        "react-dom/client": "https://esm.sh/react-dom@19.0.0/client"
      }
    }
  </script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body, #app { height: 100%; width: 100%; }
  </style>
</head>
<body>
  <div id="app"></div>
  <script type="module">
    import React from "https://esm.sh/react@19.0.0";
    import { createRoot } from "https://esm.sh/react-dom@19.0.0/client";
    import * as ExcalidrawLib from "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.js?external=react,react-dom";

    const { Excalidraw, convertToExcalidrawElements } = ExcalidrawLib;

    const elementsData = [
      // INSERT DESIGNED ELEMENTS HERE
    ];

    const elements = convertToExcalidrawElements(elementsData);

    function App() {
      return React.createElement(
        "div",
        { style: { height: "100%", width: "100%" } },
        React.createElement(Excalidraw, {
          initialData: {
            elements: elements,
            appState: { viewBackgroundColor: "#ffffff" },
            scrollToContent: true,
          },
          langCode: "en",
        })
      );
    }

    const root = createRoot(document.getElementById("app"));
    root.render(React.createElement(App));
  </script>
</body>
</html>
```

### Open in browser

After writing the HTML file, run:

```bash
open <path-to-file>.html
```

## Design Principles

1. **Visual balance** - Distribute elements evenly, maintain consistent spacing
2. **Color harmony** - Use complementary colors, limit palette to 3-4 colors
3. **Clear hierarchy** - Size and color indicate importance
4. **Readable text** - Appropriate font sizes, good contrast
5. **Logical flow** - Arrows and lines guide the eye naturally

## Quick Examples

### Simple Flowchart
```javascript
[
  { type: "rectangle", x: 100, y: 100, width: 160, height: 60, backgroundColor: "#a5d8ff", strokeColor: "#1971c2" },
  { type: "text", x: 180, y: 130, text: "Start", fontSize: 20 },
  { type: "arrow", x: 260, y: 130, width: 60, height: 0, strokeColor: "#495057" },
  { type: "rectangle", x: 320, y: 100, width: 160, height: 60, backgroundColor: "#b2f2bb", strokeColor: "#2f9e44" },
  { type: "text", x: 400, y: 130, text: "Process", fontSize: 20 },
  { type: "arrow", x: 480, y: 130, width: 60, height: 0, strokeColor: "#495057" },
  { type: "rectangle", x: 540, y: 100, width: 160, height: 60, backgroundColor: "#ffec99", strokeColor: "#f08c00" },
  { type: "text", x: 620, y: 130, text: "End", fontSize: 20 }
]
```

### Architecture Diagram
```javascript
[
  { type: "rectangle", x: 100, y: 50, width: 200, height: 80, backgroundColor: "#d0bfff", strokeColor: "#7048e8" },
  { type: "text", x: 200, y: 90, text: "Frontend", fontSize: 24, textAlign: "center" },
  { type: "arrow", x: 200, y: 130, width: 0, height: 40, strokeColor: "#495057" },
  { type: "rectangle", x: 100, y: 170, width: 200, height: 80, backgroundColor: "#a5d8ff", strokeColor: "#1971c2" },
  { type: "text", x: 200, y: 210, text: "Backend", fontSize: 24, textAlign: "center" },
  { type: "arrow", x: 200, y: 250, width: 0, height: 40, strokeColor: "#495057" },
  { type: "rectangle", x: 100, y: 290, width: 200, height: 80, backgroundColor: "#b2f2bb", strokeColor: "#2f9e44" },
  { type: "text", x: 200, y: 330, text: "Database", fontSize: 24, textAlign: "center" }
]
```
