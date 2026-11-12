:order: 70
:type: chapter
:canonical_id: semi-regular-solids-arenarius
:folio: Heath 1897, pp. xxxvi, 221–232 · Heiberg II, 242–291, 416–424 · Pappus V.19

.. _unit-semi-regular-solids-arenarius-en:

Semi-Regular Solids, *Stomachion* & *The Sand-Reckoner*
=======================================================

.. rubric:: *Τρισκαίδεκα ἡμικανονικὰ στερεά* (Pappus V.19) · *Στομάχιον* · *Ψαμμίτης (Arenarius)* — :person:`Archimedes <archimedes>` (:cite:`heath:1897`, pp. xxxvi, 221–232; :cite:`pappus:synagoge:v`; :cite:`heiberg:1881`)

.. note::

   **Edition Track (English)**: Combines the complete ancient record and :math:`\mathbb{Q}(\phi)` structural concordance of :person:`Archimedes' <archimedes>` **Thirteen Semi-Regular Polyhedra**, the 14-piece Palimpsest **Stomachion**, and the public-domain text of **The Sand-Reckoner (*Arenarius*)** from :cite:`heath:1897` (pp. 221–232), verified against 300 DPI scans of Heath (1897). Switch tracks above for the **Summary** or **Notes**.

Part I — The Thirteen Archimedean Semi-Regular Solids (*Pappus V.19*)
---------------------------------------------------------------------

.. folio:: Heath (1897), pp. xxxvi–xxxvii · Pappus Synagoge V.19 (Hultsch I, 350–358)
   :page: 36

Extending :person:`Euclid's <euclid>` five Platonic regular solids (:just:`Eucl. XIII. 13–18`, :cite:`euclid:elements`), :person:`Archimedes <archimedes>` discovered and classified the **entire finite family of thirteen convex semi-regular polyhedra** (:term:`Archimedean solids <semi-regular-polyhedra>`)—bounded by equilateral and equiangular polygons of *two or three species* meeting in congruent solid angles, excluding the infinite families of prisms and antiprisms. Although Archimedes' Greek roll was lost in late antiquity, :person:`Pappus of Alexandria <pappus>` (:cite:`pappus:synagoge:v`, *Synagoge* Book V, Prop. 19) preserved the exact polygon counts and ordering of all thirteen solids, later reconstructed in the Renaissance by :person:`Luca Pacioli <pacioli>` (:cite:`geometor:pacioli`, *De Divina Proportione*, 1509) and proved complete by :person:`Johannes Kepler <kepler>` (*Harmonices Mundi* Book II, 1619):

.. picture:: /_static/figures/fig_semi_regular_solids.svg
   :caption: Canonical Archimedean Semi-Regular Polyhedra (Pappus V.19) — Truncated Tetrahedron (3.6.6), Cuboctahedron (3.4.3.4), and Icosidodecahedron (3.5.3.5)

Complete Register of Pappus V.19 & ``geometor/pacioli`` Concordance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 6 24 14 26 14 16

   * - #
     - Kepler / Modern Name
     - Vertex Symbol
     - Pappus V.19 Face Census (:eq:`F`)
     - :eq:`(V, E, F)`
     - Algebraic Field
   * - **I**
     - Truncated Tetrahedron
     - ``(3.6.6)``
     - **8 faces**: :eq:`4` triangles + :eq:`4` hexagons
     - :eq:`(12, 18, 8)`
     - :eq:`\mathbb{Q}(\sqrt{2})`
   * - **II**
     - **Cuboctahedron** (*Pacioli ‘heavily abscised cube’*)
     - ``(3.4.3.4)``
     - **14 faces**: :eq:`8` triangles + :eq:`6` squares
     - :eq:`(12, 24, 14)`
     - :eq:`\mathbb{Q}` / :eq:`\mathbb{Q}(\sqrt{2})`
   * - **III**
     - Truncated Octahedron
     - ``(4.6.6)``
     - **14 faces**: :eq:`6` squares + :eq:`8` hexagons
     - :eq:`(24, 36, 14)`
     - :eq:`\mathbb{Q}(\sqrt{2})`
   * - **IV**
     - Truncated Cube
     - ``(3.8.8)``
     - **14 faces**: :eq:`8` triangles + :eq:`6` octagons
     - :eq:`(24, 36, 14)`
     - :eq:`\mathbb{Q}(\sqrt{2})`
   * - **V**
     - Rhombicuboctahedron (*Pacioli 26-base body*)
     - ``(3.4.4.4)``
     - **26 faces**: :eq:`8` triangles + :eq:`18` squares
     - :eq:`(24, 48, 26)`
     - :eq:`\mathbb{Q}(\sqrt{2})`
   * - **VI**
     - Truncated Cuboctahedron (Great Rhombicuboctahedron)
     - ``(4.6.8)``
     - **26 faces**: :eq:`12` sq. + :eq:`8` hex. + :eq:`6` oct.
     - :eq:`(48, 72, 26)`
     - :eq:`\mathbb{Q}(\sqrt{2})`
   * - **VII**
     - Snub Cube (*chiral*)
     - ``(3.3.3.3.4)``
     - **38 faces**: :eq:`32` triangles + :eq:`6` squares
     - :eq:`(24, 60, 38)`
     - Tribonacci cubic
   * - **VIII**
     - **Icosidodecahedron** (*Pacioli abscised icosahedron*)
     - ``(3.5.3.5)``
     - **32 faces**: :eq:`20` triangles + :eq:`12` pentagons
     - :eq:`(30, 60, 32)`
     - :eq:`\mathbb{Q}(\phi)`
   * - **IX**
     - **Truncated Icosahedron**
     - ``(5.6.6)``
     - **32 faces**: :eq:`12` pentagons + :eq:`20` hexagons
     - :eq:`(60, 90, 32)`
     - :eq:`\mathbb{Q}(\phi)`
   * - **X**
     - Truncated Dodecahedron
     - ``(3.10.10)``
     - **32 faces**: :eq:`20` triangles + :eq:`12` decagons
     - :eq:`(60, 90, 32)`
     - :eq:`\mathbb{Q}(\phi)`
   * - **XI**
     - Rhombicosidodecahedron
     - ``(3.4.5.4)``
     - **62 faces**: :eq:`20` tri. + :eq:`30` sq. + :eq:`12` pent.
     - :eq:`(60, 120, 62)`
     - :eq:`\mathbb{Q}(\phi)`
   * - **XII**
     - Truncated Icosidodecahedron
     - ``(4.6.10)``
     - **62 faces**: :eq:`30` sq. + :eq:`20` hex. + :eq:`12` dec.
     - :eq:`(120, 180, 62)`
     - :eq:`\mathbb{Q}(\phi)`
   * - **XIII**
     - Snub Dodecahedron (*chiral*)
     - ``(3.3.3.3.5)``
     - **92 faces**: :eq:`80` triangles + :eq:`12` pentagons
     - :eq:`(60, 150, 92)`
     - Cubic over :eq:`\mathbb{Q}(\phi)`

