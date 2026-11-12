:order: 40
:type: chapter
:canonical_id: sphere-spirals-conoids
:folio: Heath 1897, pp. 1–90, 99–188 · Heiberg I, 1–255, 272–499 & II, 1–141

.. _unit-sphere-spirals-conoids-en:

Sphere and Cylinder, On Spirals & Conoids and Spheroids
=======================================================

.. rubric:: *De Sphaera et Cylindro* I–II · *De Lineis Spiralibus* · *De Conoidibus et Sphaeroidibus* — :person:`Archimedes <archimedes>` (:cite:`heath:1897`, pp. 1–90, 99–188; :cite:`heiberg:1880`, :cite:`heiberg:1881`)

.. note::

   **Edition Track (English)**: Synthesizes the three grand Dositheus treatises of curved surface area, solid cubature, and kinematic curves from :cite:`heath:1897`, verified against 300 DPI scans of Heath (1897) and collated with :person:`Heiberg's <heiberg>` Teubner text and :person:`Eutocius's <eutocius>` commentary (:cite:`eutocius:in-archimedem`). Switch tracks above for the **Summary** or **Notes**.

Part I — *On the Sphere and Cylinder*, Books I & II
---------------------------------------------------

.. folio:: Heath (1897), pp. 1–56 · Heiberg I, 1–187
   :page: 1

Definitions & Five Convexity / Continuity Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Addressing :person:`Dositheus <dositheus>` after mourning :person:`Conon <conon>` (:cite:`archimedes:sphere-and-cylinder`), :person:`Archimedes <archimedes>` defines lines and surfaces :term:`concave in the same direction <concave-same-way>` (*ἐπὶ τὰ αὐτὰ κοῖλα*, Defs. 2 & 4)—meaning that the straight segment joining any two points on the curve or surface falls either wholly on the same side of, or upon, the curve or surface—and lays down **five foundational Assumptions (Λαμβανόμενα)** (Heath pp. 3–4):

1. **Assumption 1**: *Of all lines which have the same extremities, the straight line is the least.* (Explicitly cited by :person:`Proclus <proclus>`, :cite:`proclus:in-euclidem`, Friedlein p. 110.)
2. **Assumption 2**: Of other plane lines having the same extremities and :term:`concave in the same direction <concave-same-way>`, when one is wholly included between the other and the straight line having the same extremities (or partially coincides), **that which is included is the lesser**.
3. **Assumption 3**: Similarly, of surfaces having the same plane extremities, **the plane is the least** in area.
4. **Assumption 4**: Of other surfaces having the same plane extremities and concave in the same direction, when one is wholly included by the other, **the included surface is the lesser**.
5. **Assumption 5** (:term:`Archimedes' Lemma <archimedes-lemma>`): *Further, of unequal lines, unequal surfaces, and unequal solids, the greater exceeds the less by such a magnitude as, when added to itself, can be made to exceed any assigned magnitude among those which are comparable with one another.*

Book I, Propositions 33 & 34: Surface, Volume & the :eq:`2 : 3` Tomb Theorem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 39–44 · Heiberg I, 134–149
   :page: 39

Inscribing and circumscribing regular :eq:`4n`-gons to a great circle of the sphere and revolving them about a diameter generates solids bounded by conical frusta whose lateral areas sum (via Props. 21–32) to :eq:`4` times a circle of radius approaching :eq:`r`. Double :term:`exhaustion <exhaustion>` yields the two crowning theorems of Book I:

.. enunciation::

   **Proposition 33.** *The surface of any sphere is equal to four times its greatest circle* (:eq:`S = 4\pi r^2`).

.. enunciation::

   **Proposition 34.** *Any sphere is equal to four times the cone which has its base equal to the greatest circle in the sphere and its height equal to the radius of the sphere* (:eq:`V = 4 \cdot \frac{1}{3}\pi r^2 \cdot r = \frac{4}{3}\pi r^3`).

   **Corollary (The Tomb Engraving).** *From what has been proved it follows that every cylinder whose base is the greatest circle in a sphere and whose height is equal to the diameter of the sphere is* **once and a half** (:eq:`\frac{3}{2}`) *as great as the sphere, and its surface together with its bases is likewise* **once and a half** (:eq:`\frac{3}{2}`) *the surface of the sphere.*

.. picture:: /_static/figures/fig_sphere_cylinder.svg
   :caption: Archimedes' Tomb Theorem (Sphere & Cylinder I.34 Cor.) — Cone : Sphere : Cylinder = 1 : 2 : 3

In Props. 42–43, Archimedes further proves that the curved surface of **any spherical segment** (less than or greater than a hemisphere) equals the circle whose radius is the straight line drawn from the vertex of the segment to the circumference of its base circle!

Book II, Propositions 2 & 4: Spherical Segments & Eutocius's Cubic Intersection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 59–79 · Heiberg I, 194–225 & III, 130–177
   :page: 59

