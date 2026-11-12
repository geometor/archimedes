:order: 60
:type: chapter
:canonical_id: method-of-mechanical-theorems
:folio: Heath 1912, pp. 12–51 · Heiberg 1907 / Vol. II (2nd ed.), pp. 426–507

.. _unit-method-of-mechanical-theorems-en:

The Method of Mechanical Theorems (*Ἔφοδος*)
============================================

.. rubric:: *Περὶ τῶν μηχανικῶν θεωρημάτων πρὸς Ἐρατοσθένην ἔφοδος* — :person:`Archimedes <archimedes>`, deciphered by :person:`J. L. Heiberg <heiberg>` (1906/1907), ed. & trans. :person:`T. L. Heath <heath>` (:cite:`heath:1912`, pp. 12–51)

.. note::

   **Edition Track (English)**: Public-domain Cambridge Supplement translation (:cite:`heath:1912`, pp. 12–51; :cite:`archimedes:methodus`), verified page-by-page against 300 DPI scans of Heath (1912) and collated with :person:`Heiberg's <heiberg>` Palimpsest edition (:cite:`heiberg:1907`). Switch tracks above for the **Summary** or **Notes**.

Prefatory Letter to Eratosthenes: Discovery (*Ἔνδειξις*) vs. Proof (*Ἀπόδειξις*)
--------------------------------------------------------------------------------

.. folio:: Heath (1912), pp. 12–14 · Heiberg II², 426–431
   :page: 12

“**ARCHIMEDES TO ERATOSTHENES GREETING.**

I sent you on a former occasion some of the theorems discovered by me, merely writing out the enunciations and inviting you to discover the proofs, which at the moment I did not give. The enunciations of the theorems which I sent were as follows:

1. If in a right prism with a parallelogrammic base a cylinder be inscribed which has its bases in the opposite parallelograms, and its sides [generating lines] on the remaining planes (faces) of the prism, and if through the centre of the circle which is the base of the cylinder and (through) one side of the square in the plane opposite to it a plane be drawn, the plane so drawn will cut off from the cylinder a segment (:term:`cylindrical ungula <ungula>`) which is bounded by two planes and the surface of the cylinder... and the segment cut off from the cylinder is **one-sixth part of the whole prism**.
2. If in a cube a cylinder be inscribed which has its bases in the opposite parallelograms and touches with its surface the remaining four planes (faces), and if there also be inscribed in the same cube another cylinder which has its bases in other parallelograms and touches with its surface the remaining four planes (faces), then the figure bounded by the surfaces of the cylinders, which is within both cylinders (:term:`bicylinder <bicylinder>`), is **two-thirds of the whole cube**.”

Seeing that :person:`Eratosthenes <eratosthenes>` is an earnest scholar of philosophy and mathematics, :person:`Archimedes <archimedes>` sets forth in this book the **peculiar mechanical method** (:term:`ἔφοδος <ephodion>`) whereby one can investigate geometric problems via mechanics:

.. epigraph::

   “For certain things first became clear to me by a mechanical method, although they had to be demonstrated by geometry afterwards because their investigation by the said method did not furnish an actual demonstration. But it is of course easier, when we have previously acquired, by the method, some knowledge of the questions, to supply the proof than it is to find it without any previous knowledge. This is a reason why, in the case of the theorems that the cone is a third part of the cylinder, and the pyramid of the prism, of which :person:`Eudoxus <eudoxus>` was the first to discover the proof, no small share of the credit should be given to :person:`Democritus <democritus>`, who was the first to make the assertion with regard to the said figures, though he did not prove it.”

Lemmas 1–11 (pp. 14–15)
~~~~~~~~~~~~~~~~~~~~~~~

Archimedes opens by summarizing 11 statical and geometric lemmas from *Equilibrium of Planes* and *Conoids and Spheroids* (including the centroids of lines, triangles, cones—at :eq:`\frac{3}{4}` of the axis from the vertex, Lemma 10!—and cylinders), before unveiling his slice-balancing investigations.

----

.. _method-prop-1:

Proposition 1: Heuristic Slice Quadrature of the Parabola
---------------------------------------------------------

.. folio:: Heath (1912), pp. 15–18 · Heiberg II², 434–439
   :page: 15

.. enunciation::

   Let :g:`ABC` be a :term:`segment of a parabola <tmema-paraboles>` bounded by the straight line :g:`AC` and the parabola :g:`ABC`. Bisect :g:`AC` at :g:`D`, draw :g:`DBE` parallel to the diameter, and join :g:`AB`, :g:`BC`. Then shall the segment :g:`ABC` be :eq:`\frac{4}{3}` of the triangle :g:`ABC`.

.. picture:: /_static/figures/fig_method_lever.svg
   :caption: The Method, Propositions 1 & 2 — Virtual Lever Slice Balance for the Parabola and Sphere + Cone vs. Cylinder

