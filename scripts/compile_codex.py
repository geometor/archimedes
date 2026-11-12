"""Local workspace entry-point wrapper for geometor.archimedes.cli."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from geometor.archimedes.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
