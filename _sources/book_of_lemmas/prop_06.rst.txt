:canonical_id: LA.6
:order: 6
:type: proposition

Proposition 6: Maximum Inscribed Circle in the Arbelos & Pappus Chain
=====================================================================

.. folio:: Heath (1897), pp. 307–309 · Heiberg II, 433–436
   :page: 307

.. enunciation::

   **Proposition 6 (Maximum Inscribed Circle in the Arbelos).** Let :g:`AB`, the diameter of a semicircle, be divided at :g:`C` so that :eq:`AC = \frac{3}{2} CB` [or in any given ratio :eq:`\lambda : 1`]. Describe semicircles within the first semicircle and on :g:`AC`, :g:`CB` as diameters, and suppose a circle drawn touching all three semicircles. If :g:`GH` be the diameter of this circle, to find the relation between :g:`GH` and :g:`AB`.

.. picture:: /_static/figures/fig_arbelos_inscribed.svg
   :caption: Book of Lemmas, Proposition 6 — Circle Tangent to All Three Semicircles of the Arbelos (GH : AB = 6 : 19 for 3 : 2) & Pappus Chain

By repeated application of **Proposition 1** through the three points of contact, for :eq:`AC : CB = 3 : 2` it follows that :eq:`GH : AB = 6 : 19`, and in general if :eq:`AC : CB = \lambda : 1`, then:

.. math::

   GH : AB = \lambda : (1 + \lambda + \lambda^2) = (AC \cdot CB) : (AC^2 + AC \cdot CB + CB^2).

Furthermore, the height of the centre of this inscribed circle above :g:`AB` equals its own diameter :g:`GH`—the base case (:eq:`n = 1`) of the celebrated **‘ancient proposition’** preserved by :person:`Pappus <pappus>` (:cite:`pappus:synagoge:iv`, IV.14: :eq:`h_n = n \cdot d_n` for the :eq:`n`-th circle in the infinite tangent chain)!

.. qed::
