# Excalidraw Element Reference

## Basic Element Structure

All elements share these base properties:

```javascript
{
  type: "rectangle" | "ellipse" | "diamond" | "line" | "arrow" | "text" | "freedraw",
  x: number,           // X position
  y: number,           // Y position
  width: number,       // Element width (not for text/freedraw)
  height: number,      // Element height (not for text/freedraw)
  strokeColor: string, // Border/stroke color (hex)
  backgroundColor: string, // Fill color (hex or "transparent")
  fillStyle: "solid" | "hachure" | "cross-hatch", // Fill pattern
  strokeWidth: 1 | 2 | 4, // Line thickness
  roughness: 0 | 1 | 2,   // 0=architect, 1=artist, 2=cartoonist
  opacity: number,        // 0-100
  roundness: { type: 1 | 2 | 3 } | null, // Corner rounding
}
```

## Element Types

### Rectangle
```javascript
{ type: "rectangle", x: 100, y: 100, width: 200, height: 100, backgroundColor: "#a5d8ff", strokeColor: "#1971c2" }
```

### Ellipse
```javascript
{ type: "ellipse", x: 100, y: 100, width: 150, height: 150, backgroundColor: "#b2f2bb", strokeColor: "#2f9e44" }
```

### Diamond
```javascript
{ type: "diamond", x: 100, y: 100, width: 120, height: 120, backgroundColor: "#ffec99", strokeColor: "#f08c00" }
```

### Text
```javascript
{ type: "text", x: 100, y: 100, text: "Hello World", fontSize: 20, width: 160, fontFamily: 1, textAlign: "center" }
```
- **`width`: REQUIRED** - Must set explicit width to prevent text truncation
  - Short text (1-5 chars): width = 80
  - Medium text (6-12 chars): width = 160
  - Long text (13+ chars): width = 240+
  - Or calculate: `width = text.length * fontSize * 0.6`
- `fontSize`: 16 (small), 20 (medium), 28 (large), 36 (extra large)
- `fontFamily`: 1 (hand-drawn), 2 (normal), 3 (code)
- `textAlign`: "left" | "center" | "right"

### Arrow
```javascript
{ type: "arrow", x: 100, y: 100, width: 200, height: 0, strokeColor: "#e03131" }
```
- Positive width = right, negative = left
- Positive height = down, negative = up
- Combine for diagonal arrows

### Line
```javascript
{ type: "line", x: 100, y: 100, width: 200, height: 100, strokeColor: "#1971c2" }
```

### Freedraw (for custom paths)
```javascript
{ type: "freedraw", x: 0, y: 0, points: [[0,0], [10,20], [30,10]], strokeColor: "#1971c2" }
```

## Color Palette (Recommended)

### Blues
- Light: `#a5d8ff`, Stroke: `#1971c2`
- Medium: `#74c0fc`, Stroke: `#1864ab`

### Greens
- Light: `#b2f2bb`, Stroke: `#2f9e44`
- Medium: `#8ce99a`, Stroke: `#37b24d`

### Yellows
- Light: `#ffec99`, Stroke: `#f08c00`
- Medium: `#ffe066`, Stroke: `#e67700`

### Reds
- Light: `#ffc9c9`, Stroke: `#e03131`
- Medium: `#ff8787`, Stroke: `#c92a2a`

### Purples
- Light: `#d0bfff`, Stroke: `#7048e8`
- Medium: `#b197fc`, Stroke: `#6741d9`

### Grays
- Light: `#e9ecef`, Stroke: `#495057`
- Medium: `#dee2e6`, Stroke: `#343a40`

### Accent Colors
- Orange: `#ffd8a8` / `#e8590c`
- Pink: `#fcc2d7` / `#d6336c`
- Cyan: `#99e9f2` / `#0c8599`

## Layout Guidelines

### Spacing
- Minimum padding between elements: 40px
- Group spacing: 80-100px
- Text padding inside shapes: 20px

### Alignment
- Center important elements
- Use consistent vertical/horizontal spacing
- Align related elements on same axis

### Visual Hierarchy
- Use larger shapes for main concepts
- Use bolder colors for emphasis
- Use arrows to show relationships

## Common Patterns

### Flowchart Node
```javascript
[
  { type: "rectangle", x: 0, y: 0, width: 160, height: 60, backgroundColor: "#a5d8ff", strokeColor: "#1971c2", roundness: { type: 3 } },
  { type: "text", x: 80, y: 30, text: "Step 1", fontSize: 20, textAlign: "center" }
]
```

### Connection Arrow
```javascript
{ type: "arrow", x: 160, y: 30, width: 60, height: 0, strokeColor: "#495057" }
```

### Decision Diamond
```javascript
{ type: "diamond", x: 0, y: 0, width: 100, height: 80, backgroundColor: "#ffec99", strokeColor: "#f08c00" }
```

### Container/Group Box
```javascript
{ type: "rectangle", x: 0, y: 0, width: 300, height: 200, backgroundColor: "transparent", strokeColor: "#dee2e6", strokeStyle: "dashed" }
```
