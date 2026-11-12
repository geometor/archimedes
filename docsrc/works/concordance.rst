:order: 90
:type: apparatus

.. _works-concordance:

Heiberg–Heath–GEOMETOR Concordance
==================================

Master cross-reference of Archimedes' *Opera Omnia* across :person:`Johan Ludvig Heiberg <heiberg>`'s
critical Teubner editions (:cite:`heiberg:1880`, :cite:`heiberg:1881`),
:person:`Sir Thomas Little Heath <heath>`'s Cambridge editions (:cite:`heath:1897`, :cite:`heath:1912`),
and the constructive & philosophical codices of the GEOMETOR Digital Scriptorium.

Seven-Unit Codex Architecture
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 8 28 32 32

   * - Unit
     - Treatise Unit
     - Heiberg Teubner Locus
     - Heath Cambridge Locus
   * - **Unit 1**
     - :doc:`Measurement of a Circle <measurement-of-a-circle-en>` (*Κύκλου μέτρησις (Dimensio Circuli)*)
     - Vol. I (1880), pp. 256–271; 2nd ed. (1910), pp. 232–243
     - Heath (1897), pp. 91–98
   * - **Unit 2**
     - :doc:`On the Equilibrium of Planes, Books I & II <equilibrium-of-planes-en>` (*Ἐπιπέδων ἰσορροπιῶν αʹ βʹ (De Planorum Aequilibriis)*)
     - Vol. II (1881), pp. 142–241; 2nd ed. (1913), pp. 124–213
     - Heath (1897), Book I pp. 189–202; Book II pp. 203–220
   * - **Unit 3**
     - :doc:`Quadrature of the Parabola <quadrature-of-parabola-en>` (*Τετραγωνισμὸς παραβολῆς (Quadratura Parabolae)*)
     - Vol. II (1881), pp. 294–353; 2nd ed. (1913), pp. 262–315
     - Heath (1897), pp. 233–252
   * - **Unit 4**
     - :doc:`On the Sphere and Cylinder, On Spirals & On Conoids and Spheroids <sphere-spirals-conoids-en>` (*Περὶ σφαίρας καὶ κυλίνδρου · Περὶ ἑλίκων · Περὶ κωνοειδέων καὶ σφαιροειδέων*)
     - Vol. I (1880), pp. 1–255, 272–499; Vol. II (1881), pp. 1–141
     - Heath (1897), pp. 1–90, 99–188
   * - **Unit 5**
     - :doc:`Book of Lemmas (Liber Assumptorum) <book-of-lemmas-en>` (*Liber Assumptorum (Kitāb al-Maʾkhūdhāt, tr. Thābit ibn Qurra)*)
     - Vol. II (1881), pp. 426–445; 2nd ed. (1913), pp. 510–525
     - Heath (1897), pp. 301–318
   * - **Unit 6**
     - :doc:`The Method of Mechanical Theorems Addressed to Eratosthenes <method-of-mechanical-theorems-en>` (*Περὶ τῶν μηχανικῶν θεωρημάτων πρὸς Ἐρατοσθένην ἔφοδος (Methodus)*)
     - Hermes 42 (1907), pp. 243–297; Opera Omnia Vol. II, 2nd ed. (1913), pp. 426–507
     - Heath (1912 Supplement), pp. 12–51
   * - **Unit 7**
     - :doc:`The Thirteen Semi-Regular Solids, Stomachion & The Sand-Reckoner <semi-regular-solids-arenarius-en>` (*Τρισκαίδεκα ἡμικανονικὰ στερεά (Pappus V.19) · Στομάχιον · Ψαμμίτης (Arenarius)*)
     - Pappus ed. Hultsch I (1876), pp. 350–358; Heiberg II (1881), pp. 242–293; 2nd ed. (1913), pp. 216–259, 416–424
     - Heath (1897), pp. xxxvi, 221–232; Pappus V.19 Concordance

