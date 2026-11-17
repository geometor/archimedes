:navigation: header
:order: 20
:nav_title: Usage

.. _archimedes-usage:

==================
Using This Edition
==================

.. rubric:: Interactive Reader's Guide to the Digital Scriptorium Edition of Archimedes

Welcome to the GEOMETOR critical edition of **The Works and Method of Archimedes**. This digital edition is designed for deep mathematical reading, philological comparison, and algorithmic synthesis. Below are the key interactive features available throughout the site.

1. Synchronized Reading Tracks
------------------------------

Every treatise unit in the Book Codex provides three synchronized reading tracks accessible directly from the book header navigation bar:

* **English (Primary Translation)**: Folio-anchored English translation based on Sir Thomas Little Heath's landmark Cambridge editions (:cite:`heath:1897`, :cite:`heath:1912`), featuring complete synthetic demonstrations, modern mathematical notation, and 11 calibrated vector plates.
* **Summary (Deductive Architecture)**: Theorem statements, proposition dependency tables, given-to-determined matrices, and geometric invariants for rapid structural review.
* **Notes (Scholarly Commentary)**: Syracusan Doric and Hellenistic Koine philology, commentary from Eutocius of Ascalon, collation notes against Johan Ludvig Heiberg's Teubner text (:cite:`heiberg:1880`, :cite:`heiberg:1881`), and cross-corpus links across the GEOMETOR ecosystem.

Use the track switcher in the chapter header bar to toggle seamlessly between perspectives while preserving your reading position.

2. Primary-Source Folio Milestones
----------------------------------

Every proposition and major textual milestone is tethered to primary archival witnesses:

* **Marginal Folio Badges**: Marginal milestone pills (e.g., ``[p. 91]``, ``[p. 233]``) link directly to high-resolution page scans of Heath's 1897 *Works* and 1912 *Method* supplement hosted on the Internet Archive.
* **Header Folio Indicator**: The top metadata bar identifies the active archival volume, page range, and corresponding Heiberg Teubner locus (*Archimedis Opera Omnia*, Vols. I–III).

3. Interactive Diagrams & Deductive Links
-----------------------------------------

The edition features 11 calibrated, theme-adaptive ``.euclid-graphic`` SVG vector plates:

* **Geometric Hover Cards (``:g:``)**: Hovering over or clicking a geometric symbol (e.g., point, line, tangent, or segment) highlights the corresponding element in the vector plate and displays coordinate and definition tooltips.
* **Equations & Formulas (``:eq:``)**: Mathematical assertions display formatted LaTeX typography with interactive term explanations.
* **Justifications (``:just:``)**: Proof steps cite prior propositions from Euclid's *Elements* or earlier Archimedean theorems, providing direct cross-references.

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The global search box in the sidebar provides instantaneous full-text search across all seven treatise units, apparatus tables, and commentary:

* Search queries automatically append `?highlight=` parameters to destination URLs.
* Matched terms are highlighted in yellow directly within the proposition body and scholia for immediate visual discovery.

5. Categories, Tags & Collection Views
--------------------------------------

Document collections throughout the site (such as the :doc:`Development & Curation Log <../log/index>`) support rich viewing modes:

* **Cards View**: Grid of article summaries with metadata badges and timestamps.
* **Banners View**: Wide banner presentation suitable for reading extended summaries.
* **List View**: Dense tabular listing for fast scanning.
* **Taxonomy Facets**: Filter by topic tags (e.g., `mechanics`, `quadrature`, `exhaustion`, `palimpsest`).

6. People, Bibliography & Glossary Tooltips
-------------------------------------------

* **People (``:person:``)**: Historical figures (such as :person:`Archimedes of Syracuse <archimedes>`, :person:`Sir Thomas Little Heath <heath>`, :person:`Johan Ludvig Heiberg <heiberg>`, and :person:`Eratosthenes of Cyrene <eratosthenes>`) display rich biographical hover cards and link to the :doc:`People Register <../people/index>`.
* **Citations (``:cite:``)**: Inline citations link to authoritative editions in the :doc:`Bibliography <../bibliography>`.
* **Technical Terms (``:term:``)**: Classical mathematical terms (such as *exhaustion*, *arbelos*, *salinon*, *neusis*, and *center of gravity*) link directly to entries in the :doc:`Technical Glossary <../glossary>`.
* **Theme Switching**: Toggle between Light and Dark themes via the header button to suit your reading environment.

7. Command-Line & Python API
----------------------------

The ``geometor.archimedes`` Python package provides tools for concordance analysis and apparatus compilation.

Inside the ``geometor`` workspace:

.. code-block:: bash

   # Verify codex integrity and provenance sources
   archimedes verify

   # Display summary of all 7 units, 21 tracks, and vector figures
   archimedes summary

   # Recompile apparatus RST files
   archimedes compile

Python API Example:

.. code-block:: python

   from geometor.archimedes.concordance import load_concordance, load_json_resource

   # Load all canonical proposition loci
   entries = load_concordance()
   print(f"Loaded {len(entries)} canonical Archimedean loci.")

   # Inspect ecosystem links for the Law of the Lever (Equilibrium of Planes I.6-7)
   lever = next(e for e in entries if e.id == "AP-EP-I-06")
   print("Lever theorem:", lever.title)
   print("Ecosystem links:", lever.ecosystem_links)
