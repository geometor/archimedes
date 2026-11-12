:order: 10
:type: chapter
:canonical_id: measurement-of-a-circle
:folio: Heath 1897, pp. 91–98 · Heiberg I, 258–271

.. _unit-measurement-of-a-circle-en:

Measurement of a Circle (*Κύκλου μέτρησις*)
===========================================

.. rubric:: *Dimensio Circuli* — :person:`Archimedes of Syracuse <archimedes>` (ed. :person:`T. L. Heath <heath>`, 1897, pp. 91–98; :person:`J. L. Heiberg <heiberg>`, Vol. I, pp. 258–271)

.. note::

   **Edition Track (English)**: Public-domain translation from :cite:`heath:1897` (pp. 91–98), verified page-by-page against 300 DPI scans of Heath (1897) and collated with :person:`Heiberg's <heiberg>` critical Greek text (:cite:`heiberg:1880`, Vol. I, pp. 258–271) and :person:`Eutocius's <eutocius>` arithmetic commentary (:cite:`eutocius:in-archimedem`). Switch tracks above for the **Summary** or **Notes**.

.. _mc-prop-1:

Proposition 1
-------------

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

----

.. _mc-prop-2:

Proposition 2
-------------

.. folio:: Heath (1897), p. 93 · Heiberg I, 260–263
   :page: 93

.. enunciation::

   The area of a circle is to the square on its diameter as :eq:`11` to :eq:`14`.

Let :g:`AB` be the diameter of a circle, and let :g:`CGFE` be a circumscribed square. Produce side :g:`FG` so that :eq:`DE = 2 \cdot CD` and :eq:`EF = \frac{1}{7} CD`. Join :g:`AC`, :g:`AD`, :g:`AF`.

Since :eq:`\triangle ACG : \triangle ACD = 1 : 2` and :eq:`\triangle ACG : \triangle AEF = 7 : 1` (:just:`Eucl. VI. 1`), the whole triangle :g:`ACF` is to :g:`\triangle ACG` as :eq:`22 : 7`. Now the circumscribed square :g:`CGFE` is :eq:`4 \cdot \triangle ACG`, so :eq:`\triangle ACF : AB^2 = 22 : 28 = 11 : 14`. Because :eq:`CF = 3\frac{1}{7} AB` approximates the circumference (established in :ref:`Proposition 3 <mc-prop-3>`) and :g:`AC` equals the radius, :g:`\triangle ACF` equals the circle by :ref:`Proposition 1 <mc-prop-1>`. Hence the circle bears to the square on its diameter the approximate ratio :eq:`11 : 14`.

.. qed::

----

.. _mc-prop-3:

Proposition 3
-------------

.. folio:: Heath (1897), pp. 93–98 · Heiberg I, 262–271
   :page: 93

.. enunciation::

   The ratio of the circumference of any circle to its diameter is less than :eq:`3\frac{1}{7}` but greater than :eq:`3\frac{10}{71}`.

