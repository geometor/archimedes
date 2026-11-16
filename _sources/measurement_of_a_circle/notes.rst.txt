:order: 12
:type: notes
:canonical_id: measurement-of-a-circle
:folio: Heath 1897, pp. lxxvii–lxxxiv, 91–98 · Heiberg I, 258–271

.. _unit-measurement-of-a-circle-notes:

Measurement of a Circle — Philological & Mathematical Notes
===========================================================

1. Textual State & Proposition Order
------------------------------------

* **Fragmentary Byzantine Recension**: As :person:`Heiberg <heiberg>` (:cite:`heiberg:1880`) and :person:`Heath <heath>` (:cite:`heath:1897`, pp. xxiv, 93) observe, our surviving Greek text of *Κύκλου μέτρησις* bears marks of a late editor or epitomator (connected with the sixth-century school of :person:`Isidore of Miletus <isidore-of-miletus>`): the Syracusan Doric dialect has been stripped in favor of Attic/Koine forms (*κύκλος*, *περιφέρεια*, *διάμετρος*), and **Proposition 2** (:eq:`\text{Circle} : d^2 \approx 11 : 14`) stands illogically *before* **Proposition 3**, upon whose bound :eq:`3\frac{1}{7}` it depends, while lacking Archimedes' characteristic inequality phrasing ("approximately" or upper/lower bounds).
* **Testimony of Heron**: :person:`Heron of Alexandria <heron>` (:cite:`heron:metrica`, I.25–26) cites Archimedes' *Measurement of a Circle* for :eq:`3\frac{10}{71} < \pi < 3\frac{1}{7}` and mentions another treatise (*On Plinthides and Cylinders*) in which Archimedes gave still closer fractional bounds, paralleled by :person:`Apollonius's <apollonius>` *Okytokion* attested by :person:`Eutocius <eutocius>` (:cite:`eutocius:in-archimedem`).

2. Origin of the Pell Approximants :eq:`265/153` and :eq:`1351/780`
-------------------------------------------------------------------

Why does Archimedes state without explanation that :eq:`\frac{265}{153} < \sqrt{3} < \frac{1351}{780}`?

* As analyzed in :cite:`heath:1897` (Introduction, Chapter IV, pp. lxxvii–lxxxiv), both fractions belong to the **convergents of the simple continued fraction** of :eq:`\sqrt{3} = [1; \overline{1, 2}]`:

  .. math::

     1, \quad \frac{2}{1}, \quad \frac{5}{3}, \quad \frac{7}{4}, \quad \frac{19}{11}, \quad \frac{26}{15}, \quad \frac{71}{41}, \quad \frac{97}{56}, \quad \mathbf{\frac{265}{153}}, \quad \frac{362}{209}, \quad \frac{989}{571}, \quad \mathbf{\frac{1351}{780}}.

* Equivalently, iterating Heron's / Babylonians' reciprocal-averaging bounds starting from :eq:`\frac{5}{3} < \sqrt{3} < \frac{7}{4}` via :eq:`\frac{3b + a}{a + b}` and :eq:`\frac{a^2 + 3b^2}{2ab}` produces :eq:`\frac{26}{15}`, then :eq:`\frac{265}{153}` (satisfying the Pell-type equation :eq:`x^2 - 3y^2 = -2`), and one step further :eq:`\frac{1351}{780}` (satisfying Pell's equation :eq:`x^2 - 3y^2 = 1`, accurate to six decimal places: :eq:`1.73205128\dots` vs. :eq:`1.73205080\dots`).
* :person:`Eutocius of Ascalon <eutocius>` (:cite:`eutocius:in-archimedem`, Heiberg Vol. III, pp. 228–261) verifies every squared mixed fraction in Greek alphabetic numerals step-by-step.

3. GEOMETOR Cross-Corpus Concordance
------------------------------------

* **Euclid & Constructive Elements** (:cite:`geometor:euclid`): Directly extends ``euclid`` XII.2 (exhaustion by inscribed bisected squares) while adding *circumscribed* polygons whose perimeters require the explicit convexity assumptions of :doc:`Unit 4 (Sphere and Cylinder I, Assump. 1–2) <../sphere_and_spirals/sphere_cylinder_i>`.
* **Exact Symbolic Field Towers** (``geometor/model`` & ``geometor/fundamentals``): Whereas the exact algebraic coordinates of the 96-gon live in the nested quadratic tower :eq:`\mathbb{Q}(\sqrt{2 + \sqrt{2 + \sqrt{2 + \sqrt{3}}}})` of degree 16, Archimedes projects each layer back onto :eq:`\mathbb{Q}` via certified rational interval enclosures—anticipating rigorous interval arithmetic by twenty-one centuries.
* **Rational Trigonometry** (:cite:`geometor:wildberger`): Notice that Archimedes' half-angle recurrence :eq:`\cot(\theta/2) = \cot\theta + \csc\theta` operates entirely on rational spread/cotangent ratios without transcendental angle measure.