----

Part II — *Stomachion* (*Loculus Archimedius*) & *The Cattle Problem*
---------------------------------------------------------------------

.. folio:: Heath (1897), pp. 319–326 · Heiberg II², 416–424
   :page: 319

* **The Stomachion (*Στομάχιον*)**: Recovered from folios of the Constantinople Palimpsest alongside an Arabic witness, the :term:`Stomachion <stomachion>` dissects a square of side :eq:`12` (total area :eq:`144`) via rational midpoints and diagonal intersections into **14 polygonal pieces**—11 triangles, 2 quadrilaterals, and 1 pentagon—whose areas are **all exact integers**:

  .. math::

     3,\; 3,\; 6,\; 6,\; 6,\; 9,\; 12,\; 12,\; 12,\; 12,\; 14,\; 14,\; 14,\; 21 \qquad \left(\sum = 144\right),

  investigating the combinatorial multitude of distinct ways (:eq:`17{,}152` assemblies, or :eq:`536` modulo reflections and rotations) in which commensurable polygonal figures recombine to tile the square.

* **The Cattle Problem (*Πρόβλημα βοεικόν*)** (Heath 1897, pp. 319–326; Heiberg II, 446–455): Addressed in 22 elegiac distichs to :person:`Eratosthenes <eratosthenes>` at Alexandria, asking for the number of White, Black, Dappled, and Yellow bulls and cows of the Sun satisfying seven linear ratio constraints plus two Diophantine figurate conditions (White + Black bulls = a square; Yellow + Dappled bulls = a triangular number), reducing to **Pell's equation**:

  .. math::

     t^2 - 4{,}729{,}494\, u^2 = 1,

  whose smallest positive solution yields a herd total of **206,545 decimal digits**!

----

Part III — *The Sand-Reckoner* (*Ψαμμίτης / Arenarius*)
-------------------------------------------------------

.. folio:: Heath (1897), pp. 221–232 · Heiberg II, 242–291
   :page: 221

I. Address to King Gelon & Aristarchus's Heliocentric Universe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

“There are some, :person:`king Gelon <gelon>`, who think that the number of the sand is infinite in multitude; and I mean by the sand not only that which exists about Syracuse and the rest of Sicily, but also that which is found in every region whether inhabited or uninhabited. Again there are some who, without regarding it as infinite, yet think that no number has been named which is great enough to exceed its multitude.”

To refute this belief—even for a sphere equal in size to the entire **cosmos** completely filled with finest poppy-seed sand—:person:`Archimedes <archimedes>` preserves the priceless sole surviving direct account of **:person:`Aristarchus of Samos's <aristarchus>` heliocentric system** (Heath 1897, pp. 221–222):

