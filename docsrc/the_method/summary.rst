:order: 61
:type: summary
:canonical_id: method-of-mechanical-theorems
:folio: Heath 1912, pp. 12–51 · Heiberg 1907 / II², 426–507

.. _unit-method-of-mechanical-theorems-summary:

The Method of Mechanical Theorems — Analytical Summary
======================================================

*Scope*: **Heiberg (1907 / Vol. II², pp. 426–507)** · **Heath Supplement (1912), pp. 12–51** · *Epistle to Eratosthenes, Lemmas 1–11 & Propositions 1–15*

Unveiling the Workshop of Antiquity's Greatest Geometer
-------------------------------------------------------

For over two millennia, :person:`Archimedes' <archimedes>` published treatises inspired awe and perplexity: how did he guess exact ratios like :eq:`\frac{4}{3}`, :eq:`\frac{2}{3}`, :eq:`\frac{3}{8}r`, or :eq:`(AD + 3a) : (AD + 2a)` *before* setting up his intricate double-reductio exhaustion proofs? Deciphered by :person:`J. L. Heiberg <heiberg>` in Constantinople in 1906 from the tenth-century Palimpsest (Codex C), *The Method* (:cite:`archimedes:methodus`) reveals Archimedes' private analytic engine:

1. **Cavalieri Cross-Sections + Virtual Lever (:term:`ἔφοδος <ephodion>`)**: Decompose an unknown area or solid :g:`X` and a known comparison figure :g:`Y` into one-parameter families of lower-dimensional slices :eq:`X(x), Y(x)` along axis :eq:`x \in [0, a]`. Using conic/quadric symptomata, construct a virtual lever arm :g:`H` beyond the fulcrum :g:`A` (`HA = a` or `2r`) so that :eq:`\frac{Y(x)}{X(x)} = \frac{HA}{x}`. Moving every slice :eq:`X(x)` to :g:`H` concentrates :g:`X` at a single point, balancing :g:`Y` at its known centroid :eq:`\bar{x}_Y`:

   .. math::

      a \cdot \text{Vol}(X) = \bar{x}_Y \cdot \text{Vol}(Y).

2. **Methodological Separation of Discovery and Proof**: Archimedes draws a razor-sharp philosophical boundary between **indication** (*ἔνδειξις*, summing unextended planar/linear indivisibles on a mechanical lever) and **synthetic demonstration** (*ἀπόδειξις*, rigorous Eudoxean exhaustion by finite magnitudes).

Register of Propositions 1–15 in *The Method*
---------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 12 34 54

   * - Prop.
     - Subject
     - Mechanical / Geometric Result
   * - **1**
     - Parabolic Segment Area
     - Chords balanced against :g:`\triangle CFA \implies \text{Segment} = \frac{4}{3}\triangle ABC`
   * - **2**
     - Sphere Volume & Surface Analogy
     - Sphere + Cone slices balance Cylinder :eq:`\implies V = \frac{4}{3}\pi r^3 \implies S = 4\pi r^2`
   * - **3**
     - Spheroid Cubature
     - Spheroid + Cone slices balance Cylinder :eq:`\implies \text{Spheroid} = \frac{2}{3}` cylinder
   * - **4**
     - Paraboloid Segment Cubature
     - Circular slices balance Cylinder :eq:`\implies \text{Paraboloid} = \frac{1}{2}` cylinder :eq:`= \frac{3}{2}` cone
   * - **5**
     - Paraboloid Centroid
     - Divides axis in ratio :eq:`2 : 1` from vertex (:eq:`\bar{x} = \frac{2}{3}h`)
   * - **6**
     - Hemisphere Centroid
     - Divides radius in ratio :eq:`5 : 3` from pole (:eq:`\frac{3}{8}r` from base centre)
   * - **7–10**
     - Spherical & Spheroid Segments
     - Volumes and exact axial centroids of arbitrary segments
   * - **11**
     - Hyperboloid Segment & Centroid
     - Cubature and centroid of obtuse-angled conoid
   * - **12–14**
     - **Cylindrical Ungula**
     - Triple proof (mechanical lever + parabolic prisms + exhaustion): :eq:`V = \frac{1}{6}` prism (:eq:`\frac{2}{3}r^2 h`)
   * - **15**
     - **Archimedean Bicylinder**
     - Intersection of two orthogonal cylinders in cube: :eq:`V = \frac{2}{3}` cube (:eq:`\frac{16}{3}r^3`)
