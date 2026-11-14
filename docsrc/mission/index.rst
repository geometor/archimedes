:navigation: header
:order: 10
:nav_title: Mission

.. _archimedes-mission:

=======
Mission
=======

``geometor.archimedes`` establishes the scholarly **Digital Scriptorium Book Codex** and machine-queryable concordance of **Archimedes of Syracuse** (c. 287–212 BC) within the **GEOMETOR** ecosystem.

Core Objectives
---------------

1. **Multimodal Folio-Verified Fidelity**: Anchor every unit directly in 300 DPI archival page scans of **Sir Thomas Little Heath's** *The Works of Archimedes* (Cambridge, 1897) and *The Method of Archimedes* (Cambridge, 1912 Supplement), collated with **Johan Ludvig Heiberg's** critical Teubner Greek and Latin editions (*Archimedis Opera Omnia*, 1880–1881 / 1910–1915), with SHA-256 provenance verification in ``resources/works/sources_manifest.json``.
2. **Strict Separation of Historical Codex and Executable Code**: Preserve pure, authoritative historical prose, Syracusan Doric philology, and 11 calibrated theme-adaptive ``.euclid-graphic`` SVG vector plates without embedding Python construction scripts inside treatise RST files—while providing clean programmatic concordance APIs in ``src/geometor/archimedes/``.
3. **Ecosystem Synthesis Across Nine GEOMETOR Pillars**:
   - ``geometor/euclid`` & ``geometor/elements``: Resolve 100% of Heath's Archimedes citation keys across *Elements* Books I, III, IV, V, VI, X, XII, and XIII.
   - ``geometor/etc``: Anchor Kimberling's **Centroid ``X(2)``** and homogeneous barycentric coordinates :eq:`(1 : 1 : 1)` in *On the Equilibrium of Planes* I.13–14.
   - ``geometor/pappus``: Unite the *Arbelos* circle chain (*Synagoge* IV.14), *neusis* trisection, spiral quadrature, and the **13 Semi-Regular Solids** (*Synagoge* V.19).
   - ``geometor/pacioli`` & ``geometor/divine``: Connect the golden-ratio Archimedean polyhedra (`Icosidodecahedron`, `Truncated Icosahedron`, etc.) and *Lemmas* Prop. 15 over :math:`\mathbb{Q}(\phi)` to Luca Pacioli's *De Divina Proportione* (1509).
   - ``geometor/wildberger``: Link *Lemmas* Props. 5 & 11 and Heron–Archimedes triangle area to Rational Trigonometry's polynomial **Quadrea** (*Archimedes' Function*).
   - ``geometor/proclus`` & ``geometor/hilbert``: Trace *Sphere and Cylinder* I Assumptions 1 & 5 to Proclus (*Friedlein* 110) and Hilbert's **Axiom of Continuity (V 1)**.
