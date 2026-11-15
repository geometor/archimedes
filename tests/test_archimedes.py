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
    assert (root / "docsrc" / "works" / "index.rst").is_file()


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


def test_seven_units_twenty_one_tracks_and_zero_python() -> None:
    root = get_repo_root()
    works_dir = root / "docsrc" / "works"
    assert len(CANONICAL_UNIT_SLUGS) == 7
    assert len(TRACK_SUFFIXES) == 3

    track_files: list[Path] = []
    for slug in CANONICAL_UNIT_SLUGS:
        for suffix in TRACK_SUFFIXES:
            p = works_dir / f"{slug}{suffix}"
            assert p.is_file(), f"Missing track file: {p}"
            track_files.append(p)
    assert len(track_files) == 21

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
    assert len(written) == 4
    assert cli_main(["verify"]) == 0
