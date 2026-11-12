"""Generate calibrated, theme-adaptive .euclid-graphic SVG plates for GEOMETOR Archimedes.

All generated SVGs conform strictly to the ``.euclid-graphic`` contract used by
``photon-platform/publish``'s ``.. picture::`` directive and ``geometor_interactive.js``:
- Theme-adaptive CSS custom properties (``--geom-fg``, ``--geom-bg``, ``--geom-accent``, ``--geom-assert``)
- ``<defs>`` midpoint equality tick markers (``#geom-tick-1..3``)
- 3-vertex midpoint straight paths ``M x1 y1 L mx my L x2 y2``
- Canonical ``data-ref`` attributes for bidirectional ``:g:`` and ``:eq:`` highlighting
"""

from __future__ import annotations

import math
from pathlib import Path

SVG_STYLE_AND_DEFS = """  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-2" y1="-4.5" x2="-2" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
      <line x1="2" y1="-4.5" x2="2" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-3.5" y1="-4.5" x2="-3.5" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
      <line x1="3.5" y1="-4.5" x2="3.5" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
    </marker>
  </defs>
  <style>
    :root {
      --geom-fg: #18181b;
      --geom-bg: #ffffff;
      --geom-point-stroke: #ffffff;
      --geom-poly-fill: #000000;
      --geom-accent: #c88a1e;
      --geom-assert: #16a34a;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --geom-fg: #d6cfc5;
        --geom-bg: #1e1e20;
        --geom-point-stroke: #1e1e20;
        --geom-poly-fill: #d6cfc5;
        --geom-accent: #e8b85a;
        --geom-assert: #5ec27e;
      }
    }
    .euclid-graphic {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-style: normal;
      font-weight: 700;
      background-color: var(--geom-bg);
    }
    .geom-line {
      stroke: var(--geom-fg);
      stroke-width: 1.7;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-bold {
      stroke: var(--geom-fg);
      stroke-width: 2.2;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-dashed {
      stroke: var(--geom-fg);
      stroke-width: 1.3;
      stroke-dasharray: 5, 3.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      opacity: 0.72;
    }
    .geom-accent-line {
      stroke: var(--geom-accent);
      stroke-width: 2.1;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-assert-line {
      stroke: var(--geom-assert);
      stroke-width: 2.1;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-circle {
      stroke: var(--geom-fg);
      stroke-width: 1.65;
      fill: none;
    }
    .geom-circle-accent {
      stroke: var(--geom-accent);
      stroke-width: 2.1;
      fill: var(--geom-accent);
      fill-opacity: 0.10;
    }
    .geom-circle-assert {
      stroke: var(--geom-assert);
      stroke-width: 2.0;
      stroke-dasharray: 6, 3;
      fill: var(--geom-assert);
      fill-opacity: 0.08;
    }
    .geom-arc {
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      fill: none;
    }
    .geom-ang-arc {
      stroke: var(--geom-assert);
      stroke-width: 2.0;
      stroke-linecap: round;
      fill: none;
    }
    .geom-polygon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.05;
      stroke: none;
    }
    .geom-polygon-accent {
      fill: var(--geom-accent);
      fill-opacity: 0.14;
      stroke: none;
    }
    .geom-polygon-assert {
      fill: var(--geom-assert);
      fill-opacity: 0.14;
      stroke: none;
    }
    .geom-point {
      fill: var(--geom-fg);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.1;
    }
    .geom-point-accent {
      fill: var(--geom-accent);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.1;
    }
    .geom-point-assert {
      fill: var(--geom-assert);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.1;
    }
    .geom-label {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 13.5px;
      font-weight: 700;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-label-sm {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      fill: var(--geom-fg);
      opacity: 0.88;
      user-select: none;
    }
    .geom-label-accent {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 12.5px;
      font-weight: 700;
      fill: var(--geom-accent);
      user-select: none;
    }
    .geom-label-assert {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 12.5px;
      font-weight: 700;
      fill: var(--geom-assert);
      user-select: none;
    }
  </style>"""


def _esc_ref(ref: str) -> str:
    return ref.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _svg_wrap(
    graphic_id: str,
    proposition: str,
    width: int,
    height: int,
    elements: list[str],
    graphics: list[str],
    points: list[str],
    labels: list[str],
) -> str:
    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="euclid-graphic" '
        f'data-graphic-id="{graphic_id}" data-proposition="{_esc_ref(proposition)}">'
    )
    return "\n".join(
        [
            header,
            SVG_STYLE_AND_DEFS,
            '  <g id="elements">',
            *elements,
            "  </g>",
            '  <g id="graphics">',
            *graphics,
            "  </g>",
            '  <g id="highlights" style="pointer-events: none;"></g>',
            '  <g id="points">',
            *points,
            "  </g>",
            '  <g id="labels">',
            *labels,
            "  </g>",
            "</svg>",
            "",
        ]
    )


def _seg(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    cls: str = "geom-line",
    ref: str = "",
    tick: int = 0,
) -> str:
    mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
    ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
    tick_attr = f' marker-mid="url(#geom-tick-{tick})"' if tick in (1, 2, 3) else ""
    return (
        f'    <path d="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}" '
        f'class="{cls}"{ref_attr}{tick_attr} />'
    )


def _poly(pts: list[tuple[float, float]], cls: str = "geom-polygon", ref: str = "") -> str:
    s = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
    return f'    <polygon points="{s}" class="{cls}"{ref_attr} />'


def _circ(cx: float, cy: float, r: float, cls: str = "geom-circle", ref: str = "") -> str:
    ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
    return f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" class="{cls}"{ref_attr} />'


def _semicirc_up(cx: float, cy: float, r: float, cls: str = "geom-arc", ref: str = "") -> str:
    x1, x2 = cx - r, cx + r
    mx, my = cx, cy - r
    ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
    return (
        f'    <path d="M {x1:.2f} {cy:.2f} A {r:.2f} {r:.2f} 0 0 1 {mx:.2f} {my:.2f} '
        f'A {r:.2f} {r:.2f} 0 0 1 {x2:.2f} {cy:.2f}" class="{cls}"{ref_attr} />'
    )


def _semicirc_down(cx: float, cy: float, r: float, cls: str = "geom-arc", ref: str = "") -> str:
    x1, x2 = cx - r, cx + r
    mx, my = cx, cy + r
    ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
    return (
        f'    <path d="M {x1:.2f} {cy:.2f} A {r:.2f} {r:.2f} 0 0 0 {mx:.2f} {my:.2f} '
        f'A {r:.2f} {r:.2f} 0 0 0 {x2:.2f} {cy:.2f}" class="{cls}"{ref_attr} />'
    )


def _ang_arc(
    cx: float,
    cy: float,
    r: float,
    p1: tuple[float, float],
    p2: tuple[float, float],
    cls: str = "geom-ang-arc",
    ref: str = "",
) -> str:
    a1 = math.atan2(p1[1] - cy, p1[0] - cx)
    a2 = math.atan2(p2[1] - cy, p2[0] - cx)
    diff = (a2 - a1 + math.pi) % (2.0 * math.pi) - math.pi
    am = a1 + 0.5 * diff
    sweep = 1 if diff >= 0 else 0
    sx, sy = cx + r * math.cos(a1), cy + r * math.sin(a1)
    mx, my = cx + r * math.cos(am), cy + r * math.sin(am)
    ex, ey = cx + r * math.cos(a2), cy + r * math.sin(a2)
    ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
    return (
        f'    <path d="M {sx:.2f} {sy:.2f} A {r:.2f} {r:.2f} 0 0 {sweep} {mx:.2f} {my:.2f} '
        f'A {r:.2f} {r:.2f} 0 0 {sweep} {ex:.2f} {ey:.2f}" class="{cls}"{ref_attr} />'
    )


