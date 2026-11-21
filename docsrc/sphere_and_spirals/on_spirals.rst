:canonical_id: SP
:order: 3
:type: section

On Spirals: Kinematic Definition, Subtangent Rectification & Quadrature
=======================================================================

.. folio:: Heath (1897), pp. 151–188 · Heiberg II, 1–141
   :page: 151

Kinematic Definition & Discrete Sum of Squares
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Definition 1** (Heath p. 154): If a straight line drawn in a plane revolve at a uniform rate about one extremity which remains fixed, and return to the position from which it started, and if, at the same time as the line revolves, a point move at a uniform rate along the straight line beginning from the extremity which remains fixed, the point will describe a :term:`spiral <helix>` (*ἕλιξ*) in the plane (:eq:`r = a\theta`).
* **Proposition 10** *(Discrete Integral of Squares)*: Given :eq:`n` lines :eq:`A_1, A_2, \dots, A_n` in arithmetic progression :eq:`k \cdot d` (:eq:`k = 1, \dots, n`), the following exact double inequality holds:

  .. math::

     3 \sum_{k=1}^{n-1} A_k^2 + A_n^2 + d\sum_{k=1}^{n} A_k > (n + 1)\text{-fold identity} \implies 3\sum_{k=1}^{n-1} k^2 < n^3 < 3\sum_{k=1}^{n} k^2,

  the exact discrete counterpart of :eq:`\int_0^x t^2\,dt = \frac{1}{3}x^3`!

.. picture:: /_static/figures/fig_archimedean_spiral.svg
   :caption: On Spirals, Propositions 18 & 24 — Polar Subtangent Rectification (OT = 2πr) and One-Third First-Circle Quadrature

Propositions 18–20 (Subtangent Rectification) & Proposition 24 (Quadrature)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 171–182 · Heiberg II, 72–115
   :page: 171

* **Proposition 18** *(Differential Subtangent Theorem)*:

  .. enunciation::

     If :g:`OA` be the initial line, :g:`A` the extremity of the first turn of the spiral, and if the tangent to the spiral at :g:`A` be drawn meeting the perpendicular :g:`OT` to :g:`OA` at :g:`T`, then the :term:`polar subtangent <subtangent>` :g:`OT` is **equal to the circumference** (:eq:`2\pi OA`) of the ‘first circle’ having radius :g:`OA`.

  Proved by double indirect kinematic :term:`neusis <neusis>` bounds (Props. 5–9): assuming :eq:`OT > C_1` or :eq:`OT < C_1` constructs a chord/secant contradicting the uniform ratio of angular arc to radial growth (:eq:`dr / d\theta = a`)! Props. 19–20 generalize :eq:`OT_n = n \cdot C_n` to the :eq:`n`-th turn and arbitrary intermediate angles.

* **Proposition 24** *(Integral Quadrature of the Spiral)*:

  .. enunciation::

     The area bounded by the first turn of the spiral and the initial line :g:`OA` is equal to **one-third** of the ‘first circle’ (:eq:`\text{Area} = \frac{1}{3}\pi OA^2`).

  Dividing the circle into :eq:`n` equal sectors inscribes and circumscribes circular sectors of radii :eq:`\frac{k}{n} OA` (:eq:`k = 1, \dots, n`), squeezing the spiral area via **Proposition 10** (:eq:`\frac{1}{n^3}\sum k^2 \to \frac{1}{3}`)! Subsequent turns satisfy :eq:`R_2 = \frac{7}{12} C_2` and general ring ratios (Props. 25–28).