I. Proof of the Upper Bound (:eq:`\pi < 3\frac{1}{7}`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 93–96 · Heiberg I, 262–267
   :page: 94

Let :g:`AB` be the diameter of any circle, :g:`O` its centre, :g:`AC` the tangent at :g:`A`; and let the angle :g:`AOC` be one-third of a right angle (:eq:`30^\circ`). Then:

* :eq:`OA : AC = \sqrt{3} : 1 > 265 : 153`, and :eq:`OC : CA = 2 : 1 = 306 : 153`.

1. **First Bisection (12-gon)**: Draw :g:`OD` bisecting :g:`\angle AOC`. By the angle-bisector theorem (:just:`Eucl. VI. 3`), :eq:`CO : OA = CD : DA`, so :eq:`(CO + OA) : OA = CA : DA`, or :eq:`(CO + OA) : CA = OA : AD`. Hence:

   .. math::

      OA : AD > 571 : 153, \qquad OD^2 : AD^2 > (571^2 + 153^2) : 153^2 = 349450 : 23409,

   whence (:just:`Eucl. I. 47`) :eq:`OD : DA > 591\frac{1}{8} : 153`.

2. **Second Bisection (24-gon)**: Let :g:`OE` bisect :g:`\angle AOD`. By the same composition of ratios:

   .. math::

      OA : AE > 1162\frac{1}{8} : 153, \qquad OE : EA > 1172\frac{1}{8} : 153.

3. **Third Bisection (48-gon)**: Let :g:`OF` bisect :g:`\angle AOE`. Then:

   .. math::

      OA : AF > 2334\frac{1}{4} : 153, \qquad OF : FA > 2339\frac{1}{4} : 153.

4. **Fourth Bisection (96-gon)**: Let :g:`OG` bisect :g:`\angle AOF`. Then:

   .. math::

      OA : AG > 4673\frac{1}{2} : 153.

Since :g:`\angle AOC`, which is one-third of a right angle, has been bisected four times, :g:`\angle AOG` is :eq:`\frac{1}{48}` of a right angle. Make :g:`\angle AOH = \angle AOG` on the opposite side of :g:`OA`; then :g:`\angle GOH` is :eq:`\frac{1}{24}` of a right angle, so :g:`GH` is one side of a regular polygon of **96 sides** circumscribed to the circle. Since :eq:`AB = 2 \cdot OA` and :eq:`GH = 2 \cdot AG`, the ratio of the diameter to the perimeter of the circumscribed 96-gon satisfies:

.. math::

   AB : P_{96}^{\text{circ}} > 4673\frac{1}{2} : (96 \times 153) = 4673\frac{1}{2} : 14688.

Now :eq:`\frac{14688}{4673\frac{1}{2}} = 3 + \frac{667\frac{1}{2}}{4673\frac{1}{2}} < 3 + \frac{667\frac{1}{2}}{4672\frac{1}{2}} = 3\frac{1}{7}`. A fortiori, the circumference of the circle—being strictly less than :eq:`P_{96}^{\text{circ}}`—is less than :eq:`3\frac{1}{7}` times the diameter.

II. Proof of the Lower Bound (:eq:`\pi > 3\frac{10}{71}`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 96–98 · Heiberg I, 266–271
   :page: 96

Next let :g:`AB` be the diameter of a circle, and let :g:`AC`, meeting the circle in :g:`C`, make the angle :g:`CAB` equal to one-third of a right angle (:eq:`30^\circ`). Join :g:`BC`; then :g:`\angle ACB` in the semicircle is right (:just:`Eucl. III. 31`), and:

* :eq:`AC : CB = \sqrt{3} : 1 < 1351 : 780`, while :eq:`AB : BC = 2 : 1 = 1560 : 780`.

1. **First Bisection (12-gon)**: Let :g:`AD` bisect :g:`\angle CAB`, meeting :g:`BC` in :g:`d` and the circle in :g:`D`. Join :g:`BD`. By similar right triangles :g:`\triangle ADB \sim \triangle ACd \sim \triangle BdD` (:just:`Eucl. III. 21`, :just:`Eucl. VI. 3`):

   .. math::

      AD : DB = (AB + AC) : BC < 2911 : 780, \qquad AB : BD < 3013\frac{3}{4} : 780.

2. **Second Bisection (24-gon)**: Let :g:`AE` bisect :g:`\angle DAB`, meeting the circle in :g:`E`. Reducing by the factor :eq:`\frac{4}{13}` after composition:

   .. math::

      AE : EB < 5924\frac{3}{4} : 780 = 1823 : 240, \qquad AB : BE < 1838\frac{9}{11} : 240.

3. **Third Bisection (48-gon)**: Let :g:`AF` bisect :g:`\angle EAB`, meeting the circle in :g:`F`. Reducing by the factor :eq:`\frac{11}{40}`:

   .. math::

      AF : FB < 3661\frac{9}{11} : 240 = 1007 : 66, \qquad AB : BF < 1009\frac{1}{6} : 66.

4. **Fourth Bisection (96-gon)**: Let :g:`AG` bisect :g:`\angle FAB`, meeting the circle in :g:`G`. Then:

   .. math::

      AG : GB < 2016\frac{1}{6} : 66, \qquad AB : BG < 2017\frac{1}{4} : 66.

Inverting, the side :g:`BG` of the inscribed regular **96-gon** bears to the diameter :g:`AB` a ratio greater than :eq:`66 : 2017\frac{1}{4}`. Hence the perimeter of the inscribed 96-gon satisfies:

.. math::

   P_{96}^{\text{insc}} : AB > (96 \times 66) : 2017\frac{1}{4} = 6336 : 2017\frac{1}{4} = 3 + \frac{284\frac{1}{4}}{2017\frac{1}{4}} > 3\frac{10}{71},

since :eq:`71 \times 284\frac{1}{4} = 20181\frac{3}{4} > 20172\frac{1}{2} = 10 \times 2017\frac{1}{4}`. A fortiori, the circumference of the circle—being strictly greater than :eq:`P_{96}^{\text{insc}}`—is greater than :eq:`3\frac{10}{71}` times the diameter.

Thus the ratio of the circumference to the diameter is less than :eq:`3\frac{1}{7}` and greater than :eq:`3\frac{10}{71}`.

.. qed::