Canonical Proposition & Ecosystem Concordance
---------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 12 22 18 16 32

   * - Locus ID
     - Treatise & Proposition
     - Heiberg / Heath
     - Theorem Summary
     - GEOMETOR Ecosystem Links
   * - ``DC.1``
     - :doc:`Measurement of a Circle (Prop. 1) <measurement-of-a-circle-en>`
     - Heiberg I, 258–261 (2nd ed. I, 232–235); Heath 1897, pp. 91–93
     - Area of any circle equals a right-angled triangle with legs r and C
     - **euclid**: XII.2, X.1; **elements**: Polygonal exhaustion & circle quadrature reduction; **wildberger**: Rational polygon bounding of circular area
   * - ``DC.2``
     - :doc:`Measurement of a Circle (Prop. 2) <measurement-of-a-circle-en>`
     - Heiberg I, 260–263 (2nd ed. I, 234–237); Heath 1897, p. 93
     - Ratio of circle area to square on diameter is approximately 11 : 14
     - **euclid**: XII.2; **wildberger**: Rational area approximation 11/14
   * - ``DC.3``
     - :doc:`Measurement of a Circle (Prop. 3) <measurement-of-a-circle-en>`
     - Heiberg I, 262–271 (2nd ed. I, 236–243); Heath 1897, pp. 93–98
     - Circumference-to-diameter bounds: 3 10/71 < π < 3 1/7 via 96-gons and rational √3 bounds (265/153 < √3 < 1351/780)
     - **euclid**: I.47, VI.3; **elements**: Bisection recurrence on cot(θ/2) = cot θ + csc θ; **wildberger**: Pell-type rational convergents to √3 (x² - 3y² = ±1, -2)
   * - ``EP.I.Post.1-7``
     - :doc:`On the Equilibrium of Planes I (Postulates 1–7) <equilibrium-of-planes-en>`
     - Heiberg II, 142–145 (2nd ed. II, 124–125); Heath 1897, pp. 189–190
     - Seven axiomatic postulates of static balance, symmetry, superposition, and convexity of the center of gravity
     - **etc**: Axiomatic foundation of homogeneous barycentric coordinates; **hilbert**: Axiomatization of statics parallel to geometric incidence/congruence
   * - ``EP.I.6-7``
     - :doc:`On the Equilibrium of Planes I (Props. 6 & 7) <equilibrium-of-planes-en>`
     - Heiberg II, 152–159 (2nd ed. II, 132–139); Heath 1897, pp. 192–194
     - Law of the Lever: commensurable (I.6) and incommensurable (I.7) magnitudes balance at distances reciprocally proportional to weights
     - **euclid**: V.Def.4, V.Def.5; **pappus**: Synagoge VIII (centers of gravity); **etc**: Weighted barycentric division (w₁ : w₂)
   * - ``EP.I.9-10``
     - :doc:`On the Equilibrium of Planes I (Props. 9 & 10) <equilibrium-of-planes-en>`
     - Heiberg II, 162–169 (2nd ed. II, 140–147); Heath 1897, pp. 195–198
     - Center of gravity of any parallelogram lies at the intersection of its diagonals
     - **euclid**: I.34; **elements**: Midpoint concurrency of parallelogram diagonals
   * - ``EP.I.13-14``
     - :doc:`On the Equilibrium of Planes I (Props. 13 & 14) <equilibrium-of-planes-en>`
     - Heiberg II, 172–183 (2nd ed. II, 150–159); Heath 1897, pp. 198–201
     - Center of gravity of any triangle lies on each median (I.13) and at the concurrency of medians (I.14) — Kimberling X(2)
     - **etc**: X(2) Centroid — barycentric (1 : 1 : 1), trilinear (bc : ca : ab); **euclid**: VI.2, VI.4; **pappus**: Synagoge VIII centroid theorems
   * - ``EP.I.15``
     - :doc:`On the Equilibrium of Planes I (Prop. 15) <equilibrium-of-planes-en>`
     - Heiberg II, 182–187 (2nd ed. II, 158–163); Heath 1897, pp. 201–202
     - Center of gravity of a trapezium divides the segment joining midpoints of parallel sides in ratio (2b + a) : (2a + b)
     - **etc**: Barycentric decomposition of quadrilaterals into triangles
   * - ``EP.II.8-10``
     - :doc:`On the Equilibrium of Planes II (Props. 8–10) <equilibrium-of-planes-en>`
     - Heiberg II, 208–241 (2nd ed. II, 182–213); Heath 1897, pp. 208–220
     - Center of gravity of any parabolic segment divides its diameter in ratio 3 : 2 from the vertex (and frustum centroid)
     - **pappus**: Pappus–Guldin centroid foundations
   * - ``QP.Pref``
     - :doc:`Quadrature of the Parabola (Letter to Dositheus) <quadrature-of-parabola-en>`
     - Heiberg II, 294–297 (2nd ed. II, 262–265); Heath 1897, pp. 233–235
     - Mourning Conon of Samos, statement of Archimedes' Lemma, and announcement of mechanical + geometric quadrature
     - **euclid**: X.1, XII.2, XII.10; **hilbert**: Axiom V 1 (Archimedes' Axiom)
   * - ``QP.6-17``
     - :doc:`Quadrature of the Parabola (Props. 6–17) <quadrature-of-parabola-en>`
     - Heiberg II, 304–335 (2nd ed. II, 272–299); Heath 1897, pp. 238–246
     - Mechanical exhaustion via trapezium lever bounds proving parabolic segment = 4/3 of inscribed triangle
     - **etc**: Triangle & trapezium centroids applied to conic quadrature
   * - ``QP.18-24``
     - :doc:`Quadrature of the Parabola (Props. 18–24) <quadrature-of-parabola-en>`
     - Heiberg II, 336–353 (2nd ed. II, 300–315); Heath 1897, pp. 246–252
     - Pure geometric exhaustion via triangle tree (each tier = 1/4 previous) and exact finite identity A + B + ... + Z + Z/3 = 4A/3
     - **euclid**: IX.35, X.1; **wildberger**: Exact algebraic quadrature of parabola without limits
   * - ``SC.I.Assump.1-5``
     - :doc:`On the Sphere and Cylinder I (Defs. 1–6 & Assumptions 1–5) <sphere-spirals-conoids-en>`
     - Heiberg I, 2–11 (2nd ed. I, 2–9); Heath 1897, pp. 1–4
     - Straight line as shortest path, curves/surfaces concave in the same direction (convexity), and Archimedes' Lemma
     - **proclus**: Friedlein p. 110 (straight line shortest path); **hilbert**: Grundlagen Axiom V 1 (Archimedes' Axiom)
   * - ``SC.I.33-34``
     - :doc:`On the Sphere and Cylinder I (Props. 33, 34 & Corollary (Tomb Theorem)) <sphere-spirals-conoids-en>`
     - Heiberg I, 134–147 (2nd ed. I, 120–131); Heath 1897, pp. 39–44
     - Surface of sphere = 4 great circles; volume = 4 cones; circumscribed cylinder is 3/2 of sphere in both volume and total surface
     - **euclid**: XII.10, XII.18; **pacioli**: Sacred invariant 3 : 2 of Archimedes' Syracuse tomb
   * - ``SC.I.42-43``
     - :doc:`On the Sphere and Cylinder I (Props. 42 & 43) <sphere-spirals-conoids-en>`
     - Heiberg I, 172–181 (2nd ed. I, 152–161); Heath 1897, pp. 51–53
     - Surface of any spherical segment equals the circle whose radius is the chord from vertex of segment to base rim
     - **euclid**: I.47, VI.8
   * - ``SC.II.2-4``
     - :doc:`On the Sphere and Cylinder II (Props. 2 & 4) <sphere-spirals-conoids-en>`
     - Heiberg I, 194–223 (2nd ed. I, 170–195); Eutocius III, 130–176; Heath 1897, pp. 59–79
     - Volume of spherical segment (II.2) and cutting a sphere in a given ratio via cubic equation x²(a - x) = b c² preserved by Eutocius (II.4)
     - **euclid**: XI.34, XII.10; **pappus**: Solid problems solvable by intersection of parabola and hyperbola
   * - ``SP.18-20``
     - :doc:`On Spirals (Props. 18–20) <sphere-spirals-conoids-en>`
     - Heiberg II, 62–83 (2nd ed. II, 56–75); Heath 1897, pp. 171–176
     - Polar subtangent to the Archimedean spiral r = aθ rectified to circumference 2πr of the first circle
     - **pappus**: Synagoge IV.21–25 (kinematic classification of curves)
   * - ``SP.24``
     - :doc:`On Spirals (Prop. 24) <sphere-spirals-conoids-en>`
     - Heiberg II, 94–101 (2nd ed. II, 84–91); Heath 1897, pp. 178–180
     - Area bounded by first turn of spiral and initial ray equals 1/3 of the first circle (via Σ k² bounds in Prop. 10)
     - **euclid**: XII.2, XII.10; **wildberger**: Discrete sum of squares 3(1² + ... + n²) = n(n+1)(2n+1)/2
   * - ``CS.21-32``
     - :doc:`On Conoids and Spheroids (Props. 21–32) <sphere-spirals-conoids-en>`
     - Heiberg I, 378–499 (2nd ed. I, 342–445); Heath 1897, pp. 111–150
     - Ellipse area = πab (Prop. 4); paraboloid segment = 3/2 inscribed cone (Props. 21–22); hyperboloid & spheroid segments (Props. 25–32)
     - **euclid**: XII.10, XII.12
   * - ``LA.1-3``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Props. 1–3) <book-of-lemmas-en>`
     - Heiberg II, 428–431 (2nd ed. II, 510–513); Heath 1897, pp. 301–304
     - Homothetic collinearity on tangent circles (Prop. 1), semicircle tangent bisection (Prop. 2), and chord half-angle identity (Prop. 3)
     - **euclid**: III.31, VI.2; **pappus**: Synagoge IV.14
   * - ``LA.4``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Prop. 4) <book-of-lemmas-en>`
     - Heiberg II, 430–432 (2nd ed. II, 513–514); Heath 1897, pp. 304–305
     - Area of the Arbelos (shoemaker's knife) equals the circle on the internal perpendicular tangent PN
     - **euclid**: II.4, III.31, XII.2; **elements**: Exact circle-area cancellation (r₁+r₂)² - r₁² - r₂² = 2r₁r₂
   * - ``LA.5``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Prop. 5) <book-of-lemmas-en>`
     - Heiberg II, 432–435 (2nd ed. II, 514–516); Heath 1897, pp. 305–307
     - Archimedes' Twin Circles in the partitioned Arbelos have equal diameter d = AC·CB / AB = r₁r₂/(r₁+r₂)·2
     - **pappus**: Synagoge IV (p. 230 Hultsch); **wildberger**: Harmonic radius invariant 1/r = 1/r₁ + 1/r₂
   * - ``LA.6``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Prop. 6) <book-of-lemmas-en>`
     - Heiberg II, 435–438 (2nd ed. II, 516–519); Heath 1897, pp. 307–309
     - Circle inscribed in the Arbelos touching all three semicircles has diameter ratio λ : (1 + λ + λ²) (6/19 for 3:2) & Pappus chain c_n = n·d_n
     - **pappus**: Synagoge IV.14–18 ('ancient proposition' on arbelos circle chain); **wildberger**: Descartes–Soddy rational curvature relation
   * - ``LA.8``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Prop. 8) <book-of-lemmas-en>`
     - Heiberg II, 439 (2nd ed. II, 519–520); Heath 1897, pp. 309–310
     - Angle Trisection by Neusis: inserting segment BC = r outside circle on secant through center O yields ∠AEB = (1/3)∠AOB
     - **euclid**: I.5, I.32; **pappus**: Synagoge IV.36–44 (classification of plane, solid & neusis trisections)
   * - ``LA.9-13``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Props. 9–13) <book-of-lemmas-en>`
     - Heiberg II, 439–443 (2nd ed. II, 520–523); Heath 1897, pp. 310–316
     - Orthogonal chords quadrance identity AO² + BO² + CO² + DO² = 4R² (Prop. 11) and polar orthocenter reciprocity (Prop. 12)
     - **wildberger**: Pure quadrance invariant Q₁ + Q₂ + Q₃ + Q₄ = D²; **pappus**: Pole-polar reciprocity & Apollonius On Contacts
   * - ``LA.14``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Prop. 14) <book-of-lemmas-en>`
     - Heiberg II, 443–444 (2nd ed. II, 523–524); Heath 1897, pp. 316–317
     - Area of the Salinon (salt-cellar) bounded by four symmetric semicircles equals the circle on axial segment CF
     - **euclid**: II.10, XII.2
   * - ``LA.15``
     - :doc:`Book of Lemmas (Liber Assumptorum) (Prop. 15) <book-of-lemmas-en>`
     - Heiberg II, 444–445 (2nd ed. II, 524–525); Heath 1897, pp. 317–318
     - Regular pentagon & decagon chord-secant configuration cutting EC in extreme and mean ratio (golden section φ) with EM = radius
     - **euclid**: XIII.9, XIII.10; **divine**: Golden section φ = (1 + √5)/2 in pentagon-decagon secants; **pacioli**: Divine proportion in regular pentagon/decagon
   * - ``METH.Pref``
     - :doc:`The Method of Mechanical Theorems (Letter to Eratosthenes & Lemmas 1–11) <method-of-mechanical-theorems-en>`
     - Heiberg Hermes 42, 243–247; II (2nd ed.), 426–434; Heath 1912, pp. 12–15
     - Distinction between mechanical heuristic indication (ἔφοδος) and synthetic proof; tribute to Democritus & Eudoxus on cone = 1/3 cylinder
     - **euclid**: XII.7, XII.10; **aristotle**: Distinction between hoti (indication) and dioti (demonstrative proof)
   * - ``METH.1-2``
     - :doc:`The Method of Mechanical Theorems (Props. 1 & 2) <method-of-mechanical-theorems-en>`
     - Heiberg II (2nd ed.), 434–446; Heath 1912, pp. 15–21
     - Mechanical slice-balancing of parabolic segment (Prop. 1: 4/3 ΔABC) and sphere + cone against cylinder (Prop. 2: V = (4/3)πr³ → S = 4πr²)
     - **etc**: Triangle centroid W dividing median 2 : 1 (CK = 3KW) as fulcrum ratio
   * - ``METH.3-11``
     - :doc:`The Method of Mechanical Theorems (Props. 3–11) <method-of-mechanical-theorems-en>`
     - Heiberg II (2nd ed.), 446–484; Heath 1912, pp. 21–38
     - Mechanical discovery of volumes and centers of gravity of spheroids, paraboloids, hyperboloids, and spherical segments
     - **pappus**: Synagoge VIII solid centroids
   * - ``METH.12-15``
     - :doc:`The Method of Mechanical Theorems (Props. 12–15) <method-of-mechanical-theorems-en>`
     - Heiberg II (2nd ed.), 484–507; Heath 1912, pp. 38–51
     - Cubature of curved solids equal to rectilinear polyhedra: cylindrical ungula = 1/6 prism (Props. 12–14) & bicylinder = 2/3 cube (Prop. 15)
     - **heron**: Metrica citation of Archimedes' Method on ungula and bicylinder
   * - ``SOL.1-13``
     - :doc:`Thirteen Semi-Regular Solids (via Pappus Synagoge V.19) (Pappus V.19 (Solids I–XIII)) <semi-regular-solids-arenarius-en>`
     - Heiberg Pappus ed. Hultsch I (1876), 350–358; Heiberg II (2nd ed.), 535–537; Heath 1897, p. xxxvi
     - Complete census of the 13 convex vertex-transitive non-Platonic polyhedra (8, 14, 14, 14, 26, 26, 38, 32, 32, 32, 62, 62, 92 faces)
     - **euclid**: XIII.13–18 (Five Platonic Solids); **pappus**: Synagoge V.19 face-species enumeration; **pacioli**: De Divina Proportione abscised & elevated golden polyhedra; **divine**: Icosidodecahedron, truncated icosahedron & snub dodecahedron over Q(φ)
   * - ``STOM.1``
     - :doc:`Stomachion (Loculus Archimedius) (Palimpsest Fragment & Arabic Dissection) <semi-regular-solids-arenarius-en>`
     - Heiberg II (2nd ed., 1913), 416–424; Heath 1912 Intro, p. 7
     - Fourteen-tile rational areal dissection of the 12 × 12 square (536 distinct modulo-symmetry assemblies)
     - **wildberger**: Rational lattice dissection & commensurable triangle areas
   * - ``AREN.1-4``
     - :doc:`The Sand-Reckoner (Arenarius) (Sections I–IV) <semi-regular-solids-arenarius-en>`
     - Heiberg II, 242–293 (2nd ed. II, 216–259); Heath 1897, pp. 221–232
     - Aristarchus's heliocentric cosmos, solar angular diameter bounds (90°/200 < d < 90°/164), myriad-octad exponents up to 10^(8·10^16), and < 10^63 (10^51 common) cosmic sand bound
     - **euclid**: IX.8–9 (geometric progressions & law of exponents)