def _pt(x: float, y: float, r: float = 3.2, cls: str = "geom-point", ref: str = "") -> str:
    ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
    return f'    <circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" class="{cls}"{ref_attr} />'


def _lbl(
    x: float,
    y: float,
    text: str,
    cls: str = "geom-label",
    anchor: str = "middle",
) -> str:
    return f'    <text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" class="{cls}">{_esc_ref(text)}</text>'


def fig_circle_96gon() -> str:
    """Dimensio Circuli Props. 1 & 3: Circle = Right Triangle & 96-gon bisection cascade."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(155, 22, "Prop. 1: Circle = Right Triangle E", "geom-label-sm"))
    lbls.append(_lbl(465, 22, "Prop. 3: 6 → 12 → 24 → 48 → 96-gon Bounds", "geom-label-sm"))

    # Left panel: Circle (O, r=40) and right triangle KLM with KL = r, LM = 2*pi*r
    ox, oy, r = 90.0, 96.0, 40.0
    ax, ay = ox, oy - r
    elems.append(_circ(ox, oy, r, "geom-circle-accent", "( O A )"))
    gfx.append(_seg(ox, oy, ax, ay, "geom-assert-line", "/ O A /", tick=1))
    pts.extend([_pt(ox, oy, ref="O"), _pt(ax, ay, ref="A")])
    lbls.extend([_lbl(ox - 11, oy + 5, "O"), _lbl(ax, ay - 7, "A"), _lbl(ox + 11, oy - 16, "r", "geom-label-assert")])

    kx, ky = 34.0, 198.0
    lx, ly = 34.0, 238.0
    mx, my = kx + 2.0 * math.pi * r, 238.0
    elems.append(_poly([(kx, ky), (lx, ly), (mx, my)], "geom-polygon-accent", "< K L M >"))
    gfx.append(_seg(kx, ky, lx, ly, "geom-assert-line", "/ K L /", tick=1))
    gfx.append(_seg(lx, ly, mx, my, "geom-bold", "/ L M /"))
    gfx.append(_seg(kx, ky, mx, my, "geom-line", "/ K M /"))
    gfx.append(_seg(lx, ly - 8, lx + 8, ly - 8, "geom-line"))
    gfx.append(_seg(lx + 8, ly - 8, lx + 8, ly, "geom-line"))
    pts.extend([_pt(kx, ky, ref="K"), _pt(lx, ly, ref="L"), _pt(mx, my, ref="M")])
    lbls.extend(
        [
            _lbl(kx - 10, ky + 4, "K"),
            _lbl(lx - 10, ly + 4, "L"),
            _lbl(mx + 8, my + 4, "M", anchor="start"),
            _lbl((lx + mx) / 2, ly + 17, "Base LM = Circumference C = 2πr", "geom-label-sm"),
            _lbl(160, 272, "Area(Circle) = ½ r · C = Area(△KLM)", "geom-label-accent"),
        ]
    )

    # Right panel: Circle centered at Z(385, 162), R = 108, diameter AC horizontal, tangent CB vertical
    zx, zy, R = 385.0, 168.0, 112.0
    cx, cy = zx + R, zy
    # Draw right half-arc of circle from -52 deg to +22 deg
    a_top, a_bot = -math.radians(48), math.radians(24)
    sx, sy = zx + R * math.cos(a_top), zy + R * math.sin(a_top)
    ex, ey = zx + R * math.cos(a_bot), zy + R * math.sin(a_bot)
    elems.append(
        f'    <path d="M {sx:.2f} {sy:.2f} A {R:.2f} {R:.2f} 0 0 1 {cx:.2f} {cy:.2f} '
        f'A {R:.2f} {R:.2f} 0 0 1 {ex:.2f} {ey:.2f}" class="geom-circle" data-ref="( Z C )" />'
    )
    gfx.append(_seg(zx, zy, cx, cy, "geom-bold", "/ Z C /"))
    # Tangent vertical segment at C up to 30 deg (half-side of 6-gon)
    angles_deg = [(30.0, "D", "6-gon"), (15.0, "F", "12-gon"), (7.5, "G", "24-gon"), (3.75, "H", "48-gon")]
    top_y = cy - R * math.tan(math.radians(30.0))
    gfx.append(_seg(cx, cy + 16, cx, top_y - 10, "geom-bold", "/ C D /"))

    for deg, name, _tag in angles_deg:
        py = cy - R * math.tan(math.radians(deg))
        cls = "geom-accent-line" if deg in (30.0, 3.75) else "geom-dashed"
        gfx.append(_seg(zx, zy, cx, py, cls, f"/ Z {name} /"))
        pts.append(_pt(cx, py, r=2.8, cls="geom-point-accent" if deg == 3.75 else "geom-point", ref=name))

    # Inscribed 6-gon chord endpoint P at -30 deg
    px, py_in = zx + R * math.cos(math.radians(30.0)), zy - R * math.sin(math.radians(30.0))
    gfx.append(_seg(cx, cy, px, py_in, "geom-assert-line", "/ C P /"))
    pts.extend([_pt(zx, zy, ref="Z"), _pt(cx, cy, ref="C"), _pt(px, py_in, cls="geom-point-assert", ref="P")])

    lbls.extend(
        [
            _lbl(zx - 12, zy + 5, "Z"),
            _lbl(cx + 12, cy + 5, "C"),
            _lbl(cx + 14, top_y + 4, "D (30°, 6-gon)", "geom-label-sm", anchor="start"),
            _lbl(cx + 14, cy - R * math.tan(math.radians(15.0)) + 4, "F (15°, 12-gon)", "geom-label-sm", anchor="start"),
            _lbl(cx + 14, cy - R * math.tan(math.radians(7.5)) + 3, "G (7½°, 24-gon)", "geom-label-sm", anchor="start"),
            _lbl(cx + 14, cy - R * math.tan(math.radians(3.75)) + 1, "H (3¾°, 48→96)", "geom-label-accent", anchor="start"),
            _lbl(px - 10, py_in - 6, "P", "geom-label-assert"),
            _lbl(465, 245, "265/153 < √3 < 1351/780", "geom-label-sm"),
            _lbl(465, 272, "3 + 10/71 < π < 3 + 1/7", "geom-label-assert"),
        ]
    )

    return _svg_wrap("fig_circle_96gon", "Dimensio Circuli 1 & 3", 620, 290, elems, gfx, pts, lbls)


def fig_triangle_centroid() -> str:
    """Equilibrium of Planes I.6–7 & I.13–14: Law of the Lever and Triangle Centroid X(2)."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(125, 24, "I.6–7: Law of the Lever", "geom-label-sm"))
    lbls.append(_lbl(415, 24, "I.13–14: Triangle Centroid G = X(2)", "geom-label-sm"))

    # Left panel: Lever HK about fulcrum L with HL : LK = 1 : 2 and weights 2W : 1W
    hx, hy = 38.0, 118.0
    lx, ly = 98.0, 118.0
    kx, ky = 218.0, 118.0
    gfx.append(_seg(hx, hy, kx, ky, "geom-bold", "/ H K /"))
    # Fulcrum triangle under L
    elems.append(_poly([(lx, ly), (lx - 10, ly + 18), (lx + 10, ly + 18)], "geom-polygon-accent"))
    gfx.append(_seg(lx, ly, lx - 10, ly + 18, "geom-accent-line"))
    gfx.append(_seg(lx - 10, ly + 18, lx + 10, ly + 18, "geom-accent-line"))
    gfx.append(_seg(lx + 10, ly + 18, lx, ly, "geom-accent-line"))
    # Suspended weights at H (2W) and K (W)
    gfx.append(_seg(hx, hy, hx, hy + 34, "geom-dashed"))
    gfx.append(_seg(kx, ky, kx, ky + 34, "geom-dashed"))
    elems.append(_poly([(hx - 20, hy + 34), (hx + 20, hy + 34), (hx + 20, hy + 84), (hx - 20, hy + 84)], "geom-polygon-accent"))
    gfx.append(_seg(hx - 20, hy + 34, hx + 20, hy + 34, "geom-accent-line"))
    gfx.append(_seg(hx + 20, hy + 34, hx + 20, hy + 84, "geom-accent-line"))
    gfx.append(_seg(hx + 20, hy + 84, hx - 20, hy + 84, "geom-accent-line"))
    gfx.append(_seg(hx - 20, hy + 84, hx - 20, hy + 34, "geom-accent-line"))

    elems.append(_poly([(kx - 14, ky + 34), (kx + 14, ky + 34), (kx + 14, ky + 69), (kx - 14, ky + 69)], "geom-polygon-assert"))
    gfx.append(_seg(kx - 14, ky + 34, kx + 14, ky + 34, "geom-assert-line"))
    gfx.append(_seg(kx + 14, ky + 34, kx + 14, ky + 69, "geom-assert-line"))
    gfx.append(_seg(kx + 14, ky + 69, kx - 14, ky + 69, "geom-assert-line"))
    gfx.append(_seg(kx - 14, ky + 69, kx - 14, ky + 34, "geom-assert-line"))

    pts.extend([_pt(hx, hy, ref="H"), _pt(lx, ly, cls="geom-point-accent", ref="L"), _pt(kx, ky, ref="K")])
    lbls.extend(
        [
            _lbl(hx, hy - 10, "H"),
            _lbl(lx, ly - 10, "L", "geom-label-accent"),
            _lbl(kx, ky - 10, "K"),
            _lbl(hx, hy + 64, "2W", "geom-label-accent"),
            _lbl(kx, ky + 56, "1W", "geom-label-assert"),
            _lbl(68, hy - 6, "1", "geom-label-sm"),
            _lbl(158, ky - 6, "2", "geom-label-sm"),
            _lbl(125, 255, "W₁ : W₂ = LK : HL", "geom-label-accent"),
        ]
    )

    # Right panel: Triangle ABC, midpoints D, E, F, medians intersecting at G = X(2)
    A = (392.0, 44.0)
    B = (274.0, 242.0)
    C = (548.0, 242.0)
    D = ((B[0] + C[0]) / 2.0, (B[1] + C[1]) / 2.0)
    E = ((C[0] + A[0]) / 2.0, (C[1] + A[1]) / 2.0)
    F = ((A[0] + B[0]) / 2.0, (A[1] + B[1]) / 2.0)
    G = ((A[0] + B[0] + C[0]) / 3.0, (A[1] + B[1] + C[1]) / 3.0)

    elems.append(_poly([A, B, C], "geom-polygon", "< A B C >"))
    # Parallel strips illustrating Archimedes' dissection bisected by median AD
    for t in (0.25, 0.50, 0.75):
        p_left = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
        p_right = (A[0] + t * (C[0] - A[0]), A[1] + t * (C[1] - A[1]))
        gfx.append(_seg(*p_left, *p_right, "geom-dashed"))

    gfx.append(_seg(*A, *B, "geom-bold", "/ A B /"))
    gfx.append(_seg(*B, *D, "geom-bold", "/ B D /", tick=1))
    gfx.append(_seg(*D, *C, "geom-bold", "/ D C /", tick=1))
    gfx.append(_seg(*C, *A, "geom-bold", "/ C A /"))

    gfx.append(_seg(*A, *D, "geom-accent-line", "/ A D /"))
    gfx.append(_seg(*B, *E, "geom-assert-line", "/ B E /"))
    gfx.append(_seg(*C, *F, "geom-assert-line", "/ C F /"))

    pts.extend(
        [
            _pt(*A, ref="A"),
            _pt(*B, ref="B"),
            _pt(*C, ref="C"),
            _pt(*D, ref="D"),
            _pt(*E, ref="E"),
            _pt(*F, ref="F"),
            _pt(*G, r=4.4, cls="geom-point-accent", ref="G"),
        ]
    )
    lbls.extend(
        [
            _lbl(A[0], A[1] - 10, "A"),
            _lbl(B[0] - 12, B[1] + 5, "B"),
            _lbl(C[0] + 12, C[1] + 5, "C"),
            _lbl(D[0], D[1] + 18, "D"),
            _lbl(E[0] + 13, E[1] - 2, "E"),
            _lbl(F[0] - 13, F[1] - 2, "F"),
            _lbl(G[0] + 18, G[1] - 7, "G = X(2)", "geom-label-accent", anchor="start"),
            _lbl(415, 282, "Barycentric (1 : 1 : 1) · AG : GD = 2 : 1", "geom-label-assert"),
        ]
    )

    return _svg_wrap("fig_triangle_centroid", "Equilibrium I.6-7, 13-14", 580, 298, elems, gfx, pts, lbls)


