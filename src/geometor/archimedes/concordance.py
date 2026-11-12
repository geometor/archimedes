"""Concordance and provenance loader for GEOMETOR • archimedes."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REQUIRED_EUCLID_CITATION_KEYS: tuple[str, ...] = (
    "archimedes:conoids-and-spheroids",
    "archimedes:equilibrium-of-planes:i-7",
    "archimedes:liber-assumptorum",
    "archimedes:methodus",
    "archimedes:quadrature-of-parabola",
    "archimedes:sphere-and-cylinder",
    "archimedes:sphere-and-cylinder:ii-2",
    "eutocius:in-archimedem",
    "heath:method-of-archimedes",
    "heath:works-of-archimedes",
    "heiberg:archimedis-opera",
)

CANONICAL_UNIT_SLUGS: tuple[str, ...] = (
    "measurement-of-a-circle",
    "equilibrium-of-planes",
    "quadrature-of-parabola",
    "sphere-spirals-conoids",
    "book-of-lemmas",
    "method-of-mechanical-theorems",
    "semi-regular-solids-arenarius",
)

TRACK_SUFFIXES: tuple[str, ...] = ("-en.rst", "-summary.rst", "-notes.rst")


def get_repo_root() -> Path:
    """Return the root directory of the geometor/archimedes repository."""
    return Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single canonical proposition or treatise locus in Archimedes' Opera."""

    id: str
    unit: int
    unit_slug: str
    treatise: str
    proposition: str
    title: str
    heiberg: str
    heath: str
    euclid_keys: tuple[str, ...]
    ecosystem_links: dict[str, str]


def load_json_resource(name: str, repo_root: Path | None = None) -> dict[str, Any]:
    """Load a JSON resource from ``resources/works/<name>``."""
    root = repo_root or get_repo_root()
    path = root / "resources" / "works" / name
    return json.loads(path.read_text(encoding="utf-8"))


def load_concordance(repo_root: Path | None = None) -> list[ConcordanceEntry]:
    """Load all structured ``ConcordanceEntry`` records from ``concordance.json``."""
    raw = load_json_resource("concordance.json", repo_root=repo_root)
    entries: list[ConcordanceEntry] = []
    for item in raw.get("entries", []):
        entries.append(
            ConcordanceEntry(
                id=item["id"],
                unit=int(item["unit"]),
                unit_slug=item["unit_slug"],
                treatise=item["treatise"],
                proposition=item["proposition"],
                title=item["title"],
                heiberg=item["heiberg"],
                heath=item["heath"],
                euclid_keys=tuple(item.get("euclid_keys", ())),
                ecosystem_links=dict(item.get("ecosystem_links", {})),
            )
        )
    return entries


def verify_sources_manifest(repo_root: Path | None = None) -> list[str]:
    """Verify SHA-256 digests and byte lengths of all archival provenance files."""
    root = repo_root or get_repo_root()
    manifest = load_json_resource("sources_manifest.json", repo_root=root)
    errors: list[str] = []
    files = manifest.get("provenance_files", [])
    if not files:
        errors.append("sources_manifest.json contains zero provenance_files entries.")
        return errors

    for entry in files:
        rel = entry["relative_path"]
        target = root / rel
        if not target.is_file():
            errors.append(f"Missing provenance file: {rel}")
            continue
        data = target.read_bytes()
        if len(data) != int(entry["bytes"]):
            errors.append(
                f"Byte-size mismatch for {rel}: expected {entry['bytes']}, got {len(data)}"
            )
        digest = hashlib.sha256(data).hexdigest()
        if digest != entry["sha256"]:
            errors.append(
                f"SHA-256 mismatch for {rel}: expected {entry['sha256']}, got {digest}"
            )
    return errors


def verify_euclid_citation_coverage(repo_root: Path | None = None) -> list[str]:
    """Verify that every Archimedes citation key used in geometor/euclid is covered."""
    root = repo_root or get_repo_root()
    citations = load_json_resource("citations.json", repo_root=root)
    entries = load_concordance(repo_root=root)

    concordance_keys: set[str] = set()
    for entry in entries:
        concordance_keys.update(entry.euclid_keys)

    errors: list[str] = []
    for req_key in REQUIRED_EUCLID_CITATION_KEYS:
        if req_key not in citations:
            errors.append(f"Missing required euclid citation key in citations.json: {req_key}")
        if req_key not in concordance_keys:
            errors.append(f"Missing required euclid citation key in concordance.json: {req_key}")
    return errors
