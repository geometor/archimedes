:canonical_id: SOL
:order: 1
:type: section

Part I: The Thirteen Archimedean Semi-Regular Solids (Pappus V.19)
==================================================================

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
