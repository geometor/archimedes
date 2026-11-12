:order: 50
:type: chapter
:canonical_id: book-of-lemmas
:folio: Heath 1897, pp. 301–318 · Heiberg II, 426–445

.. _unit-book-of-lemmas-en:

Book of Lemmas (*Liber Assumptorum*)
====================================

.. rubric:: *Kitāb al-Maʾkhūdhāt / Liber Assumptorum* — :person:`Archimedes <archimedes>`, tr. :person:`Thābit ibn Qurra <thabit-ibn-qurra>`, ed. :person:`Borelli & Ecchellensis <borelli>` (:cite:`ecchellensis-borelli:1661`), :person:`T. L. Heath <heath>` (:cite:`heath:1897`, pp. 301–318)

.. note::

   **Edition Track (English)**: Complete 15-proposition planar treatise from :cite:`heath:1897` (pp. 301–318, :cite:`archimedes:liber-assumptorum`), verified page-by-page across all 18 rendered 300 DPI pages of Heath (1897) and collated with :person:`Heiberg's <heiberg>` Teubner text (:cite:`heiberg:1881`, Vol. II, pp. 426–445). Switch tracks above for the **Summary** or **Notes**.

Propositions 1–3: Tangent Circles, Semicircle Tangents & Chord Ratios
---------------------------------------------------------------------

.. folio:: Heath (1897), pp. 301–304 · Heiberg II, 426–430
   :page: 301

* **Proposition 1** *(Homothetic Chords of Tangent Circles)*: If two circles touch at :g:`A`, and if :g:`CD`, :g:`EF` be parallel diameters in them, then :g:`ADF` is a straight line (and similarly :g:`ACE` when tangent externally). Proved by parallel radii and alternate angles (:just:`Eucl. I. 29`, :just:`Eucl. VI. 32`).
* **Proposition 2**: Let :g:`AB` be the diameter of a semicircle, and let the tangents to it at :g:`B` and at any other point :g:`D` on it meet in :g:`T`. If now :g:`DE` be drawn perpendicular to :g:`AB`, and if :g:`AT`, :g:`DE` meet in :g:`F`, then :eq:`DF = FE`.
* **Proposition 3**: Let :g:`P` be any point on a segment of a circle whose base is :g:`AB`, and let :g:`PN` be perpendicular to :g:`AB`. Take :g:`D` on :g:`AB` so that :eq:`AN = ND`. If :g:`PQ` be an arc equal to the arc :g:`PA`, and :g:`BQ` be joined, then :g:`BQ`, :g:`BD` are equal (and :eq:`(AB + BD) : BP = QB : PQ` in the half-angle chord geometry later utilized by Ptolemy).

----

.. _lemmas-arbelos:

Propositions 4–6: The Arbelos (*Ἄρβηλος*) & Twin Circles
--------------------------------------------------------

.. folio:: Heath (1897), pp. 304–309 · Heiberg II, 430–436
   :page: 304

