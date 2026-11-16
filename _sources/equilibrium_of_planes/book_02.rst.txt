:canonical_id: EP.II
:order: 7
:type: section

Book II: Centres of Gravity of Parabolic Segments (Propositions 1–10)
=====================================================================

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
