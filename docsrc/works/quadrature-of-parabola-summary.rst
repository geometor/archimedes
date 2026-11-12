:order: 31
:type: summary
:canonical_id: quadrature-of-parabola
:folio: Heath 1897, pp. 233–252 · Heiberg II, 294–353

.. _unit-quadrature-of-parabola-summary:

Quadrature of the Parabola — Analytical Summary
===============================================

*Scope*: **Heiberg Vol. II, pp. 294–353** · **Heath (1897), pp. 233–252** · *Letter to Dositheus & Propositions 1–24*

Two Complementary Demonstrations of :eq:`\text{Segment} = \frac{4}{3}\triangle ABC`
-----------------------------------------------------------------------------------

*Quadrature of the Parabola* (:cite:`archimedes:quadrature-of-parabola`) presents the earliest exact area of a conic section in history, proved twice by independent engines:

1. **Mechanical Exhaustion (Props. 1–17)**: Slices the segment into :eq:`n` finite rectilinear trapezia (avoiding indivisibles of zero width, unlike :doc:`The Method <method-of-mechanical-theorems-en>`) and suspends them from a balance beam against the tangent triangle :g:`\triangle QqT = 4\triangle ABC`, proving :eq:`\text{Segment} = \frac{1}{3}\triangle QqT = \frac{4}{3}\triangle ABC`.
2. **Geometric Exhaustion (Props. 18–24)**: Recursively fills the two residual arches on :g:`AB`, :g:`BC` with secondary triangles :g:`\triangle ADB`, :g:`\triangle BEC` whose combined area is always :eq:`\frac{1}{4}` of the preceding stage, and closes the double reductio via the telescoping finite identity :eq:`\sum_{k=0}^{n} \frac{A}{4^k} + \frac{1}{3}\frac{A}{4^n} = \frac{4}{3}A` (Prop. 23) without ever invoking an actual infinite sum!

Structural Map of Propositions 1–24
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 28 54

   * - Block
     - Propositions
     - Mathematical Role
   * - Preface
     - Epistle to :person:`Dositheus <dositheus>`
     - Tribute to :person:`Conon <conon>`; statement of :term:`Archimedes' Lemma <archimedes-lemma>` & Eudoxean precedents
   * - Conic Lemmas
     - Props. 1–5
     - Pre-Apollonian parabola symptomata & tangent-chord intercept ratio :eq:`QO : Oq = ER : RO`
   * - Statics Lemmas
     - Props. 6–13
     - Lever equilibrium and upper/lower moment bounds for suspended triangles and trapezia
   * - Mechanical Proof
     - Props. 14–17
     - Compression between :eq:`n` circumscribed and inscribed trapezia :eq:`\implies \frac{4}{3}\triangle ABC`
   * - Exhaustion Tree
     - Props. 18–22
     - Binary parabolic triangle tree: each generation adds :eq:`2^k \cdot (\frac{1}{8})^k A = \frac{1}{4^k}A`
   * - Telescoping Sum
     - Props. 23–24
     - Exact finite remainder :eq:`\frac{1}{3}Z` + double reductio ad absurdum :eq:`\implies \frac{4}{3}\triangle ABC`