def fig_parabola_exhaustion() -> str:
    """Quadrature of the Parabola Props. 18–24: Geometric exhaustion 1 + 1/4 + 1/16 + ... = 4/3."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(280, 22, "Quadrature of the Parabola (Props. 18–24): Exhaustion by Inscribed Triangles", "geom-label-sm"))

    def y_par(u: float) -> float:
        return 54.0 + 0.0043 * (u - 275.0) ** 2

    uA, uC = 75.0, 495.0
    uB = 0.5 * (uA + uC)
    uE = 0.5 * (uA + uB)
    uF = 0.5 * (uB + uC)

    A = (uA, y_par(uA))
    B = (uB, y_par(uB))
    C = (uC, y_par(uC))
    D = (uB, 0.5 * (A[1] + C[1]))
    E = (uE, y_par(uE))
    F = (uF, y_par(uF))

    # Tertiary layer triangles (1/16 area)
    for u1, u2 in ((uA, uE), (uE, uB), (uB, uF), (uF, uC)):
        um = 0.5 * (u1 + u2)
        P1, Pm, P2 = (u1, y_par(u1)), (um, y_par(um)), (u2, y_par(u2))
        elems.append(_poly([P1, Pm, P2], "geom-polygon"))
        gfx.append(_seg(*P1, *Pm, "geom-dashed"))
        gfx.append(_seg(*Pm, *P2, "geom-dashed"))

    # Secondary triangles AEB and BFC (sum = 1/4 of ABC)
    elems.append(_poly([A, E, B], "geom-polygon-assert", "< A E B >"))
    elems.append(_poly([B, F, C], "geom-polygon-assert", "< B F C >"))

    # Primary inscribed triangle ABC (Delta_0)
    elems.append(_poly([A, B, C], "geom-polygon-accent", "< A B C >"))

    # Smooth parabola curve
    samples = [uA + (uC - uA) * i / 80.0 for i in range(81)]
    par_d = "M " + " L ".join(f"{u:.2f} {y_par(u):.2f}" for u in samples)
    gfx.append(f'    <path d="{par_d}" class="geom-bold" data-ref="( A B C )" />')

    # Tangent at B parallel to chord AC
    slope_ac = (C[1] - A[1]) / (C[0] - A[0])
    t_dx = 115.0
    gfx.append(_seg(B[0] - t_dx, B[1] - slope_ac * t_dx, B[0] + t_dx, B[1] + slope_ac * t_dx, "geom-dashed", "[ T1 T2 ]"))

    # Chords and diameter BD
    gfx.append(_seg(*A, *D, "geom-bold", "/ A D /", tick=1))
    gfx.append(_seg(*D, *C, "geom-bold", "/ D C /", tick=1))
    gfx.append(_seg(*A, *B, "geom-accent-line", "/ A B /"))
    gfx.append(_seg(*B, *C, "geom-accent-line", "/ B C /"))
    gfx.append(_seg(*B, *D, "geom-dashed", "/ B D /"))

    gfx.append(_seg(*A, *E, "geom-assert-line", "/ A E /"))
    gfx.append(_seg(*E, *B, "geom-assert-line", "/ E B /"))
    gfx.append(_seg(*B, *F, "geom-assert-line", "/ B F /"))
    gfx.append(_seg(*F, *C, "geom-assert-line", "/ F C /"))

    pts.extend(
        [
            _pt(*A, ref="A"),
            _pt(*B, r=3.8, cls="geom-point-accent", ref="B"),
            _pt(*C, ref="C"),
            _pt(*D, ref="D"),
            _pt(*E, cls="geom-point-assert", ref="E"),
            _pt(*F, cls="geom-point-assert", ref="F"),
        ]
    )
    lbls.extend(
        [
            _lbl(A[0] - 13, A[1] + 6, "A"),
            _lbl(B[0], B[1] - 11, "B (vertex)", "geom-label-accent"),
            _lbl(C[0] + 13, C[1] + 6, "C"),
            _lbl(D[0] + 10, D[1] + 16, "D"),
            _lbl(E[0] - 12, E[1] - 6, "E", "geom-label-assert"),
            _lbl(F[0] + 12, F[1] - 6, "F", "geom-label-assert"),
            _lbl(285, 168, "△ABC = Δ₀", "geom-label-accent"),
            _lbl(195, 122, "Δ₀/8", "geom-label-assert"),
            _lbl(382, 136, "Δ₀/8", "geom-label-assert"),
            _lbl(280, 290, "Area(Segment ABC) = Δ₀ (1 + 1/4 + 1/16 + ···) = 4/3 · Area(△ABC)", "geom-label-accent"),
        ]
    )

    return _svg_wrap("fig_parabola_exhaustion", "Quadrature of the Parabola 24", 560, 308, elems, gfx, pts, lbls)


def fig_sphere_cylinder() -> str:
    """On the Sphere and Cylinder I.33–34: Archimedes' Tomb Theorem (2 : 3 ratio)."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(260, 22, "On the Sphere and Cylinder I.33–34: Archimedes' Tomb Theorem (2 : 3)", "geom-label-sm"))

    ox, oy, R, ry = 185.0, 158.0, 96.0, 24.0
    xL, xR = ox - R, ox + R
    yT, yB = oy - R, oy + R

    # Cylinder shading
    elems.append(_poly([(xL, yT), (xR, yT), (xR, yB), (xL, yB)], "geom-polygon"))
    # Sphere circle
    elems.append(_circ(ox, oy, R, "geom-circle-accent", "( O A )"))

    # Top ellipse of cylinder
    gfx.append(
        f'    <path d="M {xL:.2f} {yT:.2f} A {R:.2f} {ry:.2f} 0 0 1 {xR:.2f} {yT:.2f}" class="geom-dashed" />'
    )
    gfx.append(
        f'    <path d="M {xL:.2f} {yT:.2f} A {R:.2f} {ry:.2f} 0 0 0 {xR:.2f} {yT:.2f}" class="geom-bold" />'
    )
    # Bottom ellipse of cylinder
    gfx.append(
        f'    <path d="M {xL:.2f} {yB:.2f} A {R:.2f} {ry:.2f} 0 0 1 {xR:.2f} {yB:.2f}" class="geom-dashed" />'
    )
    gfx.append(
        f'    <path d="M {xL:.2f} {yB:.2f} A {R:.2f} {ry:.2f} 0 0 0 {xR:.2f} {yB:.2f}" class="geom-bold" />'
    )
    # Equatorial great circle of sphere
    gfx.append(
        f'    <path d="M {xL:.2f} {oy:.2f} A {R:.2f} {ry:.2f} 0 0 1 {xR:.2f} {oy:.2f}" class="geom-dashed" />'
    )
    gfx.append(
        f'    <path d="M {xL:.2f} {oy:.2f} A {R:.2f} {ry:.2f} 0 0 0 {xR:.2f} {oy:.2f}" class="geom-accent-line" />'
    )

    # Vertical cylinder walls & inscribed cone (1 : 2 : 3 ratio!)
    gfx.append(_seg(xL, yT, xL, yB, "geom-bold", "/ K L /"))
    gfx.append(_seg(xR, yT, xR, yB, "geom-bold", "/ M N /"))
    gfx.append(_seg(ox, yT, xL, yB, "geom-assert-line", "/ C L /"))
    gfx.append(_seg(ox, yT, xR, yB, "geom-assert-line", "/ C N /"))
    gfx.append(_seg(ox, yT, ox, yB, "geom-dashed", "/ C D /"))
    gfx.append(_seg(xL, oy, xR, oy, "geom-dashed", "/ A B /"))

    # Height dimension line
    dx = 308.0
    gfx.append(_seg(dx, yT, dx, yB, "geom-line"))
    gfx.append(_seg(dx - 5, yT, dx + 5, yT, "geom-line"))
    gfx.append(_seg(dx - 5, yB, dx + 5, yB, "geom-line"))

    pts.extend(
        [
            _pt(ox, oy, cls="geom-point-accent", ref="O"),
            _pt(xL, oy, ref="A"),
            _pt(xR, oy, ref="B"),
            _pt(ox, yT, cls="geom-point-assert", ref="C"),
            _pt(ox, yB, ref="D"),
        ]
    )
    lbls.extend(
        [
            _lbl(ox + 10, oy - 6, "O", "geom-label-accent"),
            _lbl(xL - 12, oy + 4, "A"),
            _lbl(xR + 10, oy + 4, "B"),
            _lbl(ox, yT - 10, "C", "geom-label-assert"),
            _lbl(ox, yB + 20, "D"),
            _lbl(dx + 8, oy + 4, "h = 2r", "geom-label-sm", anchor="start"),
            _lbl(365, 96, "Cone : Sphere : Cylinder", "geom-label-sm", anchor="start"),
            _lbl(365, 120, "   1   :    2    :     3", "geom-label-assert", anchor="start"),
            _lbl(365, 162, "V_sph = 2/3 · V_cyl = 4/3 πr³", "geom-label-accent", anchor="start"),
            _lbl(365, 190, "S_sph = 2/3 · S_cyl = 4πr²", "geom-label-accent", anchor="start"),
            _lbl(365, 222, "S_sph = 4 · Area(Great Circle)", "geom-label-sm", anchor="start"),
        ]
    )

    return _svg_wrap("fig_sphere_cylinder", "Sphere and Cylinder I.33-34", 545, 305, elems, gfx, pts, lbls)


