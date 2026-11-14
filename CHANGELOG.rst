=========
Changelog
=========

0.1.1 (2026-11-13)
------------------

- Curated and mapped primary-source folio links across *The Works of Archimedes* and *The Method* (37/37 directives and 21/21 badges resolved).

0.1.0 (2026-11-12)
------------------

* Established the 7-unit synchronized 3-track **Book Codex** (``:layout: book``, 21 track files) of *The Works of Archimedes* (Heath 1897) and *The Method of Archimedes* (Heath 1912 Supplement), collated via 300 DPI multimodal vision against J. L. Heiberg's Teubner *Opera Omnia* (1880–1881).
* Generated 11 theme-adaptive ``.euclid-graphic`` SVG vector plates in ``docsrc/_static/figures/`` via ``scripts/build_figures.py``.
* Authored ``resources/works/{concordance,citations,persons,glossary,sources_manifest}.json`` covering 34 canonical loci, 30 citations (100% of ``geometor/euclid`` Archimedes citation keys), 27 historical persons, and 23 Greek/Latin/English technical terms.
* Implemented ``geometor.archimedes`` package (``concordance``, ``compile_codex``, ``sphinx_ext``, ``cli``) and full pytest verification suite.
