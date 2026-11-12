:order: 30
:type: chapter
:canonical_id: quadrature-of-parabola
:folio: Heath 1897, pp. 233–252 · Heiberg II, 294–353

.. _unit-quadrature-of-parabola-en:

Quadrature of the Parabola (*Τετραγωνισμὸς παραβολῆς*)
======================================================

.. rubric:: *Quadratura Parabolae* — :person:`Archimedes of Syracuse <archimedes>` (ed. :person:`T. L. Heath <heath>`, 1897, pp. 233–252; :person:`J. L. Heiberg <heiberg>`, Vol. II, pp. 294–353)

.. note::

   **Edition Track (English)**: Public-domain translation from :cite:`heath:1897` (pp. 233–252), verified against 300 DPI scans of Heath (1897) and collated with :person:`Heiberg's <heiberg>` critical Doric Greek edition (:cite:`heiberg:1881`, Vol. II, pp. 294–353). Switch tracks above for the **Summary** or **Notes**.

Prefatory Epistle to Dositheus
------------------------------

.. folio:: Heath (1897), pp. 233–235 · Heiberg II, 294–299
   :page: 233

“**ARCHIMEDES TO DOSITHEUS GREETING.**

When I heard that :person:`Conon <conon>`, who was my friend in his lifetime, was dead, but that you were acquainted with Conon and withal versed in geometry, while I grieved greatlily for the loss not only of a friend but of an admirable mathematician, I set myself the task of communicating to you, as I had intended to send to Conon, a certain geometrical theorem which had not been investigated before but has now been investigated by me, and which I first discovered by means of mechanics and then exhibited by means of geometry.”

:person:`Archimedes <archimedes>` recounts to :person:`Dositheus <dositheus>` how earlier geometers attempted in vain to square the circle and hyperbolic or elliptic segments, whereas no one had hitherto attempted to square the segment bounded by a straight line and a **section of a right-angled cone** (:term:`parabolic segment <tmema-paraboles>`). He announces its exact quadrature—that any parabolic segment is **four-thirds** of the triangle having the same base and equal height—and explicitly states the continuity postulate employed in the proof (:term:`Archimedes' Lemma <archimedes-lemma>`, cf. :cite:`hilbert:1899`):

.. enunciation::

   **Lemma of Archimedes.** *The excess by which the greater of (two) unequal areas exceeds the less can, by being added to itself, be made to exceed any given finite area.*

Archimedes notes that earlier geometers (:person:`Eudoxus of Cnidus <eudoxus>`) used this very lemma to prove that circles are to one another in the duplicate ratio of their diameters (:just:`Eucl. XII. 2`), spheres in the triplicate ratio of their diameters (:just:`Eucl. XII. 18`), every pyramid one-third of the prism on the same base and equal altitude (:just:`Eucl. XII. 7`), and every cone one-third of the cylinder (:just:`Eucl. XII. 10`).

----

Part I — Mechanical Exhaustion via the Lever (Propositions 1–17)
----------------------------------------------------------------

.. folio:: Heath (1897), pp. 235–246 · Heiberg II, 298–335
   :page: 235

Propositions 1–5: Conic Symptomata of the Parabola
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Drawing on the pre-Apollonian *Elements of Conics* (:person:`Euclid <euclid>` and :person:`Aristaeus <aristaeus>`), Archimedes recalls for a parabola with chord :g:`QQ'` bisected at :g:`V` by diameter :g:`PV` and tangent :g:`PT` at vertex :g:`P`:

* **Prop. 1–2**: :eq:`PV` bisects all chords parallel to :g:`QQ'`, and if tangent :g:`QT` meets diameter :g:`PV` produced at :g:`T`, then :eq:`PV = PT`.
* **Prop. 3**: Ordinate-squared property :eq:`QV^2 : Q'V'^2 = PV : PV'`.
* **Props. 4–5**: For any chord :g:`Qq`, diameter :g:`PV` through :g:`P`, and parallel lines drawn to the diameter meeting the tangent :g:`qT` at :g:`E`, the parabola at :g:`R`, and the chord :g:`Qq` at :g:`O` (while :g:`qO` meets :g:`PV` at :g:`V`), the intercept ratio satisfies:

  .. math::

     QO : Oq = ER : RO.

Propositions 6–15: Balancing Triangles and Trapezia on a Beam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 238–244 · Heiberg II, 306–329
   :page: 238

Suspend a right-angled triangle :g:`BDG` beneath a horizontal balance beam :g:`AOB` with fulcrum :g:`O` and equal opposite arm :eq:`OA = OB`:

* **Props. 6–7**: Because the :term:`centre of gravity <kentron-barous>` of :g:`\triangle BDG` lies horizontally at :eq:`\frac{1}{3} OB` from :g:`O` (:just:`Equil. I. 14`), an area :g:`P` hung at :g:`A` balances :g:`\triangle BDG` in its actual position when :eq:`P = \frac{1}{3} \triangle BDG`.
* **Props. 8–13**: Establishes upper and lower lever inequalities for every vertical trapezium strip cut from :g:`\triangle BDG` by equally spaced parallels to the diameter.
* **Props. 14–15**: Partitioning the base :g:`Qq` of the parabolic segment into :eq:`n` equal parts and drawing parallels to the diameter inscribes and circumscribes finite families of rectilinear trapezia inside :g:`\triangle QqT` (whose area is :eq:`4 \cdot \triangle QPq`). Summing the lever inequalities across all :eq:`n` strips compresses the balancing weight :g:`M` at :g:`A` between circumscribed and inscribed trapezium weights whose difference equals a single triangle of base :eq:`\frac{1}{n} Qq`, which can be made smaller than any assigned area (:term:`Archimedes' Lemma <archimedes-lemma>`).

