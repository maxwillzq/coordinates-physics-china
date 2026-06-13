# Project: Coordinates Book Part 2 Refinement

## Architecture
- Source Materials: `/sources`
- Knowledge Database: `/wiki/entities/` and `/wiki/concepts/`
- Documentation Source (Chinese): `website/docs/part2.md`
- Documentation Source (English): `website/i18n/en/docusaurus-plugin-content-docs/current/part2.md`
- Build Output: Static HTML files generated via Docusaurus `npm run build`

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Wiki Database Ingestion | Research and create/update Wiki entity and concept files, update wiki index and log | None | DONE |
| 2 | Restructure Chinese Edition | Rewrite `website/docs/part2.md` using `style_template.md` and `part2_refinement_plan.md` | M1 | DONE |
| 3 | Synchronize English Translation | Translate and align `website/i18n/en/.../part2.md` with updated Chinese version | M2 | DONE |
| 4 | Compilation & Verification | Build the website via `npm run build` and verify all formatting, images, and KaTeX | M3 | DONE |

## Interface Contracts
- **Wiki Structure**: Every new entity and concept must follow standard Markdown structures, link back/forth to related entries, and be listed in `/wiki/index.md`.
- **Docusaurus Frontmatter & Layout**: Both Chinese and English editions of `part2.md` must share the same frontmatter keys, header illustration (`pathname:///img/part2_illustration.png`), and structural outline.
- **LaTeX Math Padding**: All inline and block equations must be padded with spaces (` $...$ ` or ` $$...$$ `) to prevent MDX build failures.

## Code Layout
- `.agents/`: Coordination files and subagent work directories
- `wiki/entities/`: Historical figure biographies (Li Shanlan, Xu Shou, etc.)
- `wiki/concepts/`: Physics paradigm concepts (Chong Xue, Carnot cycle, etc.)
- `website/docs/`: Docusaurus Chinese documents
- `website/i18n/en/docusaurus-plugin-content-docs/current/`: Docusaurus English documents
