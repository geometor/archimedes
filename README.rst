=====================
GEOMETOR • archimedes
=====================

Scholarly **Digital Scriptorium Book Codex** (``:layout: book``), **11 calibrated ``.euclid-graphic`` SVG vector plates**, and programmatic **Heiberg–Heath–GEOMETOR Concordance** for **Archimedes of Syracuse** (c. 287–212 BC):

* **T. L. Heath (ed. & trans.)**, *The Works of Archimedes*, Cambridge University Press, 1897 (PD).
* **T. L. Heath (ed. & trans.)**, *The Method of Archimedes, Recently Discovered by Heiberg: A Supplement to The Works of Archimedes, 1897*, Cambridge University Press, 1912 (PD).
* **J. L. Heiberg (ed.)**, *Archimedis Opera Omnia cum commentariis Eutocii*, Vols. I–III, B. G. Teubner, Leipzig, 1880–1881 / 2nd ed. 1910–1915 (PD).

Seven-Unit Synchronized Book Codex
----------------------------------

Compiled via ``photon-platform/publish`` in ``docsrc/works/`` with three synchronized reading tracks per unit (``-en.rst``, ``-summary.rst``, ``-notes.rst`` = **21 track files**):

1. **Unit 1 — Measurement of a Circle** (``measurement-of-a-circle``): Circle-to-triangle rectification (:math:`A = \frac{1}{2}Cr`) and 96-gon rational interval bisection (:math:`3\frac{10}{71} < \pi < 3\frac{1}{7}`).
2. **Unit 2 — On the Equilibrium of Planes, Books I–II** (``equilibrium-of-planes``): Seven Postulates of statics, commensurable & incommensurable Law of the Lever (I.6–7), concurrency of triangle medians at **Centroid ``X(2)``** (I.13–14, ``geometor/etc``), and the :math:`3 : 2` centroid of the parabolic segment (II.8).
3. **Unit 3 — Quadrature of the Parabola** (``quadrature-of-parabola``): Epistle to Dositheus, Archimedes' Lemma, mechanical balance exhaustion (Props. 1–17), and pure geometric :math:`1/4^n` exhaustion proving :math:`\text{Segment} = \frac{4}{3}\triangle ABC` (Props. 18–24).
4. **Unit 4 — Sphere and Cylinder, On Spirals & Conoids and Spheroids** (``sphere-spirals-conoids``): Convexity postulates (*ἐπὶ τὰ αὐτὰ κοῖλα*), surface :math:`4\pi r^2` & the :math:`2 : 3` Tomb Theorem, Eutocius's cubic intersection for II.4, kinematic spiral subtangent rectification & :math:`1/3` quadrature, and cubature of paraboloids, hyperboloids, and spheroids.
5. **Unit 5 — Book of Lemmas (*Liber Assumptorum*)** (``book-of-lemmas``): Complete 15-proposition planar treasury preserved by Thābit ibn Qurra—*Arbelos*, *Archimedes' Twin Circles*, :math:`6 : 19` inscribed circle & Pappus chain, *neusis* angle trisection, orthogonal-chord quadrance invariant, *Salinon*, and golden-ratio pentagon/decagon secants.
6. **Unit 6 — The Method of Mechanical Theorems (*Ephodos*)** (``method-of-mechanical-theorems``): Palimpsest treatise to Eratosthenes crediting Democritus and Eudoxus, slice-lever discovery of the parabola and sphere, and cubature of the cylindrical ungula (Props. 12–14) and bicylinder (Prop. 15).
7. **Unit 7 — Semi-Regular Solids, *Stomachion* & *The Sand-Reckoner*** (``semi-regular-solids-arenarius``): Complete structural register of the **13 Archimedean Polyhedra** (Pappus V.19 & ``geometor/pacioli`` over :math:`\mathbb{Q}(\phi)`), the 14-piece *Stomachion*, the *Cattle Problem*, and *The Sand-Reckoner* to King Gelon preserving Aristarchus's heliocentric universe and myriad-octads up to :math:`10^{8 \cdot 10^{16}}`.

Development & Verification (Python 3.13 / ``uv``)
-------------------------------------------------

.. code-block:: bash

   # Regenerate apparatus RST tables and sync root JSONs
   python3 scripts/compile_codex.py compile-apparatus

   # Rebuild calibrated .euclid-graphic SVG plates
   python3 scripts/build_figures.py

   # Verify SHA-256 provenance, euclid citation coverage, 21 tracks & SVGs
   python3 scripts/compile_codex.py verify

   # Run linter, tests & Sphinx Book Codex build
   ruff check src scripts tests
   pytest
   publish build

License
-------

MIT License — Copyright (c) 2026 phi ARCHITECT / GEOMETOR. Primary texts of Archimedes, Eutocius, Pappus, Heiberg (1880–1915), and Heath (1897, 1912) are in the public domain worldwide.
