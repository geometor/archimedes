:order: 20
:type: chapter
:canonical_id: equilibrium-of-planes
:folio: Heath 1897, pp. 189–220 · Heiberg II, 142–241

.. _unit-equilibrium-of-planes-en:

On the Equilibrium of Planes (*Ἐπιπέδων ἰσορροπιῶν αʹ βʹ*)
===========================================================

.. rubric:: *De Planorum Aequilibriis*, Books I & II — :person:`Archimedes of Syracuse <archimedes>` (ed. :person:`T. L. Heath <heath>`, 1897, pp. 189–220; :person:`J. L. Heiberg <heiberg>`, Vol. II, pp. 142–241)

.. note::

   **Edition Track (English)**: Public-domain translation from :cite:`heath:1897` (pp. 189–220), verified against 300 DPI scans of Heath (1897) and collated with :person:`Heiberg's <heiberg>` critical Syracusan Doric text (:cite:`heiberg:1881`, Vol. II, pp. 142–241). Switch tracks above for the **Summary** or **Notes**.

Book I — Axiomatic Statics, the Lever & the Triangle Centroid
-------------------------------------------------------------

.. folio:: Heath (1897), pp. 189–190 · Heiberg II, 142–145
   :page: 189

Postulates (Αἰτήματα, 1–7)
~~~~~~~~~~~~~~~~~~~~~~~~~~

“I postulate the following (*Αἰτούμεθα τάδε*):”

1. **Postulate 1**: Equal weights at equal distances are in :term:`equilibrium <isorropia>`, and equal weights at unequal distances are not in equilibrium but incline towards the weight which is at the greater distance.
2. **Postulate 2**: If, when weights at certain distances are in equilibrium, something be added to one of the weights, they are not in equilibrium, but incline towards that weight to which the addition is made.
3. **Postulate 3**: Similarly, if anything be taken away from one of the weights, they are not in equilibrium, but incline towards the weight from which nothing was taken.
4. **Postulate 4**: When equal and similar plane figures coincide with one another, their :term:`centres of gravity <kentron-barous>` likewise coincide.
5. **Postulate 5**: In figures which are unequal, yet similar, the centres of gravity will be similarly situated. By points similarly situated in relation to similar figures I mean points such that, if straight lines be drawn from them to the equal angles, they make equal angles with the homologous sides.
6. **Postulate 6**: If magnitudes at certain distances be in equilibrium, (other) magnitudes equal to them will also be in equilibrium at the same distances.
7. **Postulate 7**: In any figure whose perimeter is :term:`concave in one and the same direction <concave-same-way>`, the centre of gravity must be within the figure.

Propositions 1–5: Elementary Symmetry of the Balance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 190–192 · Heiberg II, 144–153
   :page: 190

* **Proposition 1**: Weights which balance at equal distances are equal (proved by :just:`Post. 3` and :just:`Post. 1`).
* **Proposition 2**: Unequal weights at equal distances will not balance, but will incline towards the greater weight (:just:`Post. 2`, :just:`Post. 1`).
* **Proposition 3**: Unequal weights will balance at unequal distances, the greater weight being at the lesser distance (and conversely).
* **Proposition 4**: If two equal magnitudes have not the same centre of gravity, the centre of gravity of both taken together is at the middle point of the straight line joining their centres of gravity.
* **Proposition 5** *(Corollaries 1–2)*: If three (or any odd or even number of) equal magnitudes have their centres of gravity on a straight line at equal distances, the centre of gravity of the system coincides with that of the middle magnitude (or the midpoint between the two middle magnitudes).

.. _ep-i-6-7:

Propositions 6 & 7: The Law of the Lever
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 192–194 · Heiberg II, 152–159
   :page: 192

.. enunciation::

   **Proposition 6.** Commensurable magnitudes balance at distances :term:`reciprocally proportional <antipeponthos>` to the weights.

Let :g:`A`, :g:`B` be commensurable magnitudes with centres of gravity :g:`A`, :g:`B`, and let :g:`DE` be a straight line divided at :g:`C` so that :eq:`A : B = DC : CE`. Place :g:`A` at :g:`E` and :g:`B` at :g:`D`. Produce :g:`ED` so that :eq:`DK = EC` and :eq:`EL = CD`; then :eq:`LK = 2 \cdot DE` has :g:`C` as its midpoint! Since :g:`A` and :g:`B` are commensurable, divide :g:`LH` (:eq:`= 2 \cdot EC`) and :g:`HK` (:eq:`= 2 \cdot CD`) into equal segments corresponding to a common measure :g:`N` of :g:`A` and :g:`B`. Placing equal unit weights :g:`N` at the midpoints of all equal segments along :g:`LK`, the first group has its centre of gravity at :g:`E` (midpoint of :g:`LH`, by :just:`Prop. 5`) and equals :g:`A`; the second group has its centre of gravity at :g:`D` (midpoint of :g:`HK`) and equals :g:`B`; while the whole uniform array on :g:`LK` balances at its midpoint :g:`C` (:just:`Post. 6`, :just:`Prop. 5`). Therefore :g:`A` at :g:`E` and :g:`B` at :g:`D` balance about :g:`C`.

