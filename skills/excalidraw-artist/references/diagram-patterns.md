# Diagram Patterns

## Critical Layout Rules

### NO Crossing Lines
**Lines and arrows must NEVER cross each other.** Crossing lines make diagrams messy and hard to read.

Strategies to avoid crossings:
1. **Rearrange nodes** - Move nodes to different positions to eliminate crossings
2. **Use consistent flow direction** - Stick to left-to-right or top-to-bottom
3. **Add vertical/horizontal spacing** - Spread elements further apart
4. **Use different levels** - Place elements on different horizontal or vertical rows
5. **Route arrows around** - Use longer paths that go around obstacles instead of through

### Text Width
**All text elements MUST have explicit width property** to prevent truncation.
- Text x position should match the container's x position
- Text width should match the container's width
- Use `textAlign: "center"` to center text within the width

## Flowcharts

### Horizontal Flow
```
[Start] --> [Process] --> [Decision] --> [End]
```

Layout strategy:
- Start at x=100, y=200
- Each node: width=160, height=60
- Spacing between nodes: 80px (arrow width=60, gap=20)
- Center text in each node

### Vertical Flow
```
[Start]
   |
   v
[Process]
   |
   v
[End]
```

Layout strategy:
- Start at x=300, y=50
- Vertical spacing: 100px between nodes
- Arrow height=40, gap=20

### Decision Branch
```
        [Yes] --> [Action A]
       /
[Decision]
       \
        [No] --> [Action B]
```

## Architecture Diagrams

### Three-Tier
```
+------------------+
|   Presentation   |
+------------------+
        |
+------------------+
|    Business      |
+------------------+
        |
+------------------+
|      Data        |
+------------------+
```

### Microservices
```
+-------+  +-------+  +-------+
|  API  |  | Auth  |  | Users |
+-------+  +-------+  +-------+
    \         |         /
     \        |        /
      +---------------+
      |   Database    |
      +---------------+
```

## Mind Maps

### Central Topic
```
                [Branch 1]
                    |
[Branch 4] --- [Central] --- [Branch 2]
                    |
                [Branch 3]
```

Layout:
- Central node at canvas center (400, 300)
- Branches radiate at 90-degree angles
- Use consistent distance (200px) from center

## Sequence Diagrams

### Simple Request-Response
```
[Client]        [Server]        [Database]
    |               |               |
    |-- Request --->|               |
    |               |-- Query ----->|
    |               |<-- Result ----|
    |<-- Response --|               |
```

## Comparison Charts

### Side-by-Side
```
+------------+     +------------+
|  Option A  |     |  Option B  |
+------------+     +------------+
| Feature 1  |     | Feature 1  |
| Feature 2  |     | Feature 2  |
| Feature 3  |     | Feature 3  |
+------------+     +------------+
```

### Pros/Cons
```
+-------------------+
|      Topic        |
+---------+---------+
|  Pros   |  Cons   |
+---------+---------+
| + Good  | - Bad   |
| + Nice  | - Issue |
+---------+---------+
```

## Process Diagrams

### Linear Process
```
[1] --> [2] --> [3] --> [4] --> [5]
```

### Cycle
```
    +---> [Step 1] ---+
    |                 |
    |                 v
[Step 4]         [Step 2]
    ^                 |
    |                 v
    +--- [Step 3] <---+
```

## Recommended Dimensions

| Element Type | Width | Height |
|-------------|-------|--------|
| Small node | 120 | 50 |
| Medium node | 160 | 60 |
| Large node | 200 | 80 |
| Decision diamond | 100 | 80 |
| Actor/person | 60 | 100 |
| Database cylinder | 80 | 60 |
| Cloud shape | 140 | 80 |

## Text Sizing

| Context | Font Size |
|---------|-----------|
| Title | 36 |
| Heading | 28 |
| Node label | 20 |
| Description | 16 |
| Annotation | 14 |

## Spacing Guidelines

| Relationship | Distance |
|-------------|----------|
| Tight grouping | 20-40px |
| Related elements | 60-80px |
| Separate groups | 100-150px |
| Major sections | 200+ px |