* **Book II, Proposition 2** (:cite:`archimedes:sphere-and-cylinder:ii-2`): Every spherical segment of height :eq:`h` in a sphere of radius :eq:`r` equals the cone having the same base as the segment and altitude :eq:`h \cdot \frac{3r - h}{2r - h}`, whence :eq:`V_{\text{seg}} = \frac{1}{3}\pi h^2 (3r - h)`.
* **Book II, Proposition 4**: *To cut a given sphere by a plane so that the volumes of the segments have to one another a given ratio* :eq:`m : n`. Archimedes' analysis reduces the division of diameter :eq:`2r` to the **cubic proportion**:

  .. math::

     (a - x) : b = c^2 : x^2, \qquad \text{i.e.} \qquad x^2(a - x) = b c^2,

  promising to append its synthesis and *diorismos* at the end. Found missing in early copies, the authentic Doric synthesis was discovered and preserved by :person:`Eutocius of Ascalon <eutocius>` (:cite:`eutocius:in-archimedem`; Heath pp. 65–79): Archimedes constructs the root :eq:`x \in (0, a)` by intersecting the **parabola** :eq:`x^2 = \frac{c^2}{k} y` with the **rectangular hyperbola** :eq:`(a - x) y = b k`, and proves the **maximum (*diorismos*)** that :eq:`x^2(a - x)` attains its unique maximum on :eq:`(0, a)` at :eq:`x = \frac{2}{3}a` (namely :eq:`\frac{4}{27}a^3`), using tangent geometry completely equivalent to setting :eq:`\frac{d}{dx}[x^2(a-x)] = 0`!

----

Part II — *On Spirals* (*Περὶ ἑλίκων*)
--------------------------------------

.. folio:: Heath (1897), pp. 151–188 · Heiberg II, 1–141
   :page: 151

Kinematic Definition & Discrete Sum of Squares
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Definition 1** (Heath p. 154): If a straight line drawn in a plane revolve at a uniform rate about one extremity which remains fixed, and return to the position from which it started, and if, at the same time as the line revolves, a point move at a uniform rate along the straight line beginning from the extremity which remains fixed, the point will describe a :term:`spiral <helix>` (*ἕλιξ*) in the plane (:eq:`r = a\theta`).
* **Proposition 10** *(Discrete Integral of Squares)*: Given :eq:`n` lines :eq:`A_1, A_2, \dots, A_n` in arithmetic progression :eq:`k \cdot d` (:eq:`k = 1, \dots, n`), Archimedes proves the exact double inequality:

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

----

Part III — *On Conoids and Spheroids* (*Περὶ κωνοειδέων καὶ σφαιροειδέων*)
--------------------------------------------------------------------------

.. folio:: Heath (1897), pp. 99–150 · Heiberg I, 272–499
   :page: 99

In 32 propositions (:cite:`archimedes:conoids-and-spheroids`), Archimedes extends exhaustion by inscribed and circumscribed cylinder-slices ("gnomons" of equal thickness) to affine-scaled quadric surfaces of revolution:

* **Proposition 4** *(Area of the Ellipse)*: The area of any ellipse with semi-axes :eq:`a, b` bears to the circle on its major axis :eq:`2a` the ratio :eq:`b : a` (and equals the circle whose radius is the geometric mean :eq:`\sqrt{ab}`, i.e. :eq:`\text{Area} = \pi ab`).
* **Propositions 21 & 22** (:term:`Right-Angled Conoid / Paraboloid <orthogonion-konoeides>`): Any segment cut from a paraboloid of revolution by a plane (perpendicular or oblique to the axis!) is **once and a half** (:eq:`\frac{3}{2}`) of the cone having the same base and the same axis (hence **one-half** of the enveloping cylinder, since ordinates-squared grow linearly :eq:`y^2 \propto x` and :eq:`\sum_{k=1}^n k \sim \frac{1}{2}n^2`).
* **Propositions 25 & 26** (:term:`Obtuse-Angled Conoid / Hyperboloid <amblygonion-konoeides>`): Any segment of a hyperboloid of revolution bears to the cone on the same base and axis the exact ratio :eq:`(AD + 3a) : (AD + 2a)`, where :eq:`AD` is the segment axis and :eq:`2a` the transverse diameter.
* **Propositions 27–32** (:term:`Prolate & Oblate Spheroids <sphairoeides>`): Half of any spheroid cut through the centre equals **twice** the inscribed cone on the same base and axis (:eq:`V = \frac{4}{3}\pi a b^2`), and any general segment of axis :eq:`h` out of total diameter :eq:`2a` bears to its inscribed cone the ratio :eq:`(3a - h) : (2a - h)`—generalizing *Sphere and Cylinder* II.2 to arbitrary ellipsoids of revolution!

.. qed::
