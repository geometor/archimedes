:canonical_id: METH.1
:order: 2
:type: proposition

.. _method-prop-1:

Proposition 1: Heuristic Slice Quadrature of the Parabola
=========================================================

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