def fig_archimedean_spiral() -> str:
    """On Spirals Props. 18 & 24: Spiral r = a*theta, subtangent = 2*pi*r, area = 1/3 first circle."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(275, 20, "On Spirals (Props. 18 & 24): Subtangent Rectification & Sector Quadrature", "geom-label-sm"))

    # Origin O(195, 272), first circle radius R1 = 38 so 2*pi*R1 = 238.76 fits cleanly above O!
    ox, oy, R1 = 195.0, 272.0, 38.0
    ax, ay = ox + R1, oy
    tx, ty = ox, oy - 2.0 * math.pi * R1  # (195, 33.24)

    # First circle of radius R1
    elems.append(_circ(ox, oy, R1, "geom-dashed", "( O A )"))

    # Spiral sector shading (clockwise sweep in screen coords so tangent at A goes UP-LEFT to T!)
    n_steps = 120
    spiral_pts = []
    for i in range(n_steps + 1):
        th = 2.0 * math.pi * i / n_steps
        rr = R1 * (th / (2.0 * math.pi))
        sx = ox + rr * math.cos(th)
        sy = oy + rr * math.sin(th)
        spiral_pts.append((sx, sy))

    elems.append(_poly(spiral_pts, "geom-polygon-accent", "< O A >"))
    sp_d = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in spiral_pts)
    gfx.append(f'    <path d="{sp_d}" class="geom-accent-line" data-ref="( O S A )" />')

    # Initial ray OA, perpendicular subtangent OT, and tangent TA at A
    gfx.append(_seg(ox, oy, ax + 24, ay, "geom-bold", "/ O A /"))
    gfx.append(_seg(ox, oy, tx, ty, "geom-assert-line", "/ O T /"))
    gfx.append(_seg(ax, ay, tx, ty, "geom-bold", "/ A T /"))
    # Right angle box at O
    gfx.append(_seg(ox, oy - 9, ox + 9, oy - 9, "geom-line"))
    gfx.append(_seg(ox + 9, oy - 9, ox + 9, oy, "geom-line"))

    pts.extend(
        [
            _pt(ox, oy, ref="O"),
            _pt(ax, ay, cls="geom-point-accent", ref="A"),
            _pt(tx, ty, cls="geom-point-assert", ref="T"),
        ]
    )
    lbls.extend(
        [
            _lbl(ox - 12, oy + 5, "O"),
            _lbl(ax + 6, ay + 16, "A (θ = 2π)", "geom-label-accent", anchor="start"),
            _lbl(tx - 12, ty + 5, "T", "geom-label-assert"),
            _lbl(tx - 10, (oy + ty) / 2, "OT = 2π · OA", "geom-label-assert", anchor="end"),
            _lbl(295, 92, "Prop. 18 (Rectification):", "geom-label-sm", anchor="start"),
            _lbl(295, 114, "Subtangent OT = Circumference(First Circle)", "geom-label-assert", anchor="start"),
            _lbl(295, 156, "Prop. 24 (Quadrature):", "geom-label-sm", anchor="start"),
            _lbl(295, 178, "Area(Spiral Turn) = 1/3 · π · OA²", "geom-label-accent", anchor="start"),
            _lbl(295, 220, "Polar locus: r(θ) = aθ", "geom-label-sm", anchor="start"),
        ]
    )

    return _svg_wrap("fig_archimedean_spiral", "On Spirals 18 & 24", 555, 326, elems, gfx, pts, lbls)


def fig_arbelos_twins() -> str:
    """Book of Lemmas Props. 4 & 5: The Arbelos and Archimedes' Twin Circles."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(280, 22, "Book of Lemmas (Props. 4–5): The Arbelos & Archimedes' Twin Circles", "geom-label-sm"))

    # Baseline AB at y = 264, A(40, 264), B(520, 264), R = 240, r1 = 150, r2 = 90
    y0 = 264.0
    ax, bx = 40.0, 520.0
    R, r1, r2 = 240.0, 150.0, 90.0
    ox = ax + R  # 280
    cx = ax + 2.0 * r1  # 340
    o1x = ax + r1  # 190
    o2x = cx + r2  # 430

    # Altitude CD: CD^2 = AC * CB = 300 * 180 = 54000
    cd_len = math.sqrt((2.0 * r1) * (2.0 * r2))
    dx, dy = cx, y0 - cd_len

    # Arbelos shaded region path (outer semicircle CW from A to B, then CB CCW, then CA CCW)
    arb_d = (
        f"M {ax:.2f} {y0:.2f} "
        f"A {R:.2f} {R:.2f} 0 0 1 {bx:.2f} {y0:.2f} "
        f"A {r2:.2f} {r2:.2f} 0 0 0 {cx:.2f} {y0:.2f} "
        f"A {r1:.2f} {r1:.2f} 0 0 0 {ax:.2f} {y0:.2f} Z"
    )
    elems.append(f'    <path d="{arb_d}" class="geom-polygon-accent" data-ref="&lt; A D B C &gt;" />')

    # Twin circles: r_twin = r1 * r2 / (r1 + r2) = 56.25
    rt = (r1 * r2) / (r1 + r2)
    w1x = cx - rt
    h1 = math.sqrt((r1 + rt) ** 2 - (w1x - o1x) ** 2)
    w1y = y0 - h1

    w2x = cx + rt
    h2 = math.sqrt((r2 + rt) ** 2 - (w2x - o2x) ** 2)
    w2y = y0 - h2

    elems.append(_circ(w1x, w1y, rt, "geom-circle-assert", "( W1 T1 )"))
    elems.append(_circ(w2x, w2y, rt, "geom-circle-assert", "( W2 T2 )"))

    # Semicircle arcs & baseline & altitude CD
    gfx.append(_semicirc_up(ox, y0, R, "geom-bold", "( O A )"))
    gfx.append(_semicirc_up(o1x, y0, r1, "geom-bold", "( O1 A )"))
    gfx.append(_semicirc_up(o2x, y0, r2, "geom-bold", "( O2 C )"))
    gfx.append(_seg(ax, y0, bx, y0, "geom-bold", "/ A B /"))
    gfx.append(_seg(cx, y0, dx, dy, "geom-accent-line", "/ C D /"))
    # Equal twin radii segments to CD
    gfx.append(_seg(w1x, w1y, cx, w1y, "geom-assert-line", "/ W1 K1 /", tick=1))
    gfx.append(_seg(w2x, w2y, cx, w2y, "geom-assert-line", "/ W2 K2 /", tick=1))

    pts.extend(
        [
            _pt(ax, y0, ref="A"),
            _pt(cx, y0, cls="geom-point-accent", ref="C"),
            _pt(bx, y0, ref="B"),
            _pt(dx, dy, cls="geom-point-accent", ref="D"),
            _pt(w1x, w1y, cls="geom-point-assert", ref="W1"),
            _pt(w2x, w2y, cls="geom-point-assert", ref="W2"),
        ]
    )
    lbls.extend(
        [
            _lbl(ax, y0 + 18, "A"),
            _lbl(cx, y0 + 18, "C", "geom-label-accent"),
            _lbl(bx, y0 + 18, "B"),
            _lbl(dx + 12, dy + 2, "D", "geom-label-accent"),
            _lbl(w1x - 8, w1y + 4, "W₁", "geom-label-assert", anchor="end"),
            _lbl(w2x + 8, w2y + 4, "W₂", "geom-label-assert", anchor="start"),
            _lbl(145, 76, "Prop. 4: Area(Arbelos) = π · (CD/2)²", "geom-label-accent"),
            _lbl(280, 294, "Prop. 5: Twin Radii r₁ = r₂ = (r_AC · r_CB) / (r_AC + r_CB)", "geom-label-assert"),
        ]
    )

    return _svg_wrap("fig_arbelos_twins", "Liber Assumptorum 4 & 5", 560, 306, elems, gfx, pts, lbls)


