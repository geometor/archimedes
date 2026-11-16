:canonical_id: QP.18-24
:order: 3
:type: section

Part II: Pure Geometric Exhaustion (Propositions 18–24)
=======================================================

.. folio:: Heath (1897), pp. 246–252 · Heiberg II, 336–353
   :page: 246

.. picture:: /_static/figures/fig_parabola_exhaustion.svg
   :caption: Propositions 18–24 — Recursive Geometric Exhaustion of Parabolic Segment ABC (Area = 4/3 Triangle ABC)

To demonstrate the theorem purely geometrically without mechanical postulates, Archimedes defines the *base* :g:`AC`, *vertex* :g:`B` (point of maximum perpendicular height, where the tangent is parallel to :g:`AC`), and *height* of any segment:

* **Propositions 18–19**: If diameters through the midpoints :g:`F`, :g:`G` of :g:`AD` (half-chord) meet the parabola at secondary vertices :g:`D`, :g:`E`, then :eq:`BM = \frac{4}{3} DN` (actually :eq:`BV = 4 \cdot DF` measured from the chord, so the sub-segment height is :eq:`\frac{1}{4}` of the main height measured along the diameter!).
* **Proposition 20**: If :g:`ABC` be a parabolic segment with vertex :g:`B`, then :g:`\triangle ABC` is **greater than half** the area of the segment :g:`ABC` (since :g:`\triangle ABC` is half of the circumscribed parallelogram formed by the tangent at :g:`B` and diameters through :g:`A`, :g:`C`). Repeated inscription therefore exhausts the segment by :just:`Eucl. X. 1`!
* **Proposition 21**: If :g:`D`, :g:`E` be the vertices of the two remaining segments on :g:`AB` and :g:`BC`, then:

  .. math::

     \triangle ABC = 8 \cdot \triangle ADB = 8 \cdot \triangle BEC, \qquad \text{whence} \qquad \triangle ADB + \triangle BEC = \frac{1}{4} \triangle ABC.

* **Proposition 22**: For any finite sequence of areas :g:`A, B, C, D, \dots` formed at successive stages of this bisection, their sum :eq:`A + B + C + \dots` is strictly **less** than the area of the parabolic segment.
* **Proposition 23** *(Exact Finite Geometric Series Identity)*:

  .. enunciation::

     Given a series of areas :g:`A, B, C, D, \dots, Z`, of which :g:`A` is the greatest, and each is equal to four times the next in order, then:

     .. math::

        A + B + C + D + \dots + Z + \frac{1}{3} Z = \frac{4}{3} A.

  *Proof*: Add :eq:`b = \frac{1}{3}B`, :eq:`c = \frac{1}{3}C`, ..., :eq:`z = \frac{1}{3}Z`. Since :eq:`B + b = \frac{4}{3}B = \frac{1}{3}A`, :eq:`C + c = \frac{1}{3}B`, ..., :eq:`Z + z = \frac{1}{3}Y`, summing all terms gives :eq:`(A + B + \dots + Z) + (b + c + \dots + z) = A + \frac{1}{3}(A + B + \dots + Y)`. Subtracting :eq:`b + c + \dots + y = \frac{1}{3}(B + C + \dots + Y)` from both sides leaves :eq:`A + B + \dots + Z + \frac{1}{3}Z = A + \frac{1}{3}A = \frac{4}{3}A`!

* **Proposition 24** *(Geometric Quadrature of the Parabola)*:

  .. enunciation::

     Every segment bounded by a parabola and a chord :g:`AC` is equal to four-thirds of the triangle :g:`△ABC` which has the same base as the segment and equal height.

  Let :eq:`K = \frac{4}{3}\triangle ABC`.

  1. *Suppose the segment greater than* :g:`K`: Inscribe triangles recursively until the remaining parabolic segments leave a sum less than :eq:`\text{Segment} - K` (:just:`Prop. 20`, :just:`Eucl. X. 1`). Then the inscribed polygon :eq:`A + B + \dots + Z > K = \frac{4}{3}A`, contradicting :just:`Prop. 23` (:eq:`A + B + \dots + Z = \frac{4}{3}A - \frac{1}{3}Z < \frac{4}{3}A`)!
  2. *Suppose the segment less than* :g:`K`: Let :eq:`A = \triangle ABC`, :eq:`B = \frac{1}{4}A`, ..., continuing until the last term :g:`Z` is less than :eq:`K - \text{Segment}`. By :just:`Prop. 23`, :eq:`K - (A + B + \dots + Z) = \frac{1}{3}Z < Z < K - \text{Segment}`, whence :eq:`A + B + \dots + Z > \text{Segment}`, contradicting :just:`Prop. 22`!

  Therefore the parabolic segment is neither greater nor less than :eq:`K = \frac{4}{3}\triangle ABC`; it is strictly equal to :eq:`\frac{4}{3}\triangle ABC`.

.. qed::
