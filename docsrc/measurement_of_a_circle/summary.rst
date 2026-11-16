:order: 11
:type: summary
:canonical_id: measurement-of-a-circle
:folio: Heath 1897, pp. 91–98 · Heiberg I, 258–271

.. _unit-measurement-of-a-circle-summary:

Measurement of a Circle — Analytical Summary
============================================

*Scope*: **Heiberg Vol. I, pp. 258–271** · **Heath (1897), pp. 91–98** · *Propositions 1–3*

Architectural Argument
----------------------

Although briefest among the extant works of :person:`Archimedes <archimedes>`, *Measurement of a Circle* (*Κύκλου μέτρησις*) accomplishes two revolutions in Greek geometry:

1. **Equivalence of Rectification and Quadrature (Prop. 1)**: Where :person:`Euclid <euclid>` in :just:`Elements XII. 2` (:cite:`euclid:elements`) proved only the *proportionality* of two circles to the squares on their diameters (:eq:`C_1 : C_2 = d_1^2 : d_2^2`), Archimedes establishes an *exact areal identity* between a curved boundary and a rectilinear figure: the circle equals the right-angled triangle whose legs are the radius :eq:`r` and the circumference :eq:`C`. Every question of circular area is thereby reduced to a single one-dimensional ratio :eq:`C : d`.
2. **Algorithmic Rational Interval Arithmetic (Prop. 3)**: Starting from the regular hexagon (:eq:`\angle = 30^\circ`) and two extraordinary rational bounds for :eq:`\sqrt{3}`:

   .. math::

      \frac{265}{153} < \sqrt{3} < \frac{1351}{780}, \qquad \left(265^2 - 3\cdot 153^2 = -2, \quad 1351^2 - 3\cdot 780^2 = +1\right),

   Archimedes iterates four half-angle recurrences (:eq:`6 \to 12 \to 24 \to 48 \to 96` sides) using only :just:`Eucl. VI. 3` (angle bisector) and :just:`Eucl. I. 47` (Pythagoras), systematically rounding every square root *downward* in the circumscribed recurrence and *upward* in the inscribed recurrence so that the inequalities remain 100% rigorous at every step.

Step-by-Step 96-Gon Bisection Ledger
------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 14 14 36 36

   * - Stage
     - Polygon
     - Circumscribed Cotangent / Secant Lower Bounds (:eq:`\pi < 3\frac{1}{7}`)
     - Inscribed Cotangent / Cosecant Upper Bounds (:eq:`\pi > 3\frac{10}{71}`)
   * - Seed
     - 6-gon (:eq:`30^\circ`)
     - :eq:`OA : AC > 265 : 153`, :eq:`OC : CA = 306 : 153`
     - :eq:`AC : CB < 1351 : 780`, :eq:`AB : BC = 1560 : 780`
   * - Bisection 1
     - 12-gon (:eq:`15^\circ`)
     - :eq:`OA : AD > 571 : 153`, :eq:`OD : DA > 591\frac{1}{8} : 153`
     - :eq:`AD : DB < 2911 : 780`, :eq:`AB : BD < 3013\frac{3}{4} : 780`
   * - Bisection 2
     - 24-gon (:eq:`7^\circ 30'`)
     - :eq:`OA : AE > 1162\frac{1}{8} : 153`, :eq:`OE : EA > 1172\frac{1}{8} : 153`
     - :eq:`AE : EB < 1823 : 240`, :eq:`AB : BE < 1838\frac{9}{11} : 240`
   * - Bisection 3
     - 48-gon (:eq:`3^\circ 45'`)
     - :eq:`OA : AF > 2334\frac{1}{4} : 153`, :eq:`OF : FA > 2339\frac{1}{4} : 153`
     - :eq:`AF : FB < 1007 : 66`, :eq:`AB : BF < 1009\frac{1}{6} : 66`
   * - Bisection 4
     - 96-gon (:eq:`1^\circ 52' 30''`)
     - :eq:`OA : AG > 4673\frac{1}{2} : 153 \implies P_{96}^{\text{circ}} : AB < 3\frac{1}{7}`
     - :eq:`AG : GB < 2016\frac{1}{6} : 66`, :eq:`AB : BG < 2017\frac{1}{4} : 66 \implies P_{96}^{\text{insc}} : AB > 3\frac{10}{71}`
