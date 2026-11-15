=========
Changelog
=========

0.1.5 (2026-11-15)
------------------

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.4 (2026-11-15)
------------------

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2 (2026-11-14)
------------------

- **changed**: Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- Curated and mapped primary-source folio links across *The Works of Archimedes* and *The Method* (37/37 directives and 21/21 badges resolved).

0.1.0 (2026-11-12)
------------------

* Established the 7-unit synchronized 3-track **Book Codex** (``:layout: book``, 21 track files) of *The Works of Archimedes* (Heath 1897) and *The Method of Archimedes* (Heath 1912 Supplement), collated via 300 DPI multimodal vision against J. L. Heiberg's Teubner *Opera Omnia* (1880–1881).
* Generated 11 theme-adaptive ``.euclid-graphic`` SVG vector plates in ``docsrc/_static/figures/`` via ``scripts/build_figures.py``.
* Authored ``resources/works/{concordance,citations,persons,glossary,sources_manifest}.json`` covering 34 canonical loci, 30 citations (100% of ``geometor/euclid`` Archimedes citation keys), 27 historical persons, and 23 Greek/Latin/English technical terms.
* Implemented ``geometor.archimedes`` package (``concordance``, ``compile_codex``, ``sphinx_ext``, ``cli``) and full pytest verification suite.
