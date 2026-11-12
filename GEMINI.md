# GEOMETOR • archimedes

Scholarly **Digital Scriptorium Book Codex** (`:layout: book`), calibrated `.euclid-graphic` vector plates, and cross-corpus concordance for **Archimedes of Syracuse** (c. 287–212 BC): *The Works of Archimedes* (ed. T. L. Heath, 1897) + *The Method of Archimedes* (ed. T. L. Heath, 1912 Supplement), collated against J. L. Heiberg's *Archimedis Opera Omnia cum commentariis Eutocii* (Teubner, 1880–1881 / 1910–1915).

## Architectural Rules

1. **Zero Embedded Python Construction Scripts in Treatise RST**:
   - `docsrc/works/*.rst` must NEVER contain `.. code-block:: python`, `:py_file:`, or `.. literalinclude:: *.py` (enforced by `verify_codex_integrity()`).
   - All geometric diagrams in `docsrc/_static/figures/*.svg` are standalone theme-adaptive `.euclid-graphic` SVGs generated via `scripts/build_figures.py`.
2. **Multimodal Scan Vision Over OCR**:
   - Always inspect 300 DPI page scan PNGs directly via `view_file` when verifying mathematical notation, Greek/Latin orthography, or Heath/Heiberg pagination.
   - Never track large archival `*.pdf` or scratch `*.png` files in git; track provenance metadata and SHA-256 checksums in `resources/works/sources_manifest.json`.
3. **7-Unit Synchronized 3-Track Book Codex (`docsrc/works/`)**:
   - Canonical unit slugs (`CANONICAL_UNIT_SLUGS` in `src/geometor/archimedes/concordance.py`):
     1. `measurement-of-a-circle`
     2. `equilibrium-of-planes`
     3. `quadrature-of-parabola`
     4. `sphere-spirals-conoids`
     5. `book-of-lemmas`
     6. `method-of-mechanical-theorems`
     7. `semi-regular-solids-arenarius`
   - Each unit maintains `-en.rst`, `-summary.rst`, and `-notes.rst` tracks (`21` track files total) plus `concordance.rst`, `bibliography.rst`, `persons.rst`, and `glossary.rst` compiled from `resources/works/*.json` via `scripts/compile_codex.py compile-apparatus`.

## Key Modules (`src/geometor/archimedes/`)

- `concordance.py`: Structured `ConcordanceEntry` loader, `REQUIRED_EUCLID_CITATION_KEYS` validator (`100%` coverage of `geometor/euclid` Archimedes keys), and `verify_sources_manifest()`.
- `compile_codex.py`: Synchronizes `resources/works/{persons,citations,glossary}.json` to `resources/` and compiles apparatus RST pages + `verify_codex_integrity()`.
- `sphinx_ext.py`: Offline-resilient local sibling `objects.inv` resolver (`configure_local_intersphinx`).
- `cli.py`: `geometor-archimedes {summary,compile-apparatus,verify}` CLI.

## Verification Commands

```bash
/home/phi/PROJECTS/geometor/.venv/bin/python scripts/compile_codex.py compile-apparatus
/home/phi/PROJECTS/geometor/.venv/bin/python scripts/compile_codex.py verify
ruff check src scripts tests
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest
publish build
```
