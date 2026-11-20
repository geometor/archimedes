:canonical_id: EP.I.13
:order: 14
:type: proposition

.. _ep-i-13-14:

Book I, Proposition 13: Triangle Centre of Gravity Lies on Each Median
======================================================================

.. folio:: Heath (1897), pp. 198–201 · Heiberg II, 168–177
   :page: 198

.. enunciation::

   **Proposition 13.** In any triangle, the :term:`centre of gravity <kentron-barous>` lies on the straight line joining any angle to the middle point of the opposite side.

.. picture:: /_static/figures/fig_triangle_centroid.svg
   :caption: Book I, Propositions 6–7 & 13–14 — Law of the Lever and Concurrency of Medians at Triangle Centroid G = X(2)

Let :g:`ABC` be a triangle, and :g:`D` the middle point of :g:`BC`. Join :g:`AD`. If the centre of gravity :g:`H` does not lie on :g:`AD`, draw :g:`HI \parallel BC` meeting :g:`AD` in :g:`I`. Bisect :g:`DC`, :g:`BD` repeatedly and draw parallels to :g:`AD` from the division points, inscribing in :g:`\triangle ABC` a union of parallelograms symmetrical about :g:`AD` such that the remaining small corner triangles (all similar to :g:`\triangle ABC`) have a combined area having to the inscribed parallelograms a ratio *less* than :eq:`HI : IA` (:just:`Eucl. X. 1`, :just:`Eucl. VI. 19`).

By :just:`Prop. 9`, every inscribed parallelogram has its centre of gravity on :g:`AD`; therefore the centre of gravity :g:`P` of all the parallelograms taken together lies on :g:`AD`. Let :g:`Q` be the centre of gravity of the remaining corner triangles taken together; by :just:`Prop. 8`, :g:`P`, :g:`H`, :g:`Q` are collinear and:

.. math::

   \frac{\text{Remaining Triangles}}{\text{Inscribed Parallelograms}} = \frac{PH}{HQ}.

Draw :g:`KL \parallel AD` through :g:`Q` meeting :g:`BC`, :g:`AC`; since all corner triangles lie between :g:`AD` and its bounding tangents, :g:`Q` cannot lie beyond the boundary parallel through :g:`C`, implying :eq:`PH : HQ > HI : IA`, contradicting our construction! *(Archimedes also supplies a pure similarity proof decomposing :g:`\triangle ABC` into a central parallelogram :g:`FKEC` and two half-scale triangles :g:`\triangle AFE`, :g:`\triangle EBD` via :just:`Prop. 10` and :just:`Post. 5`.)*

.. qed::