Draw :g:`AF` parallel to :g:`DBE`, and let the tangent to the parabola at :g:`C` meet :g:`DBE` in :g:`E` and :g:`AF` in :g:`F`. Produce :g:`CB` to meet :g:`AF` in :g:`K`, and again produce :g:`CK` to :g:`H`, making :eq:`KH = KC`. Conceive :g:`CH` as a **lever** with fulcrum at its midpoint :g:`K`!

Through any point :g:`O` on :g:`AC`, draw :g:`MO` parallel to :g:`DBE` meeting :g:`CK` at :g:`N`, the parabola at :g:`O`, and the tangent :g:`CF` at :g:`G` (actually :g:`MO` meets :g:`AC` at :g:`M`, parabola at :g:`O`, :g:`CK` at :g:`N`, and :g:`CF` at :g:`P`). By conic properties of the parabola, :eq:`MO : OP = CA : AO = CK : KN = HK : KN`.

Now transport the parabolic chord :g:`MO` so that its midpoint hangs from the extremity :g:`H` of the lever, while leaving the full triangle-chord :g:`OP` *in situ* with its midpoint at :g:`N`! By the :term:`Law of the Lever <antipeponthos>` (:just:`Equil. I. 6–7`), since :eq:`HK : KN = OP : MO`, **each chord** :g:`MO` **placed at** :g:`H` **balances the corresponding chord** :g:`OP` **of** :g:`\triangle CFA` **in its actual place** :g:`N`!

Because the parabolic segment :g:`ABC` is *made up of* (*συνεστηκός*) all the parallel chords :g:`MO`, and :g:`\triangle CFA` is *made up of* all the parallel chords :g:`OP`, the whole parabolic segment hung at :g:`H` balances :g:`\triangle CFA` in its actual position! Now the :term:`centre of gravity <kentron-barous>` :g:`W` of :g:`\triangle CFA` lies on median :g:`CK` with :eq:`CK = 3 \cdot KW` (:just:`Equil. I. 14`). Hence:

.. math::

   \triangle CFA : \text{Segment } ABC = HK : KW = CK : \frac{1}{3}CK = 3 : 1 \implies \text{Segment } ABC = \frac{1}{3}\triangle CFA = \frac{4}{3}\triangle ABC.

Archimedes immediately adds his celebrated methodological caveat (Heath 1912, p. 18): *"Now the fact here stated is not actually demonstrated by the argument used; but that argument has given a sort of **indication** (ἔνδειξις) that the conclusion is true. Seeing then that the theorem is not demonstrated, but at the same time suspecting that the conclusion is true, we shall have recourse to the geometrical demonstration which I myself discovered and have already published."*

----

.. _method-prop-2:

Proposition 2: Mechanical Discovery of the Sphere Volume & Surface
------------------------------------------------------------------

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

----

Propositions 3–15: Conoids, Centroids, the Ungula & the Bicylinder
------------------------------------------------------------------

.. folio:: Heath (1912), pp. 21–51 · Heiberg II², 446–507
   :page: 21

* **Propositions 3–11** (pp. 21–38): Apply the identical slice-lever engine to discover the volumes of :term:`spheroids <sphairoeides>` (Prop. 3), :term:`paraboloids <orthogonion-konoeides>` (Prop. 4), centroids of paraboloid segments (:eq:`2 : 1` along the axis, Prop. 5!), centroids of hemispheres (:eq:`5 : 3` from pole to centre, i.e. :eq:`\frac{3}{8}r` from the base, Prop. 6!), spherical segments (Props. 7, 9), spheroid segments (Props. 8, 10), and :term:`hyperboloid <amblygonion-konoeides>` segments & centroids (Prop. 11).
* **Propositions 12–14: The Cylindrical Ungula** (pp. 38–48): First promised in the Preface to :person:`Eratosthenes <eratosthenes>`, Archimedes proves **three times**—first mechanically by balancing vertical rectangular slices against a prism (Props. 12–13), then geometrically via parabolic triangles and exhaustion by inscribed/circumscribed prism elements (Prop. 14)—that the :term:`cylindrical ungula <ungula>` cut from a right cylinder in a square-based prism equals **one-sixth of the whole prism** (:eq:`V = \frac{2}{3}r^2 h`), a curved solid equal to a purely rectilinear fraction of its bounding box without :eq:`\pi`!
* **Proposition 15: The Archimedean Bicylinder** (pp. 48–51): Slicing two orthogonal intersecting cylinders inscribed in a cube of edge :eq:`2r` by planes parallel to both axes produces **square cross-sections** of area :eq:`4(r^2 - x^2)`—identical in ratio at every height :eq:`x` to the circular cross-sections :eq:`\pi(r^2 - x^2)` of the inscribed sphere! Hence the :term:`bicylinder <bicylinder>` bears to the **cube** (:eq:`8r^3`) the exact ratio that the **sphere** bears to its circumscribed cylinder (:eq:`\frac{2}{3}`), proving that the bicylinder equals **two-thirds of the cube** (:eq:`V = \frac{16}{3}r^3`).

.. qed::
