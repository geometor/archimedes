:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _archimedes-about:
.. _archimedes-mission:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

**GEOMETOR • archimedes** establishes the scholarly Digital Scriptorium **3-Track Book Codex** and cross-corpus concordance of **Archimedes of Syracuse** (c. 287–212 BC). Reconstructed from Sir Thomas Little Heath's landmark Cambridge University Press editions—*The Works of Archimedes* (1897) and *The Method of Archimedes, Recently Discovered by Heiberg* (1912 Supplement)—collated against Johan Ludvig Heiberg's critical Teubner Greek and Latin texts (*Archimedis Opera Omnia cum commentariis Eutocii*, 1880–1881 / 1910–1915), this codex gathers the foundational masterpieces of ancient constructive, mechanical, and infinitesimal mathematics across seven unified units.

The codex extracts Archimedes's deductive corpus into synchronized **English**, **Summary**, and **Notes** tracks illustrated with 11 calibrated, resolution-independent ``.euclid-graphic`` vector plates. Every unit is reconstructed into machine-addressable semantic entities: bounding :math:`3\frac{10}{71} < \pi < 3\frac{1}{7}` by 96-gon rational interval recurrences in *Measurement of a Circle*, proving theoretical statics and center of gravity concurrency in *Equilibrium of Planes*, squaring the parabola and spiral, establishing the :math:`2 : 3` sphere-to-cylinder ratio, transmitting the *Arbelos*, *Twin Circles*, *Neusis Trisection*, and *Salinon* in the *Book of Lemmas*, and unveiling infinitesimal mechanical slice calculus in the Palimpsest *Method*.

Within the GEOMETOR ecosystem, this edition completes Heath's Cambridge Greek Trilogy alongside ``geometor/apollonius`` (*Treatise on Conic Sections*) and ``geometor/euclid`` (*The Thirteen Books of Euclid's Elements*). It resolves Heath's Archimedean citations across Euclid's *Elements* (``geometor.elements``), anchors Kimberling triangle center **Centroid ``X(2)``** in theoretical mechanics (``geometor.etc``), unites the *Arbelos* and the 13 Semi-Regular Solids with Pappus of Alexandria (``geometor.pappus``), links golden-ratio polyhedra over :math:`\mathbb{Q}(\phi)` to Luca Pacioli (``geometor.pacioli``, ``geometor.divine``), and maps the Archimedes-Heron area theorem to Rational Trigonometry's Quadrea (``geometor.wildberger``).

The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by **phi ARCHITECT**, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge. The mission unfolds across three essential pillars:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises—elevating prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (using ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic fields rather than floating-point approximations.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across ``geometor.com``.

Sources, Provenance & Methodology
---------------------------------

Three Streams of Textual Transmission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our knowledge of Archimedes' works descends through three extraordinary historical channels, all represented across the seven units of this codex:

1. **Archetype Codex A (Byzantine Minuscule, 9th c. → Renaissance)**: Compiled in ninth-century Constantinople in the school of Leo the Mathematician, translated word-for-word into Latin at Viterbo in 1269 by William of Moerbeke (Vatican *Ottob. lat. 1850*), copied by fifteenth-century Italian humanists before disappearing after 1564, and printed in the 1544 Basel *editio princeps*. Preserves *Sphere and Cylinder* I–II, *Measurement of a Circle*, *Conoids and Spheroids*, *On Spirals*, *Equilibrium of Planes* I–II, *The Sand-Reckoner*, *Quadrature of the Parabola*, and Eutocius's Greek commentaries.
2. **The Arabic Tradition (*Kitāb al-Maʾkhūdhāt*)**: Ninth-century Baghdad geometer Thābit ibn Qurra translated the fifteen planar propositions of the *Book of Lemmas* into Arabic; Abraham Ecchellensis and Giovanni Alfonso Borelli published the Latin translation *Liber Assumptorum* at Florence in 1661, preserving the *Arbelos*, *Twin Circles*, *Neusis Trisection*, and *Salinon*.
3. **Codex C — The Archimedes Palimpsest (10th c. → 1906 Discovery)**: A tenth-century Constantinople parchment scraped and overwritten in the thirteenth century as a Christian Euchologion, examined by Johan Ludvig Heiberg in 1906. Restored the Greek text of *On Floating Bodies*, uncovered fragments of the 14-piece *Stomachion*, and recovered the lost masterpiece **The Method of Mechanical Theorems Addressed to Eratosthenes**, translated into English in T. L. Heath's 1912 Cambridge Supplement.

Public-Domain Archival Provenance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All primary editions used in ``geometor.archimedes`` are 100% public-domain works whose metadata records are archived and SHA-256 checksummed in ``resources/works/sources_manifest.json``:

* **Heath (1897)**: *The Works of Archimedes*, Cambridge University Press (Internet Archive ``worksofarchimede00arch``).
* **Heath (1912)**: *The Method of Archimedes, Recently Discovered by Heiberg*, Cambridge University Press (Internet Archive ``methodofarchimed00archiala``).
* **Heiberg Vol. I (1880)**: *Archimedis Opera Omnia cum commentariis Eutocii*, Vol. I, B. G. Teubner, Leipzig (Internet Archive ``archimedisoperao01arch``).
* **Heiberg Vol. II (1881)**: *Archimedis Opera Omnia cum commentariis Eutocii*, Vol. II, B. G. Teubner, Leipzig (Internet Archive ``archimedisoperao02arch``).

Digital Scriptorium Methodology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Strict Content / Code Separation**: Authoritative historical prose and Syracusan mathematical demonstrations remain unencumbered by embedded scripting; figures are generated as standalone, calibrated vector graphics.
* **Synchronized Multi-Track Codex**: Side-by-side reading across unabridged English text, concise mathematical synopses, and extensive commentary notes.
* **Machine-Queryable Concordance**: Full Heiberg–Heath–GEOMETOR concordance linking classical citations to modern symbolic models.
