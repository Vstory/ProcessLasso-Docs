# AGENTS.md

Notes for anyone (human or agent) updating this mirror.

## What this repository is

A Markdown mirror of the official Process Lasso documentation at
<https://bitsum.com/apps/process-lasso/docs/>. The site is built by MkDocs with
the Material theme through GitHub Actions (`.github/workflows/pages.yml`) and
published to GitHub Pages.

- `docs/` — one Markdown file per documentation page, plus `docs/media/` for screenshots
- `mkdocs.yml` — site configuration, theme, plugins, and the full navigation
- `README.md` — repository front page; not part of the built site

## Source of truth

The upstream site, not this repository. Content here is fetched, never invented.
When upstream changes, re-fetch and re-check; do not hand-edit prose into a shape
that differs from upstream, except for Markdown formatting.

## Fetching

Page list comes from the site's own sitemap, so new pages are not missed:

```
https://bitsum.com/apps/process-lasso/docs/sitemap.xml
```

Conversion rules used when the mirror was created:

- Navigation order and section names are taken from the site's sidebar (`nav.md-nav--primary`), not from the URL tree.
- HTML is read as bytes; decoding it through a guessed charset turns em dashes and quotes into mojibake.
- In-page links to other pages become relative `.md` links with anchors preserved; off-site links stay absolute.
- Screenshots are downloaded into `docs/media/` and referenced relatively.
- MkDocs admonitions become blockquotes with a bold title, definition lists become bullet items.

## Naming

- Page files are lowercase with hyphens: `rules/cpu-affinities.md`, `reference/ini-config.md`.
- A section landing page, when upstream has one, is `index.md` inside the section directory.
- Directory names mirror the site sections: `getting-started`, `interface`, `rules`, `algorithms`, `power`, `tools`, `reference`, `deployment`, `help`.

## Adding a translated edition

The site is set up for `mkdocs-static-i18n` with `docs_structure: folder`:

1. Add pages under `docs/<locale>/` (for Simplified Chinese: `docs/zh/`).
2. In `mkdocs.yml`, change that language's `build: false` to `true`.
3. Remove the locale from `exclude_docs` if it was added there.
4. Add `nav_translations` for the language so the sidebar follows the translation.

English remains the default locale and falls back automatically for missing pages.

## Checks before pushing

- Build locally with `pip install -r requirements.txt && mkdocs build` when possible; CI also builds.
- Relative links must point at existing files; `Check links` runs lychee in offline mode for this.
- Do not add a license file: the documentation is Bitsum's copyrighted material and this
  repository only mirrors it for offline reading.
