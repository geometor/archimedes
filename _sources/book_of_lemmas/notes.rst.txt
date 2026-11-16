:order: 52
:type: notes
:canonical_id: book-of-lemmas
:folio: Heath 1897, pp. xxxii, 301–318 · Heiberg II, 426–445

.. _unit-book-of-lemmas-notes:

Book of Lemmas (*Liber Assumptorum*) — Philological & Mathematical Notes
========================================================================

1. Arabic-to-Latin Transmission (*Kitāb al-Maʾkhūdhāt* → Florence 1661)
-----------------------------------------------------------------------

No Greek manuscript of the *Book of Lemmas* survives. Its preservation is owed to ninth-century Baghdad geometer :person:`Thābit ibn Qurra <thabit-ibn-qurra>` (836–901 AD), whose Arabic translation (*Kitāb al-Maʾkhūdhāt li-Arshimīdis*) was commented upon in the tenth century by Abū al-Ḥasan ʿAlī ibn Aḥmad al-Nasawī ("Almochtasso"). In 1661, :person:`Abraham Ecchellensis and Giovanni Alfonso Borelli <borelli>` discovered an Arabic codex in the Laurentian Medici Library at Florence and published the Latin *editio princeps* (:cite:`ecchellensis-borelli:1661`), later re-edited by :person:`Heiberg <heiberg>` (:cite:`heiberg:1881`, Vol. II, pp. 426–445; 2nd ed. pp. 510–525).

Why does the text say in Props. 4 and 14 *"what Archimedes called an arbelos"* and *"which Archimedes calls a salinon"*? As :person:`Heath <heath>` (:cite:`heath:1897`, pp. xxxii, 301) explains, a late Greek or Arabic compiler gathered genuinely Archimedean theorems—attested independently by :person:`Pappus <pappus>` (:cite:`pappus:synagoge:iv`, IV.14–18 on the *arbelos* and IV.36 on *neusis* trisection)—into a handbook of planar lemmas, adding third-person glosses on Archimedes' picturesque Syracusan names.

2. GEOMETOR Cross-Corpus Concordance
------------------------------------

* **Euclid (`geometor/euclid`)** (:cite:`geometor:euclid`): Resolves ``archimedes:liber-assumptorum`` cited in Heath's *Euclid* on III.31/III.35, IV.10–11, VI.33 (angle trisection), and XIII.9 (golden section).
* **Pappus (`geometor/pappus`)** (:cite:`geometor:pappus`, :cite:`pappus:synagoge:iv`): **Propositions 1, 4, 5, 6** form the direct foundation of *Synagoge* IV.14–20 (the infinite Steiner/Pappus circle chain in the *arbelos*, effortlessly proved today by circle inversion centered at :g:`A` or :g:`B`), while **Proposition 12** is an early synthetic proof of the **polar-orthocenter theorem** for cyclic quadrilaterals inscribed in a semicircle!
* **Divine Proportion (`geometor/divine` & `geometor/elements`)**: **Proposition 15** connects the regular pentagon and decagon directly to :just:`Euclid XIII. 9` over the golden number field :eq:`\mathbb{Q}(\phi)`.
* **Rational Trigonometry (`geometor/wildberger`)** (:cite:`geometor:wildberger`): **Proposition 11** (:eq:`Q(A,O) + Q(B,O) + Q(C,O) + Q(D,O) = 4R^2`) and the rational twin-circle harmonic mean :eq:`d = \frac{d_1 d_2}{d_1 + d_2}` in **Proposition 5** are pure polynomial identities over :eq:`\mathbb{Q}` requiring zero square roots!
