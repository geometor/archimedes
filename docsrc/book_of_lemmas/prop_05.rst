:canonical_id: LA.5
:order: 3
:type: proposition

Proposition 5: Archimedes' Twin Circles
=======================================

.. folio:: Heath (1897), pp. 306–307 · Heiberg II, 432–433
   :page: 306

.. enunciation::

   **Proposition 5 (Archimedes' Twin Circles).** Let :g:`AB` be the diameter of a semicircle, :g:`C` any point on :g:`AB`, and :g:`CD` perpendicular to it, and let semicircles be described within the first semicircle and having :g:`AC`, :g:`CB` as diameters. Then if two circles be drawn touching :g:`CD` on different sides and each touching two of the semicircles, the circles so drawn will be **equal** (:term:`Archimedes' Twin Circles <twin-circles>`).

*Proof*: Let one circle touch :g:`CD` at :g:`E`, the outer semicircle :g:`AB` at :g:`F`, and the inner semicircle :g:`AC` at :g:`G`, and let its diameter :g:`EH` be parallel to :g:`AB`. By **Proposition 1**, :g:`FHG` and :g:`BFA` and :g:`AGC` align homothetically, yielding :eq:`AB : AC = BC : EH`! That is:

.. math::

   AB \cdot EH = AC \cdot CB \implies EH = \frac{AC \cdot CB}{AB}.

Because the expression :eq:`\frac{AC \cdot CB}{AB}` is **symmetric** in :g:`AC` and :g:`CB`, the second circle inscribed on the opposite side of :g:`CD` (touching :g:`CD`, semicircle :g:`AB`, and semicircle :g:`CB`) has diameter :eq:`\frac{CB \cdot AC}{AB}`, strictly equal to :g:`EH`!

.. qed::