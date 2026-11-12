:order: 32
:type: notes
:canonical_id: quadrature-of-parabola
:folio: Heath 1897, pp. 233–252 · Heiberg II, 294–353

.. _unit-quadrature-of-parabola-notes:

Quadrature of the Parabola — Philological & Mathematical Notes
==============================================================

1. Title & Pre-Apollonian Conic Terminology
-------------------------------------------

* As :person:`Heath <heath>` (:cite:`heath:1897`, p. 233) notes, the manuscript title *Τετραγωνισμὸς παραβολῆς* cannot have been :person:`Archimedes' <archimedes>` own original heading: throughout the body of the treatise (and in *Conoids and Spheroids* and *The Method*), Archimedes never writes *παραβολή* for the curve—a term coined shortly afterward by :person:`Apollonius of Perga <apollonius>` from Pythagorean application of areas—but always **ὀρθογωνίου κώνου τομή** (*section of a right-angled cone*, :term:`τμῆμα ὀρθογωνίου κώνου τομῆς <tmema-paraboles>`).
* Notice the three-stage epistemological progression across Archimedes' corpus:
  1. **Heuristic Line-Slice Discovery**: :doc:`The Method, Prop. 1 <method-of-mechanical-theorems-en>` (weighing chords :g:`MO` one-by-one, discovered first).
  2. **Rigorous Mechanical Exhaustion**: *Quadrature*, Props. 6–17 (replacing lines by finite-width trapezia compressed via :term:`Archimedes' Lemma <archimedes-lemma>`).
  3. **Pure Synthetic Exhaustion**: *Quadrature*, Props. 18–24 (eliminating mechanics altogether via the :eq:`1/4^n` triangle tree).

2. Affine Invariance of the :eq:`4/3` Ratio
-------------------------------------------

Notice that Archimedes proves :eq:`\text{Segment} = \frac{4}{3}\triangle ABC` for **every** chord :g:`AC`—not merely chords perpendicular to the axis of symmetry! In affine coordinates aligned with the diameter :g:`BV` (parallel to the axis) and tangent :g:`BT` (parallel to :g:`AC`), the parabola has equation :eq:`y^2 = 2px` regardless of obliquity, and because oblique shear preserves area ratios, both :eq:`\triangle ADB + \triangle BEC = \frac{1}{4}\triangle ABC` (Prop. 21) and :eq:`\text{Segment} = \frac{4}{3}\triangle ABC` (Prop. 24) are **affine invariants**.

3. GEOMETOR Cross-Corpus Concordance
------------------------------------

* **Euclid (`geometor/euclid`)** (:cite:`geometor:euclid`): Directly cited via ``archimedes:quadrature-of-parabola`` in Heath's commentary on *Elements* X.1 (bisection exhaustion) and XII.2/XII.10.
* **Hilbert (`geometor/hilbert`)** (:cite:`hilbert:1899`): The Preface to *Quadrature of the Parabola* (alongside *Sphere and Cylinder* I, Assump. 5) is the locus classicus from which **Axiom V 1 (Archimedes' Axiom)** enters modern axiomatic geometry and real analysis.