.. epigraph::

   “Now you are aware that ‘universe’ (*κόσμος*) is the name given by most astronomers to the sphere whose centre is the centre of the earth and whose radius is equal to the straight line between the centre of the sun and the centre of the earth. This is the common account, as you have heard from astronomers. But :person:`Aristarchus of Samos <aristarchus>` brought out a book consisting of certain hypotheses (*ὑποθέσεων γράψας*), wherein it appears, as a consequence of the assumptions made, that the universe is many times greater than the ‘universe’ just mentioned. **His hypotheses are that the fixed stars and the sun remain unmoved, that the earth revolves about the sun in the circumference of a circle, the sun lying in the middle of the orbit**, and that the sphere of the fixed stars, situated about the same centre as the sun, is so great that the circle in which he supposes the earth to revolve bears such a proportion to the distance of the fixed stars as the centre of the sphere bears to its surface.”

Interpreting Aristarchus's striking point-to-surface phrase mathematically (since a geometric point has *no* ratio to a surface, :just:`Eucl. V. Def. 4`!), Archimedes charitably models Aristarchus's proportion as:

.. math::

   (\text{Globe of Earth}) : (\text{Traditional Sun-Orbit Sphere}) = (\text{Earth-Orbit Sphere}) : (\text{Sphere of Fixed Stars}).

II. Experimental Solar Parallax & Astronomical Bounds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 223–226 · Heiberg II, 248–265
   :page: 223

Deliberately adopting *generous upper bounds* at every step so his sand-estimate stays a fortiori unassailable (Earth perimeter :eq:`< 3{,}000{,}000` stadia, ten times :person:`Eratosthenes' <eratosthenes>` measurement; solar diameter greater than the moon's, citing earlier estimates including that of **"Phidias my father"**, :person:`Φειδία δὲ τοῦ ἁμοῦ πατρός <phidias>`, who made it :eq:`12` times the moon's), Archimedes measures the apparent angular diameter :eq:`d` of the rising sun along a sighting rod with a movable cylinder, correcting for the **finite aperture of the human pupil**, and establishes:

.. math::

   \frac{90^\circ}{200} < d < \frac{90^\circ}{164}.

From this chord bound he proves geometrically that the diameter of the traditional cosmos is less than :eq:`10{,}000 = 10^4` Earth diameters (:eq:`< 10^{10}` stadia), whence the diameter of Aristarchus's sphere of fixed stars is less than :eq:`10^4 \times 10^{10} = 10^{14}` stadia!

III. The Myriad-Octad Number System & Law of Exponents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 227–232 · Heiberg II, 264–291
   :page: 227

Recalling his earlier treatise *Principles* (*Ἀρχαί*) addressed to :person:`Zeuxippus <zeuxippus>`, Archimedes constructs his recursive :term:`myriad-octad <myriad-octads>` hierarchy on base :eq:`M = 10^8` (*a myriad myriads*):

* **First Order**: numbers from :eq:`1` up to :eq:`10^8`.
* **Second Order**: taking :eq:`10^8` as unit, up to :eq:`(10^8)^2 = 10^{16}`.
* ***k*-th Order** (:eq:`1 \le k \le 10^8`): up to :eq:`10^{8k}`, culminating at the :eq:`(10^8)`-th Order in :eq:`P = (10^8)^{10^8} = 10^{800{,}000{,}000}`, which closes the **First Period**!
* **Second to Myriad-Myriadth Period**: taking :eq:`P` as the unit of the First Order of the Second Period and continuing through :eq:`10^8` Periods reaches a myriad-myriad units of the myriad-myriadth order of the myriad-myriadth period:

  .. math::

     P^{10^8} = \left(10^{8 \cdot 10^8}\right)^{10^8} = 10^{8 \cdot 10^{16}}!

To multiply across orders without overflowing language, Archimedes proves the **Law of Exponents** (Heath 1897, p. 229):

.. enunciation::

   If :eq:`A_1, A_2, A_3, \dots, A_m, \dots, A_n, \dots` be a geometric progression starting from :eq:`A_1 = 1` (specifically powers of :eq:`10`), the product :eq:`A_m \cdot A_n` equals the term :eq:`A_{m + n - 1}` whose distance from :eq:`A_n` equals the distance of :eq:`A_m` from :eq:`A_1`!

IV. Final Cosmic Sand Upper Bounds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming :eq:`\le 10{,}000` grains of sand in a poppy-seed sphere of diameter :eq:`\frac{1}{40}` finger-breadth and :eq:`1` stadium :eq:`< 10{,}000` finger-breadths, cubing diameter ratios (:just:`Eucl. XII. 18`) and applying the Law of Exponents proves:

1. **Traditional Cosmos**: Fewer than *one thousand units of the seventh order of numbers*, i.e. :eq:`< 10^{51}` grains of sand!
2. **Aristarchus's Heliocentric Sphere of Fixed Stars**: Fewer than *one thousand myriads of units of the eighth order of numbers*, i.e. :eq:`< 10^{63}` grains of sand!

“I conceive that these things, :person:`king Gelon <gelon>`, will appear incredible to the great majority of people who have not studied mathematics, but that to those who are conversant therewith and have given thought to the question of the distances and sizes of the earth and the sun and moon and the whole universe the proof will carry conviction. And it was for this reason that I thought the subject would be not inappropriate for your consideration.”

.. qed::
