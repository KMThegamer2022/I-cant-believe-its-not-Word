# ⚠️ I can't believe it's not Word ⚠️

> ## 🚨 DISCLAIMER — READ THIS FIRST 🚨
>
> **This is NOT a replacement for Microsoft Word.**
>
> This project is a **hobby/educational experiment** that attempts to recreate the Microsoft Word interface and as many features as possible using nothing but a single HTML file, CSS, and vanilla JavaScript running in your browser.
>
> **It is very broken.** Many features are incomplete, buggy, or only partially implemented. Some things look like they work but don't. Others work in unexpected ways. Expect crashes, weird behavior, and things that simply don't do what the button says.
>
> **Do NOT use this for important documents.** There is no cloud backup, no real auto-save to a server, no collaboration, and no guarantee your work won't disappear. Save early, save often, and keep your own backups.
>
> **Do NOT expect Word compatibility.** This will not correctly open .docx files, will not interoperate with Microsoft 365, and will not produce professionally formatted documents. It renders HTML, not OOXML.
>
> **Found a bug?** [Open an issue!](../../issues) — That's literally how this project improves.
>
> **Have a suggestion?** [Open an issue!](../../issues/new?template=suggestion.md) — Feature requests, UI improvements, and "hey this button does nothing" reports are all welcome.
>
> **Want to help fix it?** [Open a PR!](../../pulls) — The code is modular, reasonably commented, and (mostly) readable.

---

A web-based word processor that tries really hard to look and feel like Microsoft Word. Built for people on Chromebooks, school computers, or any locked-down machine where you can't install Office but still need to write something.

## ✨ What Actually Works (Sort Of)

| Area | Status | Notes |
|------|--------|-------|
| Ribbon tabs (all 10) | ✅ | Switch correctly since v4.0 |
| Rich text editing | ✅ | Bold, italic, underline, etc. |
| Font controls | ✅ | Family, size, colors, effects |
| Paragraph controls | ✅ | Alignment, lists, indent, spacing |
| Styles (Heading 1-3, Title) | ✅ | Applied correctly |
| Tables | ✅ | Grid picker insertion, exported to .docx |
| Images | ✅ | Insert from device, exported to .docx |
| **Dark mode (default)** | ✅ | New in v5.0, toggled in Settings/theme cycle |
| **Save / Save As (.docx)** | ✅ | Real OOXML, opens in Word — new in v5.0 |
| **Open (.docx)** | ✅ | Reads headings/lists/tables/images — new in v5.0 |
| **AutoSave + Restore** | ✅ | Non-blocking banner on reload — fixed in v5.0 |
| **Share via email** | ✅ | Web Share API → clipboard+mailto fallback |
| **Contextual Picture tab** | ✅ | Auto-shows on image selection — new in v5.0 |
| **Accessibility Assistant** | ✅ | Right-click menu + fixes — new in v5.0 |
| **Word/page count** | ✅ | Status bar + dialog + Info panel |
| **Settings dialog** | ✅ | General/Display/Proofing/Save/Accessibility |
| Shapes & SmartArt | ⚠️ | Basic SVG shapes only |
| Charts | ⚠️ | Canvas-drawn, not data-driven |
| Find & Replace | ✅ | Works |
| Comments | ✅ | Basic sidebar |
| Track Changes | ⚠️ | Visual only, no real tracking |
| Draw tab | ✅ | Pen/highlighter/eraser, page-only, Esc to exit |
| Watermarks | ✅ | Text only |
| Page layout | ✅ | Margins, orientation, size, columns |
| Table of Contents | ✅ | Auto-generated from headings |
| Footnotes | ⚠️ | Basic superscript + footer |
| Citations | ⚠️ | Format-only, no source database |
| Mail Merge | ⚠️ | CSV import + field insertion |
| Macros | ⚠️ | Basic recorder, no real VBA |
| File backstage | ✅ | All panels work since v4.0 |
| Read Aloud | ✅ | Uses Web Speech API |
| Dictation | ✅ | Uses Web Speech API (Chrome) |
| Zoom & Views | ✅ | Read/Print/Web/Outline/Draft |
| Copilot AI | ❌ | Removed in v2.0 |

