# Platform-native candidates

Use this reference to generate candidates after checking repository-local patterns. A native feature is not automatically smaller if it changes supported-runtime coverage, accessibility, localization, security, or data semantics.

## Browser and CSS

- Date, time, color, and range inputs: `<input type="date">`, `time`, `color`, or `range`
- Modal dialog: `<dialog>` with `showModal()`
- Disclosure: `<details><summary>…</summary></details>`
- Simple options: `<datalist>`
- Layout: CSS grid, flex, `minmax`, `clamp`, and container queries
- Scroll behavior: `scroll-behavior`, `position: sticky`, and scroll snap

Check keyboard interaction, form behavior, browser support, and the product's styling requirements before replacing a component.

## JavaScript and browser APIs

- Query strings: `URLSearchParams`
- Deep clone: `structuredClone`
- IDs: `crypto.randomUUID()`
- Dates, numbers, and currency: `Intl.DateTimeFormat`, `Intl.NumberFormat`, and `Intl.RelativeTimeFormat`
- Clipboard and share: `navigator.clipboard.writeText` and `navigator.share`
- Fetch timeout: `AbortSignal.timeout(...)`
- Viewport observation: `IntersectionObserver` and `ResizeObserver`
- Simple events: `EventTarget` and `CustomEvent`

Confirm compatibility and semantic equivalence first; for example, cloning class instances or replacing timezone-aware formatting can change behavior.

## Node.js and Python

- Node paths and files: `node:path`, `fs.mkdir(..., { recursive: true })`, `fs.rm(..., { recursive: true, force: true })`, and `JSON.parse(await fs.readFile(...))`
- Node collections: `[...new Set(values)]` and `array.flat(depth)`
- Python records and filesystem: `dataclasses.dataclass` and `pathlib`
- Python dates and CLI: `datetime`, `zoneinfo`, and `argparse`
- Python data tools: `json`, `functools.lru_cache`, `itertools`, `collections.defaultdict`, and `Counter`

## Database

Prefer database constraints and queries when the rule belongs to the data model: `UNIQUE`, `FOREIGN KEY`, `CHECK`, `DISTINCT`, `ON CONFLICT`, window functions, recursive CTEs, and native JSON operations.

Use an application-layer rule or dependency when it is necessary for portability, compatibility, scale, correctness, or ergonomics.
