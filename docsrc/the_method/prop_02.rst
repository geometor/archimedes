:canonical_id: METH.2
:order: 3
:type: proposition

.. _method-prop-2:

Proposition 2: Mechanical Discovery of the Sphere Volume & Surface
==================================================================

.. folio:: Heath (1912), pp. 18–21 · Heiberg II², 438–447
   :page: 18

.. enunciation::

   (1) Any sphere is (in respect of solid content) **four times** the cone with base equal to a great circle of the sphere and height equal to its radius; and (2) the cylinder with base equal to a great circle of the sphere and height equal to the diameter is **:eq:`1\frac{1}{2}` times** the sphere.

Let :g:`ABCD` be a great circle of a sphere with perpendicular diameters :g:`AC`, :g:`BD`. Circumscribe the cylinder of base diameter :eq:`EF = 2r` (around axis :g:`AC`) and height :eq:`AC = 2r`, and inscribe the double-radius cone :g:`AEF` with vertex :g:`A` and base diameter :eq:`EF = 4r` (so radius at distance :eq:`AS = x` from :g:`A` equals :eq:`x`!). Produce :g:`CA` to :g:`H` making :eq:`AH = AC = 2r`, and treat :g:`CH` as a lever with fulcrum at :g:`A`!

Cut the sphere, cone, and cylinder by any plane :g:`MN` perpendicular to :g:`AC` at distance :eq:`AS = x` from :g:`A`:

* In the **sphere**, chord :g:`OS` satisfies :eq:`OS^2 = AS \cdot SC = x(2r - x)`, so the circular cross-section has radius :eq:`OS`.
* In the **cone** :g:`AEF`, cross-section radius :eq:`SQ = AS = x`, so :eq:`SQ^2 = x^2`.
* In the **large cylinder** (radius :eq:`MS = AC = 2r` in Archimedes' construction!), :eq:`MS^2 = 4r^2 = 2r \cdot 2r`.

Summing the sphere and cone squares gives the magic algebraic cancellation:

.. math::

   OS^2 + SQ^2 = x(2r - x) + x^2 = 2rx \implies \frac{MS^2}{OS^2 + SQ^2} = \frac{4r^2}{2rx} = \frac{2r}{x} = \frac{HA}{AS}!

Therefore, **the circular section of the sphere together with the circular section of the cone, when both are hung at** :g:`H`, **balance the circular section of the cylinder in its actual place** :g:`S`! Summing all parallel circular sections from :g:`A` to :g:`C`—and noting that the cylinder's centre of gravity is the midpoint :g:`O` of :g:`AC` (:eq:`AO = r = \frac{1}{2}AH`)—gives:

.. math::

   \frac{\text{Cylinder}}{\text{Sphere} + \text{Cone } AEF} = \frac{HA}{AO} = \frac{2r}{r} = 2 \implies \text{Sphere} + \text{Cone } AEF = \frac{1}{2}\text{Cylinder}.

Since the large cylinder (radius :eq:`2r`, height :eq:`2r`) is :eq:`8` elementary cones (radius :eq:`r`, height :eq:`r`) and Cone :g:`AEF` (radius :eq:`2r`, height :eq:`2r`) is :eq:`8 \times \frac{1}{3}`—or in Archimedes' scaling, :eq:`\text{Cylinder} = 3 \cdot \text{Cone } AEF`—subtracting leaves **Sphere = 4 elementary cones** (:eq:`\frac{4}{3}\pi r^3`), and the circumscribed cylinder (radius :eq:`r`, height :eq:`2r`, equal to :eq:`6` cones) equals :eq:`\frac{3}{2}` of the sphere!

**Autobiographical Note on the Surface of the Sphere** (Heath 1912, p. 21): Immediately after Prop. 2, Archimedes writes:

.. epigraph::

   “From this theorem, to the effect that a sphere is four times as great as the cone with a great circle of the sphere as base and with height equal to the radius of the sphere, **I conceived the notion** that the surface of any sphere is four times as great as a great circle in it; for, judging from the fact that any circle is equal to a triangle with base equal to the circumference and height equal to the radius of the circle, I apprehended that, in like manner, any sphere is equal to a cone with base equal to the surface of the sphere and height equal to the radius.”