def fig_arbelos_inscribed() -> str:
    """Book of Lemmas Prop. 6: Maximum Circle Inscribed in the Arbelos (AC : CB = 3 : 2 => d/AB = 6/19)."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(280, 22, "Book of Lemmas (Prop. 6): Circle Inscribed in the Arbelos & Pappus Chain Seed", "geom-label-sm"))

    y0 = 264.0
    ax, bx = 40.0, 520.0
    R = 240.0
    r1, r2 = 144.0, 96.0  # Exact 3 : 2 ratio from Heath Prop. 6!
    ox = ax + R
    cx = ax + 2.0 * r1
    o1x = ax + r1
    o2x = cx + r2

    arb_d = (
        f"M {ax:.2f} {y0:.2f} "
        f"A {R:.2f} {R:.2f} 0 0 1 {bx:.2f} {y0:.2f} "
        f"A {r2:.2f} {r2:.2f} 0 0 0 {cx:.2f} {y0:.2f} "
        f"A {r1:.2f} {r1:.2f} 0 0 0 {ax:.2f} {y0:.2f} Z"
    )
    elems.append(f'    <path d="{arb_d}" class="geom-polygon" />')

    # Exact radius r_insc = r1 * r2 * R / (r1^2 + r1*r2 + r2^2)
    ri = (r1 * r2 * R) / (r1 * r1 + r1 * r2 + r2 * r2)
    # Solve (u - r1)^2 - (u - R)^2 = (r1 + ri)^2 - (R - ri)^2 where u = x - ax
    rhs = (r1 + ri) ** 2 - (R - ri) ** 2 - (r1 * r1 - R * R)
    u = rhs / (2.0 * (R - r1))
    ix = ax + u
    iy = y0 - math.sqrt((r1 + ri) ** 2 - (u - r1) ** 2)

    elems.append(_circ(ix, iy, ri, "geom-circle-accent", "( P T )"))

    gfx.append(_semicirc_up(ox, y0, R, "geom-bold", "( O A )"))
    gfx.append(_semicirc_up(o1x, y0, r1, "geom-bold", "( O1 A )"))
    gfx.append(_semicirc_up(o2x, y0, r2, "geom-bold", "( O2 C )"))
    gfx.append(_seg(ax, y0, bx, y0, "geom-bold", "/ A B /"))

    # Centers triangle O1 - P - O2 and O - P showing Descartes/Archimedes tangency lines
    gfx.append(_seg(o1x, y0, ix, iy, "geom-dashed", "/ O1 P /"))
    gfx.append(_seg(o2x, y0, ix, iy, "geom-dashed", "/ O2 P /"))
    gfx.append(_seg(ix, iy, ix, iy - ri, "geom-assert-line", "/ P H /"))

    pts.extend(
        [
            _pt(ax, y0, ref="A"),
            _pt(o1x, y0, ref="O1"),
            _pt(cx, y0, ref="C"),
            _pt(o2x, y0, ref="O2"),
            _pt(bx, y0, ref="B"),
            _pt(ix, iy, cls="geom-point-accent", ref="P"),
        ]
    )
    lbls.extend(
        [
            _lbl(ax, y0 + 18, "A"),
            _lbl(o1x, y0 + 18, "O₁", "geom-label-sm"),
            _lbl(cx, y0 + 18, "C"),
            _lbl(o2x, y0 + 18, "O₂", "geom-label-sm"),
            _lbl(bx, y0 + 18, "B"),
            _lbl(ix + 10, iy + 5, "P", "geom-label-accent", anchor="start"),
            _lbl(125, 68, "AC : CB = 3 : 2 ⇒ d_circle : AB = 6 : 19", "geom-label-accent", anchor="start"),
            _lbl(280, 294, "General Ratio: d / AB = (r₁ r₂) / (r₁² + r₁ r₂ + r₂²)", "geom-label-assert"),
        ]
    )

    return _svg_wrap("fig_arbelos_inscribed", "Liber Assumptorum 6", 560, 306, elems, gfx, pts, lbls)


def fig_neusis_trisection() -> str:
    """Book of Lemmas Prop. 8: Archimedes' Neusis Angle Trisection."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(280, 22, "Book of Lemmas (Prop. 8): Archimedes' Neusis Angle Trisection", "geom-label-sm"))

    dx, dy, R = 345.0, 178.0, 102.0
    theta = math.radians(23.0)  # 3*theta = 69 deg
    fx, fy = dx - R, dy
    ex, ey = dx + R, dy
    cx, cy = dx - 2.0 * R * math.cos(theta), dy
    bx, by = dx - R * math.cos(theta), dy - R * math.sin(theta)
    ax, ay = dx + R * math.cos(3.0 * theta), dy - R * math.sin(3.0 * theta)

    elems.append(_circ(dx, dy, R, "geom-circle", "( D E )"))
    elems.append(_poly([(cx, cy), (dx, dy), (ax, ay)], "geom-polygon"))

    # Angle arcs: theta at C, 3*theta at D
    gfx.append(_ang_arc(cx, cy, 42.0, (dx, dy), (ax, ay), "geom-ang-arc", "< D C A )"))
    gfx.append(_ang_arc(dx, dy, 32.0, (ex, ey), (ax, ay), "geom-accent-line", "< E D A )"))

    # Extended diameter C-F-D-E, secant C-B-A, radii DB and DA
    gfx.append(_seg(cx, cy, ex + 18, ey, "geom-bold", "/ C E /"))
    gfx.append(_seg(cx, cy, bx, by, "geom-assert-line", "/ C B /", tick=1))
    gfx.append(_seg(bx, by, ax, ay, "geom-bold", "/ B A /"))
    gfx.append(_seg(dx, dy, bx, by, "geom-assert-line", "/ D B /", tick=1))
    gfx.append(_seg(dx, dy, ax, ay, "geom-accent-line", "/ D A /", tick=1))

    pts.extend(
        [
            _pt(cx, cy, cls="geom-point-assert", ref="C"),
            _pt(fx, fy, ref="F"),
            _pt(dx, dy, ref="D"),
            _pt(ex, ey, ref="E"),
            _pt(bx, by, cls="geom-point-assert", ref="B"),
            _pt(ax, ay, cls="geom-point-accent", ref="A"),
        ]
    )
    lbls.extend(
        [
            _lbl(cx - 12, cy + 5, "C", "geom-label-assert"),
            _lbl(fx - 8, fy + 18, "F"),
            _lbl(dx, dy + 19, "D"),
            _lbl(ex + 12, ey + 17, "E"),
            _lbl(bx - 8, by - 10, "B", "geom-label-assert"),
            _lbl(ax + 10, ay - 8, "A", "geom-label-accent"),
            _lbl(cx + 55, cy - 8, "θ", "geom-label-assert"),
            _lbl(dx + 38, dy - 14, "3θ", "geom-label-accent"),
            _lbl(280, 294, "Neusis insertion CB = r (= DB = DA) ⇒ ∠BCD = 1/3 · ∠ADE", "geom-label-assert"),
        ]
    )

    return _svg_wrap("fig_neusis_trisection", "Liber Assumptorum 8", 560, 308, elems, gfx, pts, lbls)


