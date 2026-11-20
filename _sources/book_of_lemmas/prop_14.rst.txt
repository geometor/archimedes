:canonical_id: LA.14
:order: 14
:type: proposition

.. _lemmas-salinon:

Proposition 14: The Salinon (‘Salt-Cellar’)
===========================================

.. folio:: Heath (1897), pp. 316–318 · Heiberg II, 442–445
   :page: 316

.. enunciation::

   **Proposition 14 (The Salinon / ‘Salt-Cellar’).** Let :g:`ACB` be a semicircle on :g:`AB` as diameter, and let :g:`AD`, :g:`BE` be equal lengths measured along :g:`AB` from :g:`A`, :g:`B` respectively. On :g:`AD`, :g:`BE` as diameters describe semicircles on the side towards :g:`C`, and on :g:`DE` as diameter a semicircle on the opposite side. Let the perpendicular to :g:`AB` through :g:`O`, the centre of the first semicircle, meet the opposite semicircles in :g:`C`, :g:`F` respectively. Then shall the area of the figure bounded by the circumferences of all the semicircles (‘which Archimedes calls a :term:`σάλινον <salinon>`’) be **equal to the area of the circle whose diameter is** :g:`CF`.

.. picture:: /_static/figures/fig_salinon.svg
   :caption: Book of Lemmas, Proposition 14 — Archimedes' Salinon Bounded by Four Semicircles Equals the Circle on Symmetry Axis CF

*Proof*: Because :eq:`OA = \frac{1}{2}AB`, :eq:`AD` is the diameter of each lateral semicircle, and :eq:`OF = \frac{1}{2}DE`, we have :eq:`CF = OC + OF = \frac{1}{2}(AB + DE) = AD + DE = AE`. Squaring gives :eq:`AB^2 + DE^2 - 2\cdot AD^2 = (2\cdot OA)^2 + (2\cdot OF)^2 - 2(OA - OF)^2 = 2(OA + OF)^2 = 2\cdot CF^2`. Converting diameters-squared into semicircles via :just:`Eucl. XII. 2` shows that :eq:`\text{Semicircle}(AB) + \text{Semicircle}(DE) - 2\cdot\text{Semicircle}(AD) = 2\cdot\text{Semicircle}(CF) = \text{Circle}(CF)`!

.. qed::
