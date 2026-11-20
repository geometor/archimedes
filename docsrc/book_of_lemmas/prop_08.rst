:canonical_id: LA.8
:order: 8
:type: proposition

.. _lemmas-neusis:

Proposition 8: Neusis Angle Trisection
======================================

.. folio:: Heath (1897), pp. 309–311 · Heiberg II, 436–438
   :page: 309

.. enunciation::

   **Proposition 8 (Neusis Trisection of the Angle).** If :g:`AB` be any chord of a circle whose centre is :g:`O`, and if :g:`AB` be produced to :g:`C` so that :g:`BC` is **equal to the radius** (:term:`neusis <neusis>` insertion :eq:`BC = r` meeting the diameter :g:`DOE` produced at :g:`C`), and if :g:`CO` meet the circle in :g:`D` and be produced to meet the circle a second time in :g:`E`, the arc :g:`AE` will be equal to **three times** the arc :g:`BD`.

.. picture:: /_static/figures/fig_neusis_trisection.svg
   :caption: Book of Lemmas, Proposition 8 — Archimedes' Marked-Straightedge (Neusis) Angle Trisection (BC = OA = OB implies Angle AOE = 3 Angle BOD)

*Proof*: Draw chord :g:`EF` parallel to :g:`AB`, and join :g:`OB`, :g:`OF`. Since :eq:`BC = OB`, the triangle :g:`OBC` is isosceles (:just:`Eucl. I. 5`), so :eq:`\angle BOC = \angle BCO`. By exterior angles (:just:`Eucl. I. 32`), :eq:`\angle ABO = \angle BOC + \angle BCO = 2\,\angle BCO`. Since :eq:`EF \parallel AC` and :eq:`OE = OF = OA = OB`, :eq:`\angle OEF = \angle OFE = \angle ABO = 2\,\angle BCO`, and by alternate angles :eq:`\angle EOA` (actually via :eq:`\text{arc } AE = \text{arc } BF`): :eq:`\angle BOF` subtends :eq:`\text{arc } BF = \text{arc } AE` and equals :eq:`\angle OFC + \dots = 3\,\angle BOD`! Directly: in isosceles :g:`\triangle OAB`, :eq:`\angle OAB = \angle OBA = 2\,\angle BCD`; then in :g:`\triangle OAC`, exterior :eq:`\angle AOE = \angle OAC + \angle OCA = 2\,\angle BOD + \angle BOD = 3\,\angle BOD`. Thus :eq:`\text{arc } AE = 3 \cdot \text{arc } BD`!

.. qed::