def fig_salinon() -> str:
    """Book of Lemmas Prop. 14: The Salinon (Salt-Cellar)."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(270, 20, "Book of Lemmas (Prop. 14): The Salinon (Salt-Cellar) Quadrature", "geom-label-sm"))

    ox, y0 = 270.0, 192.0
    R1 = 160.0  # Outer semicircle AB
    r2 = 44.0   # Equal side semicircles AD and EB
    r3 = R1 - 2.0 * r2  # 72.0: central lower semicircle DE

    ax, bx = ox - R1, ox + R1
    dx, ex = ax + 2.0 * r2, bx - 2.0 * r2
    cx, cy = ox, y0 - R1      # Top of outer semicircle (270, 32)
    fx, fy = ox, y0 + r3      # Bottom of lower semicircle (270, 264)

    # Salinon closed curvilinear boundary
    sal_d = (
        f"M {ax:.2f} {y0:.2f} "
        f"A {R1:.2f} {R1:.2f} 0 0 1 {bx:.2f} {y0:.2f} "
        f"A {r2:.2f} {r2:.2f} 0 0 0 {ex:.2f} {y0:.2f} "
        f"A {r3:.2f} {r3:.2f} 0 0 1 {dx:.2f} {y0:.2f} "
        f"A {r2:.2f} {r2:.2f} 0 0 0 {ax:.2f} {y0:.2f} Z"
    )
    elems.append(f'    <path d="{sal_d}" class="geom-polygon-accent" data-ref="&lt; A C B E F D &gt;" />')

    # Equal-area circle on diameter CF: center M(270, (cy+fy)/2), radius (R1 + r3)/2 = 116
    my = 0.5 * (cy + fy)
    rcf = 0.5 * (R1 + r3)
    elems.append(_circ(ox, my, rcf, "geom-circle-assert", "( M C )"))

    gfx.append(_semicirc_up(ox, y0, R1, "geom-bold", "( O A )"))
    gfx.append(_semicirc_up(ax + r2, y0, r2, "geom-bold", "( O1 A )"))
    gfx.append(_semicirc_up(bx - r2, y0, r2, "geom-bold", "( O2 E )"))
    gfx.append(_semicirc_down(ox, y0, r3, "geom-bold", "( O D )"))

    gfx.append(_seg(ax, y0, dx, y0, "geom-line", "/ A D /", tick=1))
    gfx.append(_seg(dx, y0, ex, y0, "geom-dashed", "/ D E /"))
    gfx.append(_seg(ex, y0, bx, y0, "geom-line", "/ E B /", tick=1))
    gfx.append(_seg(cx, cy, fx, fy, "geom-assert-line", "/ C F /"))

    pts.extend(
        [
            _pt(ax, y0, ref="A"),
            _pt(dx, y0, ref="D"),
            _pt(ox, y0, ref="O"),
            _pt(ex, y0, ref="E"),
            _pt(bx, y0, ref="B"),
            _pt(cx, cy, cls="geom-point-assert", ref="C"),
            _pt(fx, fy, cls="geom-point-assert", ref="F"),
        ]
    )
    lbls.extend(
        [
            _lbl(ax - 12, y0 + 5, "A"),
            _lbl(dx - 8, y0 + 17, "D"),
            _lbl(ox + 9, y0 + 15, "O", "geom-label-sm"),
            _lbl(ex + 8, y0 + 17, "E"),
            _lbl(bx + 12, y0 + 5, "B"),
            _lbl(cx + 12, cy + 12, "C", "geom-label-assert"),
            _lbl(fx + 12, fy + 4, "F", "geom-label-assert"),
            _lbl(270, 298, "Area(Salinon) = Area(Circle on Diameter CF) = π · (CF / 2)²", "geom-label-assert"),
        ]
    )

    return _svg_wrap("fig_salinon", "Liber Assumptorum 14", 540, 312, elems, gfx, pts, lbls)


def fig_method_lever() -> str:
    """The Method Prop. 1: Mechanical quadrature via infinitesimal lever slices."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(290, 22, "The Method (Prop. 1 to Eratosthenes): Mechanical Lever Balance of Infinitesimal Slices", "geom-label-sm"))

    # Lever K - A - C horizontally at y = 162, fulcrum at A(265, 162), KA = AC = 180
    y_lev = 162.0
    kx, ax, cx = 75.0, 255.0, 435.0
    # Let parabola pass through A(255, 162), vertex B(345, 92), and E(435, 232)?
    # Even cleaner: let AC be median from midpoint C(435, 162) of vertical base DE to A(255, 162)!
    # Wait: in parabola x = x_A + ((y - y_A)/70)^2 * 180:
    # At y = 162: x = 255 (vertex A!). At y = 72 and y = 252 (dy = +-90): x = 435!
    # Check tangent at D(435, 72): dx/dy = 2*(y-162)*180/8100; at y=72, dx/dy = -4, so at x=255, y_tan = 72 - (-180)/(-4)??
    # Let's check exact parabola x(y) = 255 + 180 * ((y - 162)/90)^2:
    # Vertex A(255, 162), chord DE at x = 435 from D(435, 72) to E(435, 252), midpoint C(435, 162)!
    # Slice at x_N = 365 (so AN = 110, AC = 180):
    # Parabola y-half-width at x_N: 90 * sqrt(110 / 180) = 70.356
    # Secant/circumscribing triangle A D E or A E Z!
    # In Archimedes' Method Prop. 1, triangle is formed by chord, tangent at one endpoint, and diameter parallel to axis!
    # With horizontal lever K-A-C (KA = AC = 180):
    # Fulcrum at A(255, 162).
    elems.append(_poly([(ax, y_lev), (ax - 10, y_lev + 18), (ax + 10, y_lev + 18)], "geom-polygon-accent"))
    gfx.append(_seg(ax, y_lev, ax - 10, y_lev + 18, "geom-accent-line"))
    gfx.append(_seg(ax - 10, y_lev + 18, ax + 10, y_lev + 18, "geom-accent-line"))
    gfx.append(_seg(ax + 10, y_lev + 18, ax, y_lev, "geom-accent-line"))

    # Parabolic segment on [ax, cx]
    par_pts = []
    for i in range(61):
        yy = 72.0 + 180.0 * i / 60.0
        xx = 255.0 + 180.0 * ((yy - 162.0) / 90.0) ** 2
        par_pts.append((xx, yy))
    elems.append(_poly(par_pts, "geom-polygon-accent", "< A D E >"))
    par_d = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in par_pts)
    gfx.append(f'    <path d="{par_d}" class="geom-bold" data-ref="( D A E )" />')
    gfx.append(_seg(cx, 72.0, cx, 252.0, "geom-bold", "/ D E /"))

    # Circumscribing comparison triangle (centroid at 1/3 from C -> 2/3 from A, i.e., x = 255 + 120 = 375!)
    gfx.append(_seg(ax, 72.0, cx, 72.0, "geom-dashed"))
    gfx.append(_seg(ax, 252.0, cx, 252.0, "geom-dashed"))
    gfx.append(_seg(ax, 72.0, ax, 252.0, "geom-dashed"))

    # Lever bar K - A - C
    gfx.append(_seg(kx, y_lev, cx + 25, y_lev, "geom-bold", "/ K C /"))

    # Infinitesimal chord slice MO at x_N = 355 (in situ) balanced by equal slice TG suspended at K(75)!
    xn = 355.0
    hw = 90.0 * math.sqrt((xn - ax) / 180.0)
    gfx.append(_seg(xn, y_lev - hw, xn, y_lev + hw, "geom-assert-line", "/ M O /", tick=1))
    # Suspended slice TG at K of equal length 2*hw
    gfx.append(_seg(kx, y_lev - hw, kx, y_lev + hw, "geom-assert-line", "/ T G /", tick=1))

    # Centroid W of comparison figure at x_W = ax + (2/3)*180? No, for triangle with vertical base at C and apex at A, centroid is at ax + (2/3)*180 = 375, and for parabolic segment centroid is at ax + (3/5)*180 = 363!
    pts.extend(
        [
            _pt(kx, y_lev, cls="geom-point-assert", ref="K"),
            _pt(ax, y_lev, cls="geom-point-accent", ref="A"),
            _pt(xn, y_lev, ref="N"),
            _pt(cx, y_lev, ref="C"),
            _pt(xn, y_lev - hw, cls="geom-point-assert", ref="M"),
            _pt(xn, y_lev + hw, cls="geom-point-assert", ref="O"),
            _pt(kx, y_lev - hw, cls="geom-point-assert", ref="T"),
            _pt(kx, y_lev + hw, cls="geom-point-assert", ref="G"),
        ]
    )
    lbls.extend(
        [
            _lbl(kx - 13, y_lev + 5, "K", "geom-label-assert"),
            _lbl(kx, y_lev - hw - 9, "T", "geom-label-assert"),
            _lbl(kx, y_lev + hw + 17, "G", "geom-label-assert"),
            _lbl(ax - 10, y_lev - 10, "A (fulcrum)", "geom-label-accent"),
            _lbl(xn + 10, y_lev - 6, "N", "geom-label-sm"),
            _lbl(xn, y_lev - hw - 8, "M", "geom-label-assert"),
            _lbl(xn, y_lev + hw + 16, "O", "geom-label-assert"),
            _lbl(cx + 12, y_lev - 6, "C"),
            _lbl(cx + 12, 74, "D"),
            _lbl(cx + 12, 256, "E"),
            _lbl(165, 148, "KA = AC", "geom-label-sm"),
            _lbl(290, 292, "Slice Equilibrium: KA · TG = AN · Slice(N)  ⇒  Heuristic Discovery Prior to Exhaustion", "geom-label-accent"),
        ]
    )

    return _svg_wrap("fig_method_lever", "The Method 1", 580, 308, elems, gfx, pts, lbls)


