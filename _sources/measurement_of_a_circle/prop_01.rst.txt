:canonical_id: DC.1
:order: 1
:type: proposition

.. _mc-prop-1:

Proposition 1: Circle Area Equal to Right-Angled Triangle
=========================================================

.. folio:: Heath (1897), pp. 91–93 · Heiberg I, 258–261
   :page: 91

.. enunciation::

   The area of any circle is equal to a right-angled triangle in which one of the sides about the right angle is equal to the radius, and the other to the circumference, of the circle.

Let :g:`ABCD` be the given circle, and :g:`K` the triangle described, having one of the sides about the right angle equal to the radius of the circle :g:`ABCD` and the other equal to its circumference (*ἴσος ἄρα ὁ κύκλος τῷ Ε τριγώνῳ*, Heiberg I, 260).

.. picture:: /_static/figures/fig_circle_96gon.svg
   :caption: Proposition 1 & Proposition 3 — Circle Rectification and 6-to-96-gon Inscribed/Circumscribed Bisection Bounds

Then, if the circle is not equal to :g:`K`, it must be either greater or less, and we apply the double :term:`method of exhaustion <exhaustion>`:

1. **First Reductio — Suppose the circle greater than** :g:`K`:
   Inscribe a square :g:`ABCD`, bisect the arcs :g:`AB`, :g:`BC`, :g:`CD`, :g:`DA`, then bisect (if necessary) the halves, and so on continually, until the sides of the inscribed regular polygon subtend segments whose sum is less than the excess of the area of the circle over :g:`K` (:just:`Eucl. X. 1`, :just:`Eucl. XII. 2`; cf. :cite:`euclid:elements`). Thus the area of the inscribed polygon is greater than :g:`K`.

   Let :g:`AE` be any side of this polygon, and :g:`ON` the perpendicular on :g:`AE` from the centre :g:`O`. Then :g:`ON` is less than the radius of the circle, and therefore less than one of the sides about the right angle in :g:`K`. Also the perimeter of the inscribed polygon is strictly less than the circumference of the circle (:just:`Sphere & Cyl. I, Assump. 1` — :term:`concave in the same direction <concave-same-way>`), i.e. less than the other side about the right angle in :g:`K`. Therefore the area of the polygon (:eq:`\frac{1}{2} \cdot ON \cdot \text{perimeter}`) is less than :g:`K`; which is inconsistent with the hypothesis that the polygon is greater than :g:`K`.

2. **Second Reductio — Suppose the circle less than** :g:`K`:
   Circumscribe a square, and let two adjacent sides, touching the circle at :g:`E` and :g:`H`, meet in :g:`T`. Bisect the arcs between adjacent points of contact and draw tangents at the points of bisection. If :g:`A` is the middle point of the arc :g:`EH`, and :g:`FAKG` is the tangent at :g:`A`, the angle :g:`TAG` is right; therefore :eq:`TG > GA` and :eq:`TG > GH`. It follows that the triangle :g:`FTG` is greater than half the area :g:`TEAH` bounded by the tangents and the arc. Continuing this bisection (:just:`Eucl. X. 1`), we leave spaces between the circle and the circumscribed polygon whose sum is less than the excess of :g:`K` over the circle; hence the circumscribed polygon is less than :g:`K`.

   Yet the perpendicular :g:`OA` from the centre on any side equals the radius of the circle, while the perimeter of the circumscribed polygon is strictly greater than the circumference of the circle (:term:`convexity postulate <concave-same-way>`). Therefore the area of the circumscribed polygon is greater than the triangle :g:`K`; which is impossible.

Since, then, the area of the circle is neither greater nor less than :g:`K`, it is equal to it.

.. qed::
