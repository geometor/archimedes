"""Apparatus RST generator and Book Codex structural verifier for GEOMETOR • archimedes."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from geometor.archimedes.concordance import (
    CANONICAL_UNIT_SLUGS,
    TRACK_SUFFIXES,
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
    """Render ``docsrc/works/concordance.rst`` from ``concordance.json``."""
    root = repo_root or get_repo_root()
    raw = load_json_resource("concordance.json", repo_root=root)
    entries = load_concordance(repo_root=root)

    lines: list[str] = [
        ":order: 90",
        ":type: apparatus",
        "",
        ".. _works-concordance:",
        "",
        "Heiberg–Heath–GEOMETOR Concordance",
        "==================================",
        "",
        "Master cross-reference of Archimedes' *Opera Omnia* across :person:`Johan Ludvig Heiberg <heiberg>`'s",
        "critical Teubner editions (:cite:`heiberg:1880`, :cite:`heiberg:1881`),",
        ":person:`Sir Thomas Little Heath <heath>`'s Cambridge editions (:cite:`heath:1897`, :cite:`heath:1912`),",
        "and the constructive & philosophical codices of the GEOMETOR Digital Scriptorium.",
        "",
        "Seven-Unit Codex Architecture",
        "-----------------------------",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 8 28 32 32",
        "",
        "   * - Unit",
        "     - Treatise Unit",
        "     - Heiberg Teubner Locus",
        "     - Heath Cambridge Locus",
    ]

    for u in raw.get("units", []):
        lines.extend(
            [
                f"   * - **Unit {u['unit_number']}**",
                f"     - :doc:`{u['title']} <{u['slug']}-en>` (*{u['greek_or_latin_title']}*)",
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
            "   :widths: 12 22 18 16 32",
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
        lines.extend(
            [
                f"   * - ``{entry.id}``",
                f"     - :doc:`{entry.treatise} ({entry.proposition}) <{entry.unit_slug}-en>`",
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
        ":order: 91",
        ":type: apparatus",
        "",
        ".. _works-bibliography:",
        "",
        "Bibliography & Critical Editions",
        "================================",
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
        ":order: 92",
        ":type: apparatus",
        "",
        ".. _works-persons:",
        "",
        "Prosopography (Index Personarum)",
        "================================",
        "",
        "Chronological register of geometers, astronomers, Syracusan patrons, commentators,",
        "and philologists linked via ``:person:`` across the Archimedean corpus.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 22 14 24 40",
        "",
        "   * - Person & Native Orthography",
        "     - Flourished / Dates",
        "     - Historical Role",
        "     - Archimedean Witness & Significance",
    ]

    for _slug, p in ordered:
        lines.extend(
            [
                f"   * - **{p['name']}** (*{p['greek']}*)",
                f"     - {p['dates']}",
                f"     - {p['role']}",
                f"     - {p['summary']} (*Loci*: {p['archimedes_loci']})",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def render_glossary_rst(repo_root: Path | None = None) -> str:
    """Render ``docsrc/works/glossary.rst`` from ``glossary.json``."""
    root = repo_root or get_repo_root()
    glossary = load_json_resource("glossary.json", repo_root=root)

    lines: list[str] = [
        ":order: 93",
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
    """Synchronize root apparatus JSONs and write the four RST apparatus tables in ``docsrc/works/``."""
    root = repo_root or get_repo_root()
    sync_root_apparatus_json(repo_root=root)
    works_doc = root / "docsrc" / "works"
    works_doc.mkdir(parents=True, exist_ok=True)

    outputs = {
        works_doc / "concordance.rst": render_concordance_rst(repo_root=root),
        works_doc / "bibliography.rst": render_bibliography_rst(repo_root=root),
        works_doc / "persons.rst": render_persons_rst(repo_root=root),
        works_doc / "glossary.rst": render_glossary_rst(repo_root=root),
    }

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

    works_doc = root / "docsrc" / "works"
    index_rst = works_doc / "index.rst"
    if not index_rst.is_file():
        errors.append("Missing docsrc/works/index.rst")
    else:
        idx_text = index_rst.read_text(encoding="utf-8")
        if ":layout: book" not in idx_text:
            errors.append("docsrc/works/index.rst must declare ':layout: book'")

    for slug in CANONICAL_UNIT_SLUGS:
        for suffix in TRACK_SUFFIXES:
            track_path = works_doc / f"{slug}{suffix}"
            if not track_path.is_file():
                errors.append(f"Missing unit track file: docsrc/works/{slug}{suffix}")
                continue
            text = track_path.read_text(encoding="utf-8")
            if suffix == "-en.rst" and ".. folio::" not in text:
                errors.append(f"Primary translation track missing '.. folio::' marker: {track_path.name}")
            for pat in FORBIDDEN_CODE_PATTERNS:
                if pat.search(text):
                    errors.append(
                        f"Forbidden embedded Python script pattern '{pat.pattern}' in {track_path.name}"
                    )

    for rst_file in works_doc.glob("*.rst"):
        text = rst_file.read_text(encoding="utf-8")
        for pat in FORBIDDEN_CODE_PATTERNS:
            if pat.search(text):
                errors.append(f"Forbidden embedded Python code in {rst_file.name}")

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
