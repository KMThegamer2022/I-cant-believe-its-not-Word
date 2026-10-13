# v4.0 — Tab Switching, Backstage & Drawing Fixes

**Status:** Partially working

## What's Fixed ✅
- **Ribbon tabs now switch correctly** — Root cause was a single extra `)` in a string literal creating a syntax error. Tab switching is now in its own standalone script with three layers of protection (inline onclick, event delegation, CSS class + inline style).
- **File backstage buttons work** — `closeBackstage()` and `showBackstagePanel()` moved to standalone scripts. All panels (New, Open, Info, Save As, Print, Share, Export, Account, Options) render correctly. Back arrow works.
- **Drawing is confined to the page** — Canvas moved inside the editor page. You can only draw on the white page area, not the whole screen.
- **Drawing mode can be disabled** — Press Escape or click "Draw on Page" again to exit. A red indicator pill appears at the bottom while drawing mode is active.
- **QAT buttons work** — Save, Undo, Redo, Print Preview all have working onclick handlers.

## What's NOT Working Yet ❌ (Next Release)
- **Save to device** — The download function has issues in some browsers. The file may not appear in your Downloads folder reliably.
- **Open from device** — File picker may not load the document correctly in all browsers.
- **Share via email** — The mailto: link opens but doesn't attach the file. Needs a different approach.
- **AutoSave** — Saves to browser localStorage but the restore prompt on reload is unreliable.
- **Page breaks** — Visual page break markers exist but auto-pagination doesn't trigger reliably while typing.
- **Zoom** — Uses CSS `zoom` which works in Chrome/Edge but may not work in older Firefox.

These are all **scheduled for v5.0**.

## Changes from v3.0
- Standalone script tags for tab switching and backstage functions
- Drawing canvas moved inside editor-page
- Escape key exits drawing mode
- Draw mode indicator pill
- All backstage panels rewritten with simple string concatenation (no template literals)