.. qed::

.. enunciation::

   **Proposition 7.** And even if the magnitudes are incommensurable, they will likewise balance at distances reciprocally proportional to the magnitudes (:cite:`archimedes:equilibrium-of-planes:i-7`).

Let :eq:`(A + a) : B = DC : CE`, where :g:`A` and :g:`B` are incommensurable. If :g:`A + a` placed at :g:`E` does not balance :g:`B` placed at :g:`D`, either :g:`A + a` is too great to balance :g:`B` or not great enough. Suppose :g:`A + a` is too great. Take from :g:`A + a` a magnitude less than the excess by which it fails to balance :g:`B`, yet such that the remainder :g:`A` is **commensurable** with :g:`B` (:just:`Eucl. V. Def. 4`). Then since :g:`A`, :g:`B` are commensurable and :eq:`A : B < DC : CE`, :g:`A` at :g:`E` will *not* incline the beam at :g:`E` down, by :just:`Prop. 6`, rather :g:`D` will incline downward—contradicting that insufficient weight was removed to stop :g:`E` from inclining! Similarly :g:`B` cannot incline downward. Hence incommensurable magnitudes likewise balance at reciprocally proportional distances.

.. qed::

Propositions 8–12: Remainders, Parallelograms & Similar Triangles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 194–198 · Heiberg II, 158–169
   :page: 194

* **Proposition 8**: If :g:`AB` be a magnitude whose centre of gravity is :g:`C`, and :g:`AD` a part of it whose centre of gravity is :g:`F`, then the centre of gravity :g:`G` of the remaining part :g:`DE` lies on :g:`FC` produced so that :eq:`GC : CF = AD : DE`.
* **Propositions 9 & 10** *(with Alternative Proof)*: In any parallelogram (*Παντὸς παραλληλογράμμου τὸ κέντρον τοῦ βάρεός ἐστιν...*, Heiberg II, 162), the centre of gravity lies on the straight line joining the middle points of opposite sides (Prop. 9), and coincides with **the point of intersection of its diagonals** (Prop. 10).
* **Propositions 11 & 12**: If two triangles be similar, and points within them be similarly situated with respect to them, if one point is the centre of gravity of the first triangle, the other point is likewise the centre of gravity of the second triangle.

.. _ep-i-13-14:

Propositions 13 & 14: The Triangle Centroid ``X(2)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 198–201 · Heiberg II, 168–177
   :page: 198

.. enunciation::

   **Proposition 13.** In any triangle, the :term:`centre of gravity <kentron-barous>` lies on the straight line joining any angle to the middle point of the opposite side.

   **Proposition 14.** It follows at once that the centre of gravity of any triangle is at the intersection of the lines drawn from any two angles to the middle points of the opposite sides respectively.

.. picture:: /_static/figures/fig_triangle_centroid.svg
   :caption: Book I, Propositions 6–7 & 13–14 — Law of the Lever and Concurrency of Medians at Triangle Centroid G = X(2)

Let :g:`ABC` be a triangle, and :g:`D` the middle point of :g:`BC`. Join :g:`AD`. If the centre of gravity :g:`H` does not lie on :g:`AD`, draw :g:`HI \parallel BC` meeting :g:`AD` in :g:`I`. Bisect :g:`DC`, :g:`BD` repeatedly and draw parallels to :g:`AD` from the division points, inscribing in :g:`\triangle ABC` a union of parallelograms symmetrical about :g:`AD` such that the remaining small corner triangles (all similar to :g:`\triangle ABC`) have a combined area having to the inscribed parallelograms a ratio *less* than :eq:`HI : IA` (:just:`Eucl. X. 1`, :just:`Eucl. VI. 19`).

By :just:`Prop. 9`, every inscribed parallelogram has its centre of gravity on :g:`AD`; therefore the centre of gravity :g:`P` of all the parallelograms taken together lies on :g:`AD`. Let :g:`Q` be the centre of gravity of the remaining corner triangles taken together; by :just:`Prop. 8`, :g:`P`, :g:`H`, :g:`Q` are collinear and:

.. math::

   \frac{\text{Remaining Triangles}}{\text{Inscribed Parallelograms}} = \frac{PH}{HQ}.

Draw :g:`KL \parallel AD` through :g:`Q` meeting :g:`BC`, :g:`AC`; since all corner triangles lie between :g:`AD` and its bounding tangents, :g:`Q` cannot lie beyond the boundary parallel through :g:`C`, implying :eq:`PH : HQ > HI : IA`, contradicting our construction! *(Archimedes also supplies a pure similarity proof decomposing :g:`\triangle ABC` into a central parallelogram :g:`FKEC` and two half-scale triangles :g:`\triangle AFE`, :g:`\triangle EBD` via :just:`Prop. 10` and :just:`Post. 5`.)*

Applying **Proposition 13** to two medians :g:`AD` and :g:`BE` yields **Proposition 14**: the three medians concur at the unique barycenter :g:`G` dividing each median in the ratio :eq:`2 : 1` (:cite:`geometor:etc`, Kimberling center ``X(2)`` with homogeneous barycentric coordinates :eq:`1 : 1 : 1`).

.. qed::

Proposition 15: Centre of Gravity of a Trapezium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 201–202 · Heiberg II, 176–181
   :page: 201

.. enunciation::

   **Proposition 15.** In any trapezium having two sides parallel to one another, the centre of gravity lies on the straight line joining the middle points of the parallel sides, at the point dividing it so that the segment adjacent to the smaller parallel side is to the remaining segment as twice the greater parallel side together with the smaller is to twice the smaller together with the greater:

   .. math::

      GE : GF = (2 \cdot BC + AD) : (2 \cdot AD + BC).

Proved by producing the non-parallel sides to meet at :g:`H`, decomposing the trapezium as the difference of two triangles :g:`\triangle HBC - \triangle HAD` whose centroids trisect :g:`HF` and :g:`HE` (:just:`Prop. 14`), and applying the remainder formula (:just:`Prop. 8`).

.. qed::

----

Book II — Centres of Gravity of Parabolic Segments
--------------------------------------------------

.. folio:: Heath (1897), pp. 203–220 · Heiberg II, 182–241
   :page: 203

In **Book II** (10 Propositions), Archimedes combines Book I with the *Quadrature of the Parabola* (:cite:`archimedes:quadrature-of-parabola`) to determine the exact centre of gravity of any :term:`parabolic segment <tmema-paraboles>` and parabolic frustum:

* **Proposition 1**: Two parabolic segments placed on a balance are treated as plane laminae via :just:`Book I, Props. 6–7`.
* **Propositions 2–7**: Recursive inscription of triangles ("known manner" :g:`\triangle ABC` + :g:`\triangle ADB` + :g:`\triangle BEC` + ...) proves that the centre of gravity of any parabolic segment lies on its diameter :g:`AO` (Prop. 2), that similar-like exhaustion polygons have centres of gravity approaching that of the segment (Props. 3–6), and that the ratio in which the centre of gravity divides the diameter is **constant** across all parabolic segments (Prop. 7).
* **Proposition 8** *(Fundamental Centroid of the Parabola)*:

  .. enunciation::

     If :g:`AO` be the diameter of a parabolic segment, and :g:`G` its centre of gravity, then :eq:`AG = \frac{3}{2} GO` (that is, :eq:`AG = \frac{3}{5} AO` from the vertex :g:`A` and :eq:`GO = \frac{2}{5} AO` from the base midpoint :g:`O`).

  Let :eq:`AG : GO = m : n` identically for every parabolic segment (:just:`Prop. 7`). Decompose the main segment :g:`BAb` (area :eq:`\frac{4}{3}\triangle BAb`) into its inscribed triangle :g:`\triangle BAb` (centroid at :eq:`\frac{2}{3} AO` from :g:`A`, :just:`Book I, Prop. 14`) and two flanking sub-segments on :g:`AB`, :g:`Ab` (combined area :eq:`\frac{1}{3}\triangle BAb`), whose diameters have length :eq:`\frac{3}{4} AO` measured from the line through :g:`A` and whose centroids also divide their diameters in the identical unknown ratio :eq:`AG : GO`! Taking moments along :g:`AO` via :just:`Book I, Props. 4, 6–8` yields a linear equation in :eq:`AG / AO` whose unique solution is :eq:`AG = \frac{3}{5} AO`, i.e. :eq:`AG : GO = 3 : 2`.

* **Proposition 9**: Arithmetic lemma on six terms in continued proportion used to reduce the frustum moment equation.
* **Proposition 10**: Exact division ratio for the centre of gravity of the **parabolic frustum** cut off between any two parallel chords.

.. qed::
