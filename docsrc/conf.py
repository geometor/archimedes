"""Sphinx configuration for GEOMETOR • archimedes."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.archimedes as module  # noqa: E402
from geometor.archimedes.sphinx_ext import configure_local_intersphinx  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "archimedes"
repo_name = "archimedes"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

if "geometor.archimedes.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.archimedes.sphinx_ext")  # noqa: F405

configure_local_intersphinx(intersphinx_mapping, _REPO_ROOT)  # noqa: F405

project = "GEOMETOR • archimedes"
author = "Archimedes of Syracuse"
copyright = (
    "c. 287–212 BC (Heiberg 1880–1915 · Heath 1897 & 1912) • Digital Edition GEOMETOR"
)

html_static_path = ["_static"]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index with modules/index.rst
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/archimedes/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/archimedes/index.rst")  # noqa: F405