def _project_polyhedron(
    verts_3d: list[tuple[float, float, float]],
    cx: float,
    cy: float,
    scale: float,
    rx_deg: float = 22.0,
    ry_deg: float = 28.0,
) -> tuple[list[tuple[float, float, float]], list[tuple[int, int, bool]]]:
    """Rotate 3D vertices and classify minimum-length edges into front vs. back."""
    rx, ry = math.radians(rx_deg), math.radians(ry_deg)
    crx, srx = math.cos(rx), math.sin(rx)
    cry, sry = math.cos(ry), math.sin(ry)

    rot: list[tuple[float, float, float]] = []
    for x, y, z in verts_3d:
        x1 = x * cry + z * sry
        z1 = -x * sry + z * cry
        y2 = y * crx - z1 * srx
        z2 = y * srx + z1 * crx
        rot.append((cx + scale * x1, cy - scale * y2, z2))

    # Find edge length (minimum positive pairwise distance)
    dists = []
    n = len(verts_3d)
    for i in range(n):
        for j in range(i + 1, n):
            d2 = sum((verts_3d[i][k] - verts_3d[j][k]) ** 2 for k in range(3))
            dists.append(d2)
    min_d2 = min(dists)

    edges: list[tuple[int, int, bool]] = []
    for i in range(n):
        for j in range(i + 1, n):
            d2 = sum((verts_3d[i][k] - verts_3d[j][k]) ** 2 for k in range(3))
            if abs(d2 - min_d2) < 1e-5:
                front = (rot[i][2] + rot[j][2]) >= -0.05
                edges.append((i, j, front))
    return rot, edges


