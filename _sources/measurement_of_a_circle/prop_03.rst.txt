:canonical_id: DC.3
:order: 3
:type: proposition

.. _mc-prop-3:

Proposition 3: Circumference-to-Diameter Bounds (3 10/71 < π < 3 1/7)
=====================================================================

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