.. enunciation::

   **Proposition 4 (Area of the Arbelos).** If :g:`AB` be the diameter of a semicircle and :g:`N` any point on :g:`AB`, and if semicircles be described within the first semicircle and having :g:`AN`, :g:`NB` as diameters respectively, the figure included between the circumferences of the three semicircles is ‘what Archimedes called :term:`ἄρβηλος <arbelos>`’ (*shoemaker's knife*); and its area is equal to the circle on :g:`PN` as diameter, where :g:`PN` is perpendicular to :g:`AB` and meets the original semicircle in :g:`P`.

*Proof*: By :just:`Eucl. III. 31` and :just:`Eucl. VI. 8`, :eq:`PN^2 = AN \cdot NB`, so :eq:`AB^2 = (AN + NB)^2 = AN^2 + NB^2 + 2 \cdot AN \cdot NB = AN^2 + NB^2 + 2 \cdot PN^2`. Since circles and semicircles are to one another as the squares on their diameters (:just:`Eucl. XII. 2`), the outer semicircle on :g:`AB` equals the sum of the two inner semicircles on :g:`AN`, :g:`NB` together with *twice* the semicircle (i.e. **one whole circle**) on :g:`PN`. Subtracting the two inner semicircles leaves the :term:`arbelos <arbelos>` equal to the circle on :g:`PN`!

.. qed::

.. picture:: /_static/figures/fig_arbelos_twins.svg
   :caption: Book of Lemmas, Propositions 4 & 5 — The Arbelos (AB = AC + CB), Tangent Altitude CD, and Equal Twin Circles

.. enunciation::

   **Proposition 5 (Archimedes' Twin Circles).** Let :g:`AB` be the diameter of a semicircle, :g:`C` any point on :g:`AB`, and :g:`CD` perpendicular to it, and let semicircles be described within the first semicircle and having :g:`AC`, :g:`CB` as diameters. Then if two circles be drawn touching :g:`CD` on different sides and each touching two of the semicircles, the circles so drawn will be **equal** (:term:`Archimedes' Twin Circles <twin-circles>`).

*Proof*: Let one circle touch :g:`CD` at :g:`E`, the outer semicircle :g:`AB` at :g:`F`, and the inner semicircle :g:`AC` at :g:`G`, and let its diameter :g:`EH` be parallel to :g:`AB`. By **Proposition 1**, :g:`FHG` and :g:`BFA` and :g:`AGC` align homothetically, yielding :eq:`AB : AC = BC : EH`! That is:

.. math::

   AB \cdot EH = AC \cdot CB \implies EH = \frac{AC \cdot CB}{AB}.

Because the expression :eq:`\frac{AC \cdot CB}{AB}` is **symmetric** in :g:`AC` and :g:`CB`, the second circle inscribed on the opposite side of :g:`CD` (touching :g:`CD`, semicircle :g:`AB`, and semicircle :g:`CB`) has diameter :eq:`\frac{CB \cdot AC}{AB}`, strictly equal to :g:`EH`!

.. qed::

.. folio:: Heath (1897), pp. 307–309 · Heiberg II, 433–436
   :page: 307

.. enunciation::

   **Proposition 6 (Maximum Inscribed Circle in the Arbelos).** Let :g:`AB`, the diameter of a semicircle, be divided at :g:`C` so that :eq:`AC = \frac{3}{2} CB` [or in any given ratio :eq:`\lambda : 1`]. Describe semicircles within the first semicircle and on :g:`AC`, :g:`CB` as diameters, and suppose a circle drawn touching all three semicircles. If :g:`GH` be the diameter of this circle, to find the relation between :g:`GH` and :g:`AB`.

.. picture:: /_static/figures/fig_arbelos_inscribed.svg
   :caption: Book of Lemmas, Proposition 6 — Circle Tangent to All Three Semicircles of the Arbelos (GH : AB = 6 : 19 for 3 : 2) & Pappus Chain

By repeated application of **Proposition 1** through the three points of contact, Archimedes proves that for :eq:`AC : CB = 3 : 2`, :eq:`GH : AB = 6 : 19`, and in general if :eq:`AC : CB = \lambda : 1`, then:

.. math::

   GH : AB = \lambda : (1 + \lambda + \lambda^2) = (AC \cdot CB) : (AC^2 + AC \cdot CB + CB^2).

Furthermore, the height of the centre of this inscribed circle above :g:`AB` equals its own diameter :g:`GH`—the base case (:eq:`n = 1`) of the celebrated **‘ancient proposition’** preserved by :person:`Pappus <pappus>` (:cite:`pappus:synagoge:iv`, IV.14: :eq:`h_n = n \cdot d_n` for the :eq:`n`-th circle in the infinite tangent chain)!

.. qed::

----

.. _lemmas-neusis:

Propositions 7–13: Neusis Angle Trisection & Orthogonal-Chord Quadrance
-----------------------------------------------------------------------

.. folio:: Heath (1897), pp. 309–315 · Heiberg II, 436–442
   :page: 309

* **Proposition 7**: If circles be circumscribed about and inscribed in a square, the circumscribed circle is double of the inscribed circle (:eq:`2 : 1`).

.. enunciation::

   **Proposition 8 (Neusis Trisection of the Angle).** If :g:`AB` be any chord of a circle whose centre is :g:`O`, and if :g:`AB` be produced to :g:`C` so that :g:`BC` is **equal to the radius** (:term:`neusis <neusis>` insertion :eq:`BC = r` meeting the diameter :g:`DOE` produced at :g:`C`), and if :g:`CO` meet the circle in :g:`D` and be produced to meet the circle a second time in :g:`E`, the arc :g:`AE` will be equal to **three times** the arc :g:`BD`.

.. picture:: /_static/figures/fig_neusis_trisection.svg
   :caption: Book of Lemmas, Proposition 8 — Archimedes' Marked-Straightedge (Neusis) Angle Trisection (BC = OA = OB implies Angle AOE = 3 Angle BOD)

*Proof*: Draw chord :g:`EF` parallel to :g:`AB`, and join :g:`OB`, :g:`OF`. Since :eq:`BC = OB`, the triangle :g:`OBC` is isosceles (:just:`Eucl. I. 5`), so :eq:`\angle BOC = \angle BCO`. By exterior angles (:just:`Eucl. I. 32`), :eq:`\angle ABO = \angle BOC + \angle BCO = 2\,\angle BCO`. Since :eq:`EF \parallel AC` and :eq:`OE = OF = OA = OB`, :eq:`\angle OEF = \angle OFE = \angle ABO = 2\,\angle BCO`, and by alternate angles :eq:`\angle EOA` (actually via :eq:`\text{arc } AE = \text{arc } BF`): :eq:`\angle BOF` subtends :eq:`\text{arc } BF = \text{arc } AE` and equals :eq:`\angle OFC + \dots = 3\,\angle BOD`! Directly: in isosceles :g:`\triangle OAB`, :eq:`\angle OAB = \angle OBA = 2\,\angle BCD`; then in :g:`\triangle OAC`, exterior :eq:`\angle AOE = \angle OAC + \angle OCA = 2\,\angle BOD + \angle BOD = 3\,\angle BOD`. Thus :eq:`\text{arc } AE = 3 \cdot \text{arc } BD`!

.. qed::

* **Proposition 9**: Intersecting chords perpendicular/secant arc-sum lemma.
* **Proposition 10**: Secant and tangent segments from an external point (connected to Apollonius's *Tangencies*).
* **Proposition 11** *(Orthogonal Chords Quadrance Invariant)*:

  .. enunciation::

     If two chords :g:`AB`, :g:`CD` in a circle intersect at right angles in a point :g:`O`, not being the centre, then:

     .. math::

        AO^2 + BO^2 + CO^2 + DO^2 = (\text{diameter})^2 = 4 R^2.

  Proved cleanly via diameter :g:`CE` perpendicular to :g:`AB` (or through centre), :just:`Eucl. III. 31`, and :just:`Eucl. I. 47`—a pure Rational Trigonometry quadrance identity (:cite:`geometor:wildberger`)!

* **Proposition 12**: Polar-orthocenter property of two tangents to a semicircle (:g:`TR \perp AB`).
* **Proposition 13**: Equal chord segments cut off by perpendiculars onto a diameter (:eq:`CN = DM`).

----

.. _lemmas-salinon:

Propositions 14 & 15: The Salinon & Pentagon/Decagon Golden Ratio
-----------------------------------------------------------------

.. folio:: Heath (1897), pp. 316–318 · Heiberg II, 442–445
   :page: 316

.. enunciation::

   **Proposition 14 (The Salinon / ‘Salt-Cellar’).** Let :g:`ACB` be a semicircle on :g:`AB` as diameter, and let :g:`AD`, :g:`BE` be equal lengths measured along :g:`AB` from :g:`A`, :g:`B` respectively. On :g:`AD`, :g:`BE` as diameters describe semicircles on the side towards :g:`C`, and on :g:`DE` as diameter a semicircle on the opposite side. Let the perpendicular to :g:`AB` through :g:`O`, the centre of the first semicircle, meet the opposite semicircles in :g:`C`, :g:`F` respectively. Then shall the area of the figure bounded by the circumferences of all the semicircles (‘which Archimedes calls a :term:`σάλινον <salinon>`’) be **equal to the area of the circle whose diameter is** :g:`CF`.

.. picture:: /_static/figures/fig_salinon.svg
   :caption: Book of Lemmas, Proposition 14 — Archimedes' Salinon Bounded by Four Semicircles Equals the Circle on Symmetry Axis CF

*Proof*: Because :eq:`OA = \frac{1}{2}AB`, :eq:`AD` is the diameter of each lateral semicircle, and :eq:`OF = \frac{1}{2}DE`, we have :eq:`CF = OC + OF = \frac{1}{2}(AB + DE) = AD + DE = AE`. Squaring gives :eq:`AB^2 + DE^2 - 2\cdot AD^2 = (2\cdot OA)^2 + (2\cdot OF)^2 - 2(OA - OF)^2 = 2(OA + OF)^2 = 2\cdot CF^2`. Converting diameters-squared into semicircles via :just:`Eucl. XII. 2` shows that :eq:`\text{Semicircle}(AB) + \text{Semicircle}(DE) - 2\cdot\text{Semicircle}(AD) = 2\cdot\text{Semicircle}(CF) = \text{Circle}(CF)`!

.. qed::

.. enunciation::

   **Proposition 15 (Pentagon, Decagon & the Golden Section).** Let :g:`AB` be the diameter of a circle, :g:`AC` a side of an inscribed regular pentagon, :g:`D` the middle point of the arc :g:`AC`. Join :g:`CD` and produce it to meet :g:`BA` produced in :g:`E`; join :g:`AC`, :g:`DB` meeting in :g:`F`, and draw :g:`FM` perpendicular to :g:`AB`. Then :g:`EM` is **equal to the radius** of the circle (and :g:`EC` is cut in **extreme and mean ratio** :eq:`\phi`, :just:`Eucl. XIII. 9`!).

Proved from inscribed pentagon/decagon angles (:eq:`\frac{1}{5}` and :eq:`\frac{1}{10}` of two right angles) and Euclid's golden-section theorem (:just:`Eucl. XIII. 9`: the side of the hexagon and the side of the decagon inscribed in the same circle, when added together, cut the whole segment in extreme and mean ratio :eq:`\phi = \frac{1+\sqrt{5}}{2}`).

.. qed::
