:canonical_id: QP.23
:order: 24
:type: proposition

Proposition 23: Exact Finite Geometric Series Identity (1/4^n)
==============================================================

.. folio:: Heath (1897), pp. 246–252 · Heiberg II, 336–353
   :page: 250

.. enunciation::

   **Proposition 23 (Exact Finite Geometric Series Identity).** Given a series of areas :g:`A, B, C, D, \dots, Z`, of which :g:`A` is the greatest, and each is equal to four times the next in order, then:

   .. math::

      A + B + C + D + \dots + Z + \frac{1}{3} Z = \frac{4}{3} A.

*Proof*: Add :eq:`b = \frac{1}{3}B`, :eq:`c = \frac{1}{3}C`, ..., :eq:`z = \frac{1}{3}Z`. Since :eq:`B + b = \frac{4}{3}B = \frac{1}{3}A`, :eq:`C + c = \frac{1}{3}B`, ..., :eq:`Z + z = \frac{1}{3}Y`, summing all terms gives :eq:`(A + B + \dots + Z) + (b + c + \dots + z) = A + \frac{1}{3}(A + B + \dots + Y)`. Subtracting :eq:`b + c + \dots + y = \frac{1}{3}(B + C + \dots + Y)` from both sides leaves :eq:`A + B + \dots + Z + \frac{1}{3}Z = A + \frac{1}{3}A = \frac{4}{3}A`!

.. qed::
