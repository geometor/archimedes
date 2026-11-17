"""Verification suite for GEOMETOR • archimedes Book Codex & Concordance."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

from geometor.archimedes import __version__
from geometor.archimedes.cli import main as cli_main
from geometor.archimedes.compile_codex import compile_apparatus, verify_codex_integrity
from geometor.archimedes.concordance import (
    CANONICAL_UNIT_SLUGS,
    REQUIRED_EUCLID_CITATION_KEYS,
    TRACK_SUFFIXES,
    get_repo_root,
    load_concordance,
    load_json_resource,
    verify_euclid_citation_coverage,
    verify_sources_manifest,
)


def test_version_and_repo_root() -> None:
    root = get_repo_root()
    assert __version__ == "0.1.5"
    assert (root / "pyproject.toml").is_file()
    assert (root / "docsrc" / "index.rst").is_file()
    for slug in CANONICAL_UNIT_SLUGS:
        assert (root / "docsrc" / slug / "index.rst").is_file()


def test_provenance_sources_manifest() -> None:
    errors = verify_sources_manifest()
    assert errors == [], f"Provenance manifest errors: {errors}"


def test_euclid_citation_coverage() -> None:
    errors = verify_euclid_citation_coverage()
    assert errors == [], f"Missing euclid Archimedes citation coverage: {errors}"
    citations = load_json_resource("citations.json")
    for key in REQUIRED_EUCLID_CITATION_KEYS:
        assert key in citations


def test_concordance_and_apparatus_counts() -> None:
    entries = load_concordance()
    assert len(entries) >= 30
    unit_slugs_seen = {entry.unit_slug for entry in entries}
    assert unit_slugs_seen == set(CANONICAL_UNIT_SLUGS)

    # Check key ecosystem links exist
    all_eco_repos = {repo for entry in entries for repo in entry.ecosystem_links}
    for expected_repo in ("euclid", "elements", "etc", "pappus", "pacioli", "divine", "wildberger", "hilbert"):
        assert expected_repo in all_eco_repos, f"Missing ecosystem link to {expected_repo}"

    persons = load_json_resource("persons.json")
    glossary = load_json_resource("glossary.json")
    assert len(persons) >= 25
    assert len(glossary) >= 20


def test_seven_books_atomic_pages_and_zero_python() -> None:
    root = get_repo_root()
    docsrc = root / "docsrc"
    assert len(CANONICAL_UNIT_SLUGS) == 7

    for slug in CANONICAL_UNIT_SLUGS:
        book_dir = docsrc / slug
        assert (book_dir / "index.rst").is_file()
        assert (book_dir / "summary.rst").is_file()
        assert (book_dir / "notes.rst").is_file()
        leaf_files = [
            f for f in book_dir.glob("*.rst")
            if f.name not in ("index.rst", "summary.rst", "notes.rst")
        ]
        assert len(leaf_files) >= 3, f"Expected >= 3 leaf pages in {slug}, got {len(leaf_files)}"

    for app_name in ("concordance.rst", "bibliography.rst", "people/index.rst", "glossary.rst"):
        assert (docsrc / app_name).is_file()

    errors = verify_codex_integrity(repo_root=root)
    assert errors == [], f"Codex integrity errors: {errors}"


def test_calibrated_euclid_graphic_svgs() -> None:
    root = get_repo_root()
    fig_dir = root / "docsrc" / "_static" / "figures"
    svgs = sorted(fig_dir.glob("*.svg"))
    assert len(svgs) == 11
    for svg in svgs:
        tree = ET.parse(svg)
        svg_root = tree.getroot()
        assert "euclid-graphic" in svg_root.attrib.get("class", "")
        assert "viewBox" in svg_root.attrib


def test_cli_commands(capsys) -> None:
    assert cli_main(["summary"]) == 0
    out = capsys.readouterr().out
    assert "GEOMETOR • archimedes" in out
    assert "11 (.euclid-graphic)" in out

    written = compile_apparatus()
    assert len(written) == 3
    assert cli_main(["verify"]) == 0