Propositions 16 & 17: First Quadrature Theorem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 244–246 · Heiberg II, 330–335
   :page: 244

* **Proposition 16**: By double indirect :term:`exhaustion <exhaustion>` on the balance beam, the parabolic segment equals **one-third** of the enveloping tangent triangle :g:`\triangle QqT`.
* **Proposition 17**: Since :eq:`\triangle QqT = 4 \cdot \triangle QPq` (where :g:`P` is the vertex of the segment where the tangent is parallel to :g:`Qq`), it follows immediately that:

  .. enunciation::

     *The area of any segment of a parabola is four-thirds of the triangle which has the same base and equal height.*

----

Part II — Pure Geometric Exhaustion (Propositions 18–24)
--------------------------------------------------------

.. folio:: Heath (1897), pp. 246–252 · Heiberg II, 336–353
   :page: 246

.. picture:: /_static/figures/fig_parabola_exhaustion.svg
   :caption: Propositions 18–24 — Recursive Geometric Exhaustion of Parabolic Segment ABC (Area = 4/3 Triangle ABC)

To demonstrate the theorem purely geometrically without mechanical postulates, Archimedes defines the *base* :g:`AC`, *vertex* :g:`B` (point of maximum perpendicular height, where the tangent is parallel to :g:`AC`), and *height* of any segment:

* **Propositions 18–19**: If diameters through the midpoints :g:`F`, :g:`G` of :g:`AD` (half-chord) meet the parabola at secondary vertices :g:`D`, :g:`E`, then :eq:`BM = \frac{4}{3} DN` (actually :eq:`BV = 4 \cdot DF` measured from the chord, so the sub-segment height is :eq:`\frac{1}{4}` of the main height measured along the diameter!).
* **Proposition 20**: If :g:`ABC` be a parabolic segment with vertex :g:`B`, then :g:`\triangle ABC` is **greater than half** the area of the segment :g:`ABC` (since :g:`\triangle ABC` is half of the circumscribed parallelogram formed by the tangent at :g:`B` and diameters through :g:`A`, :g:`C`). Repeated inscription therefore exhausts the segment by :just:`Eucl. X. 1`!
* **Proposition 21**: If :g:`D`, :g:`E` be the vertices of the two remaining segments on :g:`AB` and :g:`BC`, then:

  .. math::

     \triangle ABC = 8 \cdot \triangle ADB = 8 \cdot \triangle BEC, \qquad \text{whence} \qquad \triangle ADB + \triangle BEC = \frac{1}{4} \triangle ABC.

* **Proposition 22**: For any finite sequence of areas :g:`A, B, C, D, \dots` formed at successive stages of this bisection, their sum :eq:`A + B + C + \dots` is strictly **less** than the area of the parabolic segment.
* **Proposition 23** *(Exact Finite Geometric Series Identity)*:

  .. enunciation::

     Given a series of areas :g:`A, B, C, D, \dots, Z`, of which :g:`A` is the greatest, and each is equal to four times the next in order, then:

     .. math::

        A + B + C + D + \dots + Z + \frac{1}{3} Z = \frac{4}{3} A.

  *Proof*: Add :eq:`b = \frac{1}{3}B`, :eq:`c = \frac{1}{3}C`, ..., :eq:`z = \frac{1}{3}Z`. Since :eq:`B + b = \frac{4}{3}B = \frac{1}{3}A`, :eq:`C + c = \frac{1}{3}B`, ..., :eq:`Z + z = \frac{1}{3}Y`, summing all terms gives :eq:`(A + B + \dots + Z) + (b + c + \dots + z) = A + \frac{1}{3}(A + B + \dots + Y)`. Subtracting :eq:`b + c + \dots + y = \frac{1}{3}(B + C + \dots + Y)` from both sides leaves :eq:`A + B + \dots + Z + \frac{1}{3}Z = A + \frac{1}{3}A = \frac{4}{3}A`!

* **Proposition 24** *(Geometric Quadrature of the Parabola)*:

  .. enunciation::

     Every segment bounded by a parabola and a chord :g:`AC` is equal to four-thirds of the triangle :g:`△ABC` which has the same base as the segment and equal height.

  Let :eq:`K = \frac{4}{3}\triangle ABC`.

  1. *Suppose the segment greater than* :g:`K`: Inscribe triangles recursively until the remaining parabolic segments leave a sum less than :eq:`\text{Segment} - K` (:just:`Prop. 20`, :just:`Eucl. X. 1`). Then the inscribed polygon :eq:`A + B + \dots + Z > K = \frac{4}{3}A`, contradicting :just:`Prop. 23` (:eq:`A + B + \dots + Z = \frac{4}{3}A - \frac{1}{3}Z < \frac{4}{3}A`)!
  2. *Suppose the segment less than* :g:`K`: Let :eq:`A = \triangle ABC`, :eq:`B = \frac{1}{4}A`, ..., continuing until the last term :g:`Z` is less than :eq:`K - \text{Segment}`. By :just:`Prop. 23`, :eq:`K - (A + B + \dots + Z) = \frac{1}{3}Z < Z < K - \text{Segment}`, whence :eq:`A + B + \dots + Z > \text{Segment}`, contradicting :just:`Prop. 22`!

  Therefore the parabolic segment is neither greater nor less than :eq:`K = \frac{4}{3}\triangle ABC`; it is strictly equal to :eq:`\frac{4}{3}\triangle ABC`.

.. qed::
