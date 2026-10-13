# v3.0 — Bug Fix Release (Issues #1–#4)

**Status:** Working

## Fixes from GitHub Issues

### Issue #1: Menus don't switch ✅
- Added inline `onclick="switchTab(this)"` to every tab (bulletproof)
- Wrapped event delegation in try-catch as backup
- `switchTab()` function with error logging

### Issue #2: Save doesn't work ✅
- New `downloadBlob()` helper that appends anchor to DOM before clicking
- Delayed URL revocation (1s timeout instead of instant)
- Full try-catch with user-friendly error messages
- Alert now says "check your Downloads folder"

### Issue #3: Page doesn't break ✅
- Added `.page-break` CSS class with dashed line + "Page Break" label
- `insertPageBreak()` now inserts a visible break + new paragraph with cursor placement
- `checkAutoPageBreak()` runs on every keystroke — inserts break markers when content exceeds page height (1056px = 11")
- Status bar page count uses actual break count

### Issue #4: Zoom doesn't work ✅
- Replaced `transform: scale()` (broke scrolling) with CSS `zoom` property
- Added fallback for browsers without `zoom` support (transform + dimension adjustment)
- Zoom slider, buttons, and One Page/Page Width all use the new function

### Additional fixes
- QAT buttons (Save/Undo/Redo/Print Preview) now have onclick handlers
- All functions wrapped in try-catch for better error visibility

## Changes from v2.0
- Tab switching is now bulletproof (inline handlers + event delegation backup)
- Save appends anchor to DOM for reliable downloads
- Page breaks are visible and auto-generated
- Zoom uses CSS zoom for proper scrolling
