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

| Area | Status |
|------|--------|
| Ribbon tabs (all 10) | ✅ They switch now |
| Rich text editing | ✅ Bold, italic, underline, etc. |
| Font controls | ✅ Family, size, colors, effects |
| Paragraph controls | ✅ Alignment, lists, indent, spacing |
| Styles (Heading 1-3, Title) | ✅ Applied correctly |
| Tables | ✅ Grid picker insertion |
| Images | ✅ Insert from device |
| Shapes & SmartArt | ⚠️ Basic SVG shapes |
| Charts | ⚠️ Canvas-drawn, not data-driven |
| Find & Replace | ✅ Works |
| Comments | ✅ Basic sidebar |
| Track Changes | ⚠️ Visual only, no real tracking |
| Draw tab | ✅ Pen/highlighter/eraser on canvas |
| Watermarks | ✅ Text only |
| Page layout | ✅ Margins, orientation, size, columns |
| Table of Contents | ✅ Auto-generated from headings |
| Footnotes | ⚠️ Basic superscript + footer |
| Citations | ⚠️ Format-only, no source database |
| Mail Merge | ⚠️ CSV import + field insertion |
| Macros | ⚠️ Basic recorder, no real VBA |
| Export (PDF/HTML/TXT) | ✅ Via browser print/download |
| Share via email | ✅ Opens mailto: link |
| AutoSave | ⚠️ To browser localStorage only |
| Read Aloud | ✅ Uses Web Speech API |
| Dictation | ✅ Uses Web Speech API (Chrome) |
| Zoom & Views | ✅ Read/Print/Web/Outline/Draft |
| Copilot AI | ❌ Removed in v2.0 |

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
    ├── v1.0/     ← initial release (broken)
    │   └── modules/ (8 files)
    └── v2.0/     ← current (less broken)
        └── modules/ (8 files)
```

## 🔧 Building from Source

```bash
python3 build.py          # build latest version
python3 build.py v2.0     # build specific version
python3 build.py --list   # list all versions
```

## 📋 Versioning

| Version | Status | Changes |
|---------|--------|---------|
| v1.0 | ❌ Broken | Initial build. Tabs didn't switch. |
| v2.0 | ⚠️ Less broken | Fixed tabs, fixed layout, removed Copilot. |

Future versions will follow semver-ish conventions:
- **v2.1, v2.2** — minor fixes, small improvements
- **v3.0** — major features, big changes

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
2. Create a version branch: `git checkout -b v2.1-my-fix`
3. Edit the modules in `versions/v2.1/modules/`
4. Test by running `python3 build.py v2.1`
5. Open a PR

## 📜 Legal Stuff

- This project is **not affiliated with, endorsed by, or connected to Microsoft** in any way.
- "Microsoft Word" and "Office" are trademarks of Microsoft Corporation.
- This is a parody/educational project for entertainment purposes.
- The UI is **inspired by** but does not copy Microsoft's proprietary code or assets.
- Icons are Unicode characters and emoji, not Microsoft assets.

## 📄 License

MIT — Do whatever you want with it. Just don't blame us when it eats your essay.
