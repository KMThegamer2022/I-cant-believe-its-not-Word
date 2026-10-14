# v5.0 — Dark Mode, Real .docx Save/Open, Contextual Tabs

**Status:** Mostly working. This is the most feature-packed release so far.

> **Reminder:** this is not Microsoft Word. It is a single HTML file that tries very
> hard to look like Word and mostly succeeds at looking at it. It will never be a
> real replacement. Report bugs in the **Issues** tab — suggestions are welcome.

## What's New / Fixed ✅

### Dark mode by default
- The whole UI (title bar, ribbon, panes, status bar, backstage) is dark out of the box.
- The **page** is dark too by default. Toggle it from the status bar (page-mode button) or View tab.
- A **Settings** dialog (gear in the title bar, or File → Options) lets you switch:
  General / Display / Proofing / Save / Accessibility / About. All settings persist.
- Theme cycle button in the title bar: **dark → light → system**. Preferences are saved to
  `localStorage` and survive reloads. A flash-prevention script in `<head>` applies the theme
  before first paint, so there is no white flash on load.

### Real file saving, AutoSave and exporting
- **Save / Save As** now produce a genuine `.docx` (a hand-rolled ZIP of OOXML parts) that
  opens in real Microsoft Word, LibreOffice and Google Docs. Also exports **`.rtf`**, **`.html`**,
  **`.txt`** and a Word-readable **`.doc`** (HTML-based). PDF export uses the print dialog.
- **Open** reads a real `.docx` back into the editor (headings, bold/italic/underline, colours,
  highlighting, lists, tables, hyperlinks and images), plus `.html`, `.rtf` and `.txt`.
- **AutoSave** toggle in the title bar. It debounces and writes to browser storage without
  blocking typing, and shows a **non-blocking Restore banner** on reload (no modal dialogs).
- **Share** opens your default email app (mailto with the document attached via a fallback that
  copies the content and opens the mail client). Falls back to the Web Share API where available.

### Contextual tabs
- Selecting a picture auto-shows a **Picture Format** contextual tab: brightness/contrast/colour,
  artistic filters, compress, crop, picture styles, text wrapping, align, rotate, size and alt text.
- The tab hides again when you select text instead.

### Accessibility Assistant
- Right-click anywhere for a custom context menu (cut/copy/paste plus a full **Accessibility
  Assistant** section): alt-text, contrast, heading structure, links, tables and reading-order
  checks, each with a one-click **Fix** and an overall score.
- A mini formatting toolbar appears on selection.
- The **Home tab → Voice & Accessibility** group and the status-bar **Accessibility** indicator
  both open the assistant pane.

### Ribbon and status bar
- Every ribbon tab was rebuilt to match the reference screenshots: Home, Insert, Draw (with a
  **Select** tool), Design, Layout, References, Mailings, Review, View, Help, and the contextual
  Picture Format tab.
- The status bar shows live **page X of Y**, **word count** and **character count**; clicking the
  count opens a full Word Count dialog (words, characters, paragraphs, lines, pages).
- Added working **Sort**, **Add-ins** and **Signature Line** features (all three previously
  referenced buttons that did nothing).

## What's Still Broken ❌
- **Page breaks** are visual only. Auto-pagination while typing is approximate (based on zoom and
  page height), not a true layout engine.
- **.docx round-trip** is good but not lossless. Exotic Word features (SmartArt, charts, footnotes,
  section breaks, tracked changes, embedded fonts) are **not** imported or exported.
- **Zoom** uses CSS transforms; very large documents (hundreds of pages) will get slow.
- **Track Changes** shows the visual markup but does not keep a full revision history, so "Accept
  All" cannot restore the original.
- **Mail Merge** generates the documents but obviously cannot talk to a real mail server.
- **Drawing ink** is stored as canvas strokes; it is not saved into the exported `.docx`.
- The **Insert tab** (charts, 3D models, screenshots) is still mostly decorative.

## Technical Notes
- Built from 8 numbered module files (`00`–`08`) combined by `build.py`. Module `08` contains the
  ZIP/OOXML engine (CRC32 + `CompressionStream`) and the RTF writer.
- All inline `onclick` handlers were audited against defined functions. Three previously-missing
  functions (`showSortDialog`, `showAddins`, `insertSignatureLine`) were added.
- The ink canvas is recreated on demand so that importing a document does not destroy it.

## Changes from v4.0
- Dark theme is now the default (was light-only).
- Real `.docx` export and import (was a fake HTML "docx").
- AutoSave restore is now a non-blocking banner (was an unreliable prompt).
- Contextual Picture Format tab.
- Custom context menu with Accessibility Assistant.
- Settings dialog with persistable preferences.
- Fixed: `zoomLevel` TDZ error that broke module 05 at load, table export (checked for a `tbl`
  block type that was never produced), RTF colour table (missing separators), and the sticky
  Picture Format tab that would not hide.
