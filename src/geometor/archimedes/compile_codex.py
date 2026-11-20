"""Apparatus RST generator and Book Codex structural verifier for GEOMETOR • archimedes."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from geometor.archimedes.concordance import (
    CANONICAL_BOOK_SLUGS,
    get_repo_root,
    load_concordance,
    load_json_resource,
    verify_euclid_citation_coverage,
    verify_sources_manifest,
)

FORBIDDEN_CODE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\.\.\s+code-block::\s*python", re.IGNORECASE),
    re.compile(r":py_file:"),
    re.compile(r"\.\.\s+literalinclude::.*\.py\b", re.IGNORECASE),
)


def sync_root_apparatus_json(repo_root: Path | None = None) -> None:
    """Keep root ``resources/*.json`` synchronized with ``resources/works/*.json``."""
    root = repo_root or get_repo_root()
    works_dir = root / "resources" / "works"
    res_dir = root / "resources"
    for name in ("persons.json", "citations.json", "glossary.json"):
        shutil.copy2(works_dir / name, res_dir / name)


def render_concordance_rst(repo_root: Path | None = None) -> str:
    """Render ``docsrc/concordance.rst`` from ``concordance.json``."""
    root = repo_root or get_repo_root()
    raw = load_json_resource("concordance.json", repo_root=root)
    entries = load_concordance(repo_root=root)

    lines: list[str] = [
        ":navigation: footer",
        ":order: 50",
        ":nav_title: Concordance",
        ":type: apparatus",
        "",
        ".. _works-concordance:",
        "",
        "Heiberg–Heath–GEOMETOR Concordance",
        "==================================",
        "",
        "Master cross-reference of Archimedes' canon across :person:`Johan Ludvig Heiberg <heiberg>`'s",
        "critical Teubner editions (:cite:`heiberg:1880`, :cite:`heiberg:1881`),",
        ":person:`Sir Thomas Little Heath <heath>`'s Cambridge editions (:cite:`heath:1897`, :cite:`heath:1912`),",
        "and the constructive & philosophical codices of the GEOMETOR Digital Scriptorium.",
        "",
        "Seven-Book Codex Architecture",
        "-----------------------------",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 8 28 32 32",
        "",
        "   * - Book",
        "     - Treatise Title",
        "     - Heiberg Teubner Locus",
        "     - Heath Cambridge Locus",
    ]

    for u in raw.get("units", []):
        lines.extend(
            [
                f"   * - **Book {u['unit_number']}**",
                f"     - :doc:`{u['title']} <{u['slug']}/index>` (*{u['greek_or_latin_title']}*)",
                f"     - {u['heiberg_locus']}",
                f"     - {u['heath_locus']}",
            ]
        )

    lines.extend(
        [
            "",
            "Canonical Proposition & Ecosystem Concordance",
            "---------------------------------------------",
            "",
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 12 24 18 16 30",
            "",
            "   * - Locus ID",
            "     - Treatise & Proposition",
            "     - Heiberg / Heath",
            "     - Theorem Summary",
            "     - GEOMETOR Ecosystem Links",
        ]
    )

    for entry in entries:
        eco_str = "; ".join(f"**{k}**: {v}" for k, v in entry.ecosystem_links.items()) or "—"
        target = entry.target_doc or f"{entry.unit_slug}/index"
        lines.extend(
            [
                f"   * - ``{entry.id}``",
                f"     - :doc:`{entry.treatise} ({entry.proposition}) <{target}>`",
                f"     - Heiberg {entry.heiberg}; Heath {entry.heath}",
                f"     - {entry.title}",
                f"     - {eco_str}",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def render_bibliography_rst(repo_root: Path | None = None) -> str:
    """Render ``docsrc/works/bibliography.rst`` from ``citations.json``."""
    root = repo_root or get_repo_root()
    citations = load_json_resource("citations.json", repo_root=root)

    categories = (
        ("edition", "Critical Greek, Latin & Public-Domain English Editions"),
        ("ancient", "Ancient & Medieval Mathematical Witnesses"),
        ("modern", "GEOMETOR Ecosystem & Modern Axiomatic Concordances"),
    )

    lines: list[str] = [
        ":navigation: header",
        ":order: 8",
        ":nav_title: Bibliography",
        ":type: apparatus",
        "",
        ".. _works-bibliography:",
        "",
        "Bibliography",
        "============",
        "",
        "Archival editions, ancient mathematical commentaries, and GEOMETOR companion codices",
        "referenced via the ``:cite:`` role throughout the *Works* and *Method* of Archimedes.",
        "",
    ]

    for cat_key, heading in categories:
        lines.extend([heading, "-" * len(heading), ""])
        for key, item in citations.items():
            if item.get("category") != cat_key:
                continue
            lines.append(f".. _cite-{key}:")
            lines.append("")
            lines.append(f"* **[{key}]** — {item['author']}, *{item['work']}* ({item['locus']}).")
            if item.get("note"):
                lines.append(f"  {item['note']}")
            if item.get("url"):
                lines.append(f"  Archive: `{item['url']} <{item['url']}>`_.")
            lines.append("")

    return "\n".join(lines)


def render_persons_rst(repo_root: Path | None = None) -> str:
    """Render ``docsrc/works/persons.rst`` from ``persons.json``."""
    root = repo_root or get_repo_root()
    persons = load_json_resource("persons.json", repo_root=root)
    ordered = sorted(persons.items(), key=lambda kv: int(kv[1].get("sort_year", 0)))

    lines: list[str] = [
        ":navigation: header",
        ":order: 9",
        ":nav_title: People",
        ":type: apparatus",
        "",
        ".. _works-persons:",
        "",
        "People",
        "======",
        "",
        ".. rubric:: Biographical Register of Ancient Geometers, Translators & Commentators",
        "",
        "Chronological register of geometers, astronomers, Syracusan patrons, commentators,",
        "and philologists linked via ``:person:`` across the Archimedean corpus.",
        "",
        "Authors, Translators & Editors",
        "------------------------------",
        "",
    ]

    top_slugs = ["archimedes", "heath", "heiberg"]
    for slug in top_slugs:
        p = persons.get(slug)
        if not p:
            continue
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                f"{p['name']} ({p['dates']})",
                "~" * len(f"{p['name']} ({p['dates']})"),
                "",
                f"* **Original Name / Form**: *{p.get('greek', '')}*",
                f"* **Role**: {p.get('role', '')}",
                f"* **Archimedean Witness & Loci**: {p.get('archimedes_loci', '')}",
                "",
                p.get("summary", ""),
                "",
            ]
        )

    lines.extend(
        [
            "Cited Geometers, Philosophers & Scholars",
            "----------------------------------------",
            "",
        ]
    )

    for slug, p in ordered:
        if slug in top_slugs:
            continue
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                f"{p['name']} ({p['dates']})",
                "~" * len(f"{p['name']} ({p['dates']})"),
                "",
                f"* **Original Name / Form**: *{p.get('greek', '')}*",
                f"* **Role**: {p.get('role', '')}",
                f"* **Archimedean Witness & Loci**: {p.get('archimedes_loci', '')}",
                "",
                p.get("summary", ""),
                "",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def render_glossary_rst(repo_root: Path | None = None) -> str:
    """Render ``docsrc/works/glossary.rst`` from ``glossary.json``."""
    root = repo_root or get_repo_root()
    glossary = load_json_resource("glossary.json", repo_root=root)

    lines: list[str] = [
        ":navigation: footer",
        ":order: 60",
        ":nav_title: Glossary",
        ":type: apparatus",
        "",
        ".. _works-glossary:",
        "",
        "Greek–Latin–English Technical Glossary",
        "======================================",
        "",
        "Lexicon of Syracusan Doric, Hellenistic Koine, Arabic-Latin (*Liber Assumptorum*),",
        "and modern geometric terminology wired to the interactive ``:term:`` role.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 18 18 16 48",
        "",
        "   * - Term Key & Headword",
        "     - Greek / Latin",
        "     - English Sense",
        "     - Mathematical Definition & Loci",
    ]

    for key, item in glossary.items():
        lines.extend(
            [
                f"   * - ``{key}`` — **{item['headword']}**",
                f"     - *{item['greek']}* / *{item['latin']}*",
                f"     - {item['english']}",
                f"     - {item['definition']} (*Loci*: {item['archimedes_loci']})",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def compile_apparatus(repo_root: Path | None = None) -> list[Path]:
    """Synchronize root apparatus JSONs and write the four RST apparatus tables in ``docsrc/``."""
    root = repo_root or get_repo_root()
    sync_root_apparatus_json(repo_root=root)
    docsrc = root / "docsrc"
    docsrc.mkdir(parents=True, exist_ok=True)

    outputs = {
        docsrc / "concordance.rst": render_concordance_rst(repo_root=root),
        docsrc / "bibliography.rst": render_bibliography_rst(repo_root=root),
        docsrc / "glossary.rst": render_glossary_rst(repo_root=root),
    }
    if not (docsrc / "people" / "index.rst").is_file():
        outputs[docsrc / "persons.rst"] = render_persons_rst(repo_root=root)

    written: list[Path] = []
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def verify_codex_integrity(repo_root: Path | None = None) -> list[str]:
    """Verify full Book Codex structural, provenance, SVG, and zero-embedded-Python invariants."""
    root = repo_root or get_repo_root()
    errors: list[str] = []

    errors.extend(verify_sources_manifest(repo_root=root))
    errors.extend(verify_euclid_citation_coverage(repo_root=root))

    docsrc = root / "docsrc"
    index_rst = docsrc / "index.rst"
    if not index_rst.is_file():
        errors.append("Missing docsrc/index.rst")

    for slug in CANONICAL_BOOK_SLUGS:
        book_dir = docsrc / slug
        if not book_dir.is_dir():
            errors.append(f"Missing book directory: docsrc/{slug}")
            continue
        book_idx = book_dir / "index.rst"
        if not book_idx.is_file():
            errors.append(f"Missing book index: docsrc/{slug}/index.rst")
        else:
            text = book_idx.read_text(encoding="utf-8")
            if ":layout: book" not in text:
                errors.append(f"docsrc/{slug}/index.rst must declare ':layout: book'")
        for req_track in ("summary.rst", "notes.rst"):
            tp = book_dir / req_track
            if not tp.is_file():
                errors.append(f"Missing companion track in docsrc/{slug}: {req_track}")
        leaf_files = [f for f in book_dir.glob("*.rst") if f.name not in ("index.rst", "summary.rst", "notes.rst")]
        if not leaf_files:
            errors.append(f"No leaf proposition/section files found in docsrc/{slug}")
        for lf in leaf_files:
            text = lf.read_text(encoding="utf-8")
            if ".. enunciation::" in text and ".. folio::" not in text:
                errors.append(f"Primary enunciation page missing '.. folio::' marker: {slug}/{lf.name}")

    for app_name in ("concordance.rst", "bibliography.rst", "people/index.rst", "glossary.rst"):
        ap = docsrc / app_name
        if not ap.is_file():
            errors.append(f"Missing root apparatus table: docsrc/{app_name}")

    codex_rst_files = [docsrc / app for app in ("concordance.rst", "bibliography.rst", "people/index.rst", "glossary.rst")]
    codex_rst_files.extend(sorted((docsrc / "people").glob("*.rst")))
    for slug in CANONICAL_BOOK_SLUGS:
        book_p = docsrc / slug
        if book_p.is_dir():
            codex_rst_files.extend(book_p.glob("*.rst"))

    for rst_file in codex_rst_files:
        if not rst_file.is_file():
            continue
        text = rst_file.read_text(encoding="utf-8")
        for pat in FORBIDDEN_CODE_PATTERNS:
            if pat.search(text):
                errors.append(f"Forbidden embedded Python code in {rst_file.relative_to(docsrc)}")

    fig_dir = root / "docsrc" / "_static" / "figures"
    svg_files = sorted(fig_dir.glob("*.svg")) if fig_dir.is_dir() else []
    if len(svg_files) < 10:
        errors.append(f"Expected >= 10 calibrated .euclid-graphic SVGs, found {len(svg_files)}")
    for svg in svg_files:
        svg_text = svg.read_text(encoding="utf-8")
        if "euclid-graphic" not in svg_text:
            errors.append(f"SVG missing '.euclid-graphic' class: {svg.name}")
        if "data-命题" in svg_text or "viewBox=" not in svg_text:
            errors.append(f"SVG missing valid viewBox attribute: {svg.name}")

    return errors