def fig_semi_regular_solids() -> str:
    """Archimedes' Semi-Regular Solids (via Pappus Book V -> Pacioli): Cuboctahedron & Icosidodecahedron."""
    elems, gfx, pts, lbls = [], [], [], []
    lbls.append(_lbl(150, 22, "Cuboctahedron (3.4.3.4) — Q", "geom-label-sm"))
    lbls.append(_lbl(445, 22, "Icosidodecahedron (3.5.3.5) — Q(φ)", "geom-label-sm"))

    # 1. Cuboctahedron: 12 vertices, permutations of (+-1, +-1, 0)
    cubo_v: list[tuple[float, float, float]] = []
    for s1 in (-1.0, 1.0):
        for s2 in (-1.0, 1.0):
            cubo_v.append((s1, s2, 0.0))
            cubo_v.append((s1, 0.0, s2))
            cubo_v.append((0.0, s1, s2))

    rot_c, edges_c = _project_polyhedron(cubo_v, 150.0, 150.0, 68.0, rx_deg=20.0, ry_deg=32.0)
    for i, j, front in sorted(edges_c, key=lambda e: e[2]):
        cls = "geom-bold" if front else "geom-dashed"
        gfx.append(_seg(rot_c[i][0], rot_c[i][1], rot_c[j][0], rot_c[j][1], cls))
    for idx, (px, py, pz) in enumerate(rot_c):
        pts.append(_pt(px, py, r=2.9 if pz >= 0 else 2.2, cls="geom-point-accent" if pz >= 0 else "geom-point", ref=f"V{idx}"))

    # 2. Icosidodecahedron: 30 vertices over Q(phi)
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    phi2 = phi * phi
    icosi_v: list[tuple[float, float, float]] = []
    for s in (-1.0, 1.0):
        icosi_v.append((0.0, 0.0, s * phi))
        icosi_v.append((0.0, s * phi, 0.0))
        icosi_v.append((s * phi, 0.0, 0.0))
    for s1 in (-0.5, 0.5):
        for s2 in (-0.5, 0.5):
            for s3 in (-0.5, 0.5):
                # Even permutations of (+-1/2, +-phi/2, +-phi^2/2)
                a, b, c = s1 * 1.0, s2 * phi, s3 * phi2
                icosi_v.append((a, b, c))
                icosi_v.append((b, c, a))
                icosi_v.append((c, a, b))

    rot_i, edges_i = _project_polyhedron(icosi_v, 445.0, 150.0, 62.0, rx_deg=18.0, ry_deg=26.0)
    for i, j, front in sorted(edges_i, key=lambda e: e[2]):
        cls = "geom-accent-line" if front else "geom-dashed"
        gfx.append(_seg(rot_i[i][0], rot_i[i][1], rot_i[j][0], rot_i[j][1], cls))
    for idx, (px, py, pz) in enumerate(rot_i):
        pts.append(_pt(px, py, r=2.6 if pz >= 0 else 1.9, cls="geom-point-assert" if pz >= 0 else "geom-point", ref=f"W{idx}"))

    lbls.extend(
        [
            _lbl(150, 266, "V = 12, E = 24, F = 14 (8△ + 6□)", "geom-label-accent"),
            _lbl(150, 286, "Pappus V.19 · Pacioli Exacedron abscisus", "geom-label-sm"),
            _lbl(445, 266, "V = 30, E = 60, F = 32 (20△ + 12⬠)", "geom-label-assert"),
            _lbl(445, 286, "Pappus V.19 · Pacioli Icosidodecaedron", "geom-label-sm"),
        ]
    )

    return _svg_wrap("fig_semi_regular_solids", "Pappus Synagoge V.19", 600, 304, elems, gfx, pts, lbls)


FIGURES = {
    "fig_circle_96gon.svg": fig_circle_96gon,
    "fig_triangle_centroid.svg": fig_triangle_centroid,
    "fig_parabola_exhaustion.svg": fig_parabola_exhaustion,
    "fig_sphere_cylinder.svg": fig_sphere_cylinder,
    "fig_archimedean_spiral.svg": fig_archimedean_spiral,
    "fig_arbelos_twins.svg": fig_arbelos_twins,
    "fig_arbelos_inscribed.svg": fig_arbelos_inscribed,
    "fig_neusis_trisection.svg": fig_neusis_trisection,
    "fig_salinon.svg": fig_salinon,
    "fig_method_lever.svg": fig_method_lever,
    "fig_semi_regular_solids.svg": fig_semi_regular_solids,
}


def build_all(output_dir: Path | None = None) -> list[Path]:
    """Render all 11 standalone .euclid-graphic SVGs into docsrc/_static/figures/."""
    out = output_dir or (Path(__file__).resolve().parents[1] / "docsrc" / "_static" / "figures")
    out.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for filename, fn in FIGURES.items():
        target = out / filename
        target.write_text(fn(), encoding="utf-8")
        written.append(target)
    return written


if __name__ == "__main__":
    paths = build_all()
    for p in paths:
        print(f"Generated {p.name} ({p.stat().st_size} bytes)")
