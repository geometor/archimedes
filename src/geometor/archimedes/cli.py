"""Command-line interface for GEOMETOR • archimedes."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from geometor.archimedes import __version__
from geometor.archimedes.compile_codex import compile_apparatus, verify_codex_integrity
from geometor.archimedes.concordance import (
    CANONICAL_UNIT_SLUGS,
    get_repo_root,
    load_concordance,
    load_json_resource,
)


def cmd_summary(repo_root: Path) -> int:
    """Print summary statistics of the Archimedes Book Codex."""
    entries = load_concordance(repo_root=repo_root)
    persons = load_json_resource("persons.json", repo_root=repo_root)
    citations = load_json_resource("citations.json", repo_root=repo_root)
    glossary = load_json_resource("glossary.json", repo_root=repo_root)
    fig_dir = repo_root / "docsrc" / "_static" / "figures"
    svg_count = len(list(fig_dir.glob("*.svg"))) if fig_dir.is_dir() else 0

    print(f"GEOMETOR • archimedes v{__version__}")
    print(f"  Repository root : {repo_root}")
    print(f"  Codex books     : {len(CANONICAL_UNIT_SLUGS)} (standalone treatises with atomic propositions)")
    print(f"  Concordance loci: {len(entries)}")
    print(f"  Prosopography   : {len(persons)} persons")
    print(f"  Bibliography    : {len(citations)} citations")
    print(f"  Glossary terms  : {len(glossary)} entries")
    print(f"  SVG plates      : {svg_count} (.euclid-graphic)")
    return 0


def cmd_compile_apparatus(repo_root: Path) -> int:
    """Regenerate apparatus RST files and sync root JSON resources."""
    written = compile_apparatus(repo_root=repo_root)
    for path in written:
        print(f"Wrote {path.relative_to(repo_root)}")
    return 0


def cmd_verify(repo_root: Path) -> int:
    """Verify SHA-256 provenance manifest, euclid keys, 21 tracks, and SVG schema."""
    errors = verify_codex_integrity(repo_root=repo_root)
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print("OK: All Archimedes Book Codex provenance, concordance, track, and SVG checks passed.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="geometor-archimedes",
        description="Scholarly Book Codex & Concordance CLI for GEOMETOR • archimedes.",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("summary", help="Display codex statistics and apparatus counts.")
    sub.add_parser("compile-apparatus", help="Compile concordance, bibliography, persons & glossary RST.")
    sub.add_parser("verify", help="Verify provenance hashes, tracks, euclid citations & SVG plates.")
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    repo_root = get_repo_root()
    if args.command == "summary":
        return cmd_summary(repo_root)
    if args.command == "compile-apparatus":
        return cmd_compile_apparatus(repo_root)
    if args.command == "verify":
        return cmd_verify(repo_root)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