### ❌ Still NOT Working

| Area | Problem |
|------|---------|
| **.docx round-trip fidelity** | SmartArt, charts, footnotes, section breaks, tracked changes, embedded fonts are not imported/exported |
| **Page breaks** | Visual only — auto-pagination is approximate, not a real layout engine |
| **Drawing ink → .docx** | Ink is canvas strokes; it does not export into the .docx |
| **Zoom (older Firefox)** | CSS `zoom` works in Chrome/Edge but may fail in older Firefox |
| **Insert tab extras** | Charts, 3D models, screenshots are still mostly decorative |
| **Mail Merge** | Cannot talk to a real mail server |

## 🚀 Quick Start

1. Download `I cant believe its not Word.html`
2. Open it in Chrome, Edge, Firefox, or Safari
3. Start typing
4. Encounter bugs
5. [Report them](../../issues)

## 📁 Project Structure

```
├── I cant believe its not Word.html   ← the actual product (open this)
├── build.py                           ← combines modules into one file
├── README.md                          ← you are here
└── versions/
    ├── v1.0/     ← initial release (broken tabs)
    ├── v2.0/     ← fixed tabs/layout, removed Copilot
    ├── v3.0/     ← internal — never released
    ├── v4.0/     ← tabs, backstage, drawing fixed
    └── v5.0/     ← current (dark mode, real .docx, contextual tabs)
        └── modules/ (9 files)
```

## 🔧 Building from Source

```bash
python3 build.py          # build latest version
python3 build.py v5.0     # build specific version
python3 build.py --list   # list all versions
```

## 📋 Versioning

| Version | Status | Changes |
|---------|--------|---------|
| v1.0 | ❌ Broken | Initial build. Tabs didn't switch. |
| v2.0 | ⚠️ Less broken | Fixed tabs/layout, removed Copilot. |
| v3.0 | — | Internal only, never released. |
| v4.0 | ⚠️ Mostly working | Tabs switch, backstage works, drawing is page-only. |
| **v5.0** | ✅ **Current** | **Dark mode, real .docx save/open, AutoSave restore, contextual Picture tab, Accessibility Assistant, Settings dialog.** |

### Planned for v6.0
- Better .docx fidelity (footnotes, section breaks, tracked changes)
- True auto-pagination while typing
- Data-driven charts
- Mail merge against a real mail server
- Export ink drawings into .docx

## 🐛 Reporting Issues

**This is the most important section.**

Every bug you find makes this project better. When filing an issue, please include:

1. **What you were doing** — "I clicked the Table button on the Insert tab"
2. **What you expected** — "A table should be inserted"
3. **What actually happened** — "Nothing happened" or "The page crashed"
4. **Your browser** — Chrome/Firefox/Safari/Edge + version
5. **Screenshots** — If possible, a screenshot helps enormously

Use the [bug report template](../../issues/new?template=bug_report.md) — it has all these fields pre-filled.

## 💡 Suggestions

Got an idea for a feature? Think something could work better? [Open a suggestion](../../issues/new?template=suggestion.md)!

## 🤝 Contributing

1. Fork the repo
2. Create a version branch: `git checkout -b v5.0-my-fix`
3. Edit the modules in `versions/v5.0/modules/`
4. Test by running `python3 build.py v5.0`
5. Open a PR

## 📜 Legal Stuff

- This project is **not affiliated with, endorsed by, or connected to Microsoft** in any way.
- "Microsoft Word" and "Office" are trademarks of Microsoft Corporation.
- This is a parody/educational project for entertainment purposes.
- The UI is **inspired by** but does not copy Microsoft's proprietary code or assets.
- Icons are Unicode characters and emoji, not Microsoft assets.

## 📄 License

MIT — Do whatever you want with it. Just don't blame us when it eats your essay.
