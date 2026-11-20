:canonical_id: QP.24
:order: 25
:type: proposition

Proposition 24: Pure Geometric Quadrature of the Parabola (4/3 ΔABC)
====================================================================

.. folio:: Heath (1897), pp. 246–252 · Heiberg II, 336–353
   :page: 251

.. enunciation::

   **Proposition 24 (Geometric Quadrature of the Parabola).** Every segment bounded by a parabola and a chord :g:`AC` is equal to four-thirds of the triangle :g:`△ABC` which has the same base as the segment and equal height.

.. picture:: /_static/figures/fig_parabola_exhaustion.svg
   :caption: Propositions 18–24 — Recursive Geometric Exhaustion of Parabolic Segment ABC (Area = 4/3 Triangle ABC)

Let :eq:`K = \frac{4}{3}\triangle ABC`.

1. *Suppose the segment greater than* :g:`K`: Inscribe triangles recursively until the remaining parabolic segments leave a sum less than :eq:`\text{Segment} - K` (:just:`Prop. 20`, :just:`Eucl. X. 1`). Then the inscribed polygon :eq:`A + B + \dots + Z > K = \frac{4}{3}A`, contradicting :just:`Prop. 23` (:eq:`A + B + \dots + Z = \frac{4}{3}A - \frac{1}{3}Z < \frac{4}{3}A`)!
2. *Suppose the segment less than* :g:`K`: Let :eq:`A = \triangle ABC`, :eq:`B = \frac{1}{4}A`, ..., continuing until the last term :g:`Z` is less than :eq:`K - \text{Segment}`. By :just:`Prop. 23`, :eq:`K - (A + B + \dots + Z) = \frac{1}{3}Z < Z < K - \text{Segment}`, whence :eq:`A + B + \dots + Z > \text{Segment}`, contradicting :just:`Prop. 22`!

Therefore the parabolic segment is neither greater nor less than :eq:`K = \frac{4}{3}\triangle ABC`; it is strictly equal to :eq:`\frac{4}{3}\triangle ABC`.

.. qed::
