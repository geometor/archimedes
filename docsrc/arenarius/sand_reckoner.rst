:canonical_id: AREN
:order: 3
:type: section

Part III: The Sand-Reckoner (Arenarius)
=======================================

.. folio:: Heath (1897), pp. 221–232 · Heiberg II, 242–291
   :page: 221

I. Address to King Gelon & Aristarchus's Heliocentric Universe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

“There are some, :person:`king Gelon <gelon>`, who think that the number of the sand is infinite in multitude; and I mean by the sand not only that which exists about Syracuse and the rest of Sicily, but also that which is found in every region whether inhabited or uninhabited. Again there are some who, without regarding it as infinite, yet think that no number has been named which is great enough to exceed its multitude.”

To refute this belief—even for a sphere equal in size to the entire **cosmos** completely filled with finest poppy-seed sand—I shall first set down the account of **:person:`Aristarchus of Samos <aristarchus>`** (Heath 1897, pp. 221–222):

.. epigraph::

   “Now you are aware that ‘universe’ (*κόσμος*) is the name given by most astronomers to the sphere whose centre is the centre of the earth and whose radius is equal to the straight line between the centre of the sun and the centre of the earth. This is the common account, as you have heard from astronomers. But :person:`Aristarchus of Samos <aristarchus>` brought out a book consisting of certain hypotheses (*ὑποθέσεων γράψας*), wherein it appears, as a consequence of the assumptions made, that the universe is many times greater than the ‘universe’ just mentioned. **His hypotheses are that the fixed stars and the sun remain unmoved, that the earth revolves about the sun in the circumference of a circle, the sun lying in the middle of the orbit**, and that the sphere of the fixed stars, situated about the same centre as the sun, is so great that the circle in which he supposes the earth to revolve bears such a proportion to the distance of the fixed stars as the centre of the sphere bears to its surface.”

Since a geometric point has no magnitude and therefore no ratio to a surface (:just:`Eucl. V. Def. 4`), we take Aristarchus's meaning to be this proportion:

.. math::

   (\text{Globe of Earth}) : (\text{Traditional Sun-Orbit Sphere}) = (\text{Earth-Orbit Sphere}) : (\text{Sphere of Fixed Stars}).

II. Experimental Solar Parallax & Astronomical Bounds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 223–226 · Heiberg II, 248–265
   :page: 223

Assuming *generous upper bounds* at every step so that the estimate remains unassailable—taking the perimeter of the earth to be :eq:`< 3{,}000{,}000` stadia (ten times the measurement of earlier astronomers such as :person:`Eratosthenes <eratosthenes>`), and the diameter of the sun greater than that of the moon (recalling earlier estimates including that of **"Phidias my father"**, :person:`Φειδία δὲ τοῦ ἁμοῦ πατρός <phidias>`, who made it :eq:`12` times the moon's)—I measure the apparent angular diameter :eq:`d` of the rising sun along a sighting rod fitted with a movable cylinder, correcting for the **finite aperture of the pupil**, and establish:

.. math::

   \frac{90^\circ}{200} < d < \frac{90^\circ}{164}.

From this chord bound it follows geometrically that the diameter of the traditional cosmos is less than :eq:`10{,}000 = 10^4` Earth diameters (:eq:`< 10^{10}` stadia), whence the diameter of Aristarchus's sphere of fixed stars is less than :eq:`10^4 \times 10^{10} = 10^{14}` stadia.

III. The Myriad-Octad Number System & Law of Exponents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. folio:: Heath (1897), pp. 227–232 · Heiberg II, 264–291
   :page: 227

As I have set forth in the books addressed to :person:`Zeuxippus <zeuxippus>` (*Principles*, *Ἀρχαί*), let us construct a recursive :term:`myriad-octad <myriad-octads>` hierarchy on base :eq:`M = 10^8` (*a myriad myriads*):

* **First Order**: numbers from :eq:`1` up to :eq:`10^8`.
* **Second Order**: taking :eq:`10^8` as unit, up to :eq:`(10^8)^2 = 10^{16}`.
* ***k*-th Order** (:eq:`1 \le k \le 10^8`): up to :eq:`10^{8k}`, culminating at the :eq:`(10^8)`-th Order in :eq:`P = (10^8)^{10^8} = 10^{800{,}000{,}000}`, which closes the **First Period**!
* **Second to Myriad-Myriadth Period**: taking :eq:`P` as the unit of the First Order of the Second Period and continuing through :eq:`10^8` Periods reaches a myriad-myriad units of the myriad-myriadth order of the myriad-myriadth period:

  .. math::

     P^{10^8} = \left(10^{8 \cdot 10^8}\right)^{10^8} = 10^{8 \cdot 10^{16}}!

To multiply across orders, the following **Law of Exponents** holds (Heath 1897, p. 229):

.. enunciation::

   If :eq:`A_1, A_2, A_3, \dots, A_m, \dots, A_n, \dots` be a geometric progression starting from :eq:`A_1 = 1` (specifically powers of :eq:`10`), the product :eq:`A_m \cdot A_n` equals the term :eq:`A_{m + n - 1}` whose distance from :eq:`A_n` equals the distance of :eq:`A_m` from :eq:`A_1`!

IV. Final Cosmic Sand Upper Bounds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming :eq:`\le 10{,}000` grains of sand in a poppy-seed sphere of diameter :eq:`\frac{1}{40}` finger-breadth and :eq:`1` stadium :eq:`< 10{,}000` finger-breadths, cubing diameter ratios (:just:`Eucl. XII. 18`) and applying the Law of Exponents proves:

1. **Traditional Cosmos**: Fewer than *one thousand units of the seventh order of numbers*, i.e. :eq:`< 10^{51}` grains of sand!
2. **Aristarchus's Heliocentric Sphere of Fixed Stars**: Fewer than *one thousand myriads of units of the eighth order of numbers*, i.e. :eq:`< 10^{63}` grains of sand!

“I conceive that these things, :person:`king Gelon <gelon>`, will appear incredible to the great majority of people who have not studied mathematics, but that to those who are conversant therewith and have given thought to the question of the distances and sizes of the earth and the sun and moon and the whole universe the proof will carry conviction. And it was for this reason that I thought the subject would be not inappropriate for your consideration.”

.. qed::
