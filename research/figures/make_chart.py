"""Redraw Figure A11 of Stromberg, Lei & Wu (2026) as SVG for the Just Learn README.

The values come from the vector paths in the paper's PDF (a11_digitised.json), so the
lines and bands are the paper's own smoothed means and 95% confidence intervals.
"""
import json
import sys

data = json.load(open(sys.argv[1]))
out_dir = sys.argv[2]

THEMES = {
    "light": dict(surface="#fcfcfb", primary="#0b0b0b", secondary="#52514e", muted="#8a8984",
                  grid="#e7e6e2", ref="#52514e", noai="#2a78d6", ai="#eb6834", band_op=0.16),
    "dark": dict(surface="#1a1a19", primary="#f0efec", secondary="#c3c2b7", muted="#8f8e86",
                 grid="#2e2e2c", ref="#c3c2b7", noai="#3987e5", ai="#d95926", band_op=0.24),
}

W, H = 800, 516
L, R, T, B = 64, 28, 118, 88          # plot margins
X0, X1, Y0, Y1 = 76, 132, 50, 120     # data ranges


def sx(x):
    return L + (x - X0) / (X1 - X0) * (W - L - R)


def sy(y):
    return H - B - (y - Y0) / (Y1 - Y0) * (H - T - B)


def path(points):
    return "M" + " L".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in points)


def nearest(points, x):
    return min(points, key=lambda p: abs(p[0] - x))


def svg(theme):
    c = THEMES[theme]
    font = "font-family=\"-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif\""
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" {font} '
         f'role="img" aria-labelledby="t d">',
         '<title id="t">Homework scores up, exam scores down</title>',
         '<desc id="d">Average closed-book exam score by homework score for 26,811 Chinese secondary '
         'students, January 2023 to June 2025, scaled so the average without AI is 100. For students who '
         'never used AI, higher homework scores go with higher exam scores, rising to about 111. For AI '
         'users, exam scores peak just under 100 at a homework score of about 104, then fall to about 64 '
         'at a homework score of 131. Data: Stromberg, Lei and Wu (2026), Figure A11.</desc>',
         f'<rect width="{W}" height="{H}" rx="12" fill="{c["surface"]}"/>']

    # Title and subtitle
    s.append(f'<text x="{L - 40}" y="44" font-size="22" font-weight="600" fill="{c["primary"]}">'
             'Homework scores up, exam scores down</text>')
    s.append(f'<text x="{L - 40}" y="70" font-size="14" fill="{c["secondary"]}">'
             'Average exam score by homework score, 26,811 secondary students in China, '
             'Jan 2023 to Jun 2025</text>')

    # Legend (two series: legend always present, plus direct labels)
    lx = L - 40
    for i, (key, label) in enumerate([("noai", "Never used AI"), ("ai", "Using AI")]):
        x = lx + i * 150
        s.append(f'<line x1="{x}" y1="94" x2="{x + 20}" y2="94" stroke="{c[key]}" stroke-width="2.5" '
                 'stroke-linecap="round"/>')
        s.append(f'<text x="{x + 28}" y="98.5" font-size="13" fill="{c["secondary"]}">{label}</text>')
    s.append(f'<rect x="{lx + 270}" y="88" width="20" height="12" rx="2" fill="{c["secondary"]}" '
             f'fill-opacity="{c["band_op"] + 0.06}"/>')
    s.append(f'<text x="{lx + 298}" y="98.5" font-size="13" fill="{c["secondary"]}">95% confidence interval</text>')

    # Grid and y-axis labels
    for y in range(50, 121, 10):
        s.append(f'<line x1="{L}" y1="{sy(y):.1f}" x2="{W - R}" y2="{sy(y):.1f}" stroke="{c["grid"]}" '
                 'stroke-width="1"/>')
        s.append(f'<text x="{L - 10}" y="{sy(y) + 4.5:.1f}" font-size="12" text-anchor="end" '
                 f'fill="{c["muted"]}">{y}</text>')
    for x in range(80, 131, 10):
        s.append(f'<text x="{sx(x):.1f}" y="{H - B + 22}" font-size="12" text-anchor="middle" '
                 f'fill="{c["muted"]}">{x}</text>')
    s.append(f'<text x="{(L + W - R) / 2:.1f}" y="{H - 40}" font-size="13" text-anchor="middle" '
             f'fill="{c["secondary"]}">Homework score (100 = average without AI)</text>')
    s.append(f'<text transform="translate(18,{(T + H - B) / 2:.1f}) rotate(-90)" font-size="13" '
             f'text-anchor="middle" fill="{c["secondary"]}">Exam score (100 = average without AI)</text>')

    # Reference line at 100
    s.append(f'<line x1="{L}" y1="{sy(100):.1f}" x2="{W - R}" y2="{sy(100):.1f}" stroke="{c["ref"]}" '
             'stroke-width="1" stroke-dasharray="4 4"/>')

    # Bands, then lines
    for key in ("noai", "ai"):
        s.append(f'<path d="{path(data[key + "_band"])} Z" fill="{c[key]}" fill-opacity="{c["band_op"]}"/>')
    for key in ("noai", "ai"):
        s.append(f'<path d="{path(data[key + "_line"])}" fill="none" stroke="{c[key]}" stroke-width="2.5" '
                 'stroke-linejoin="round" stroke-linecap="round"/>')

    # Direct labels
    end = data["noai_line"][-1]
    s.append(f'<text x="{sx(end[0]) + 8:.1f}" y="{sy(end[1]) + 4:.1f}" font-size="13" font-weight="600" '
             f'fill="{c["primary"]}">Never used AI</text>')
    p = nearest(data["ai_line"], 119)
    s.append(f'<text x="{sx(p[0]) + 12:.1f}" y="{sy(p[1]) - 10:.1f}" font-size="13" font-weight="600" '
             f'fill="{c["primary"]}">Using AI</text>')

    # The paper's homework-time annotations for AI users (62 min at 100, 43 min at 120)
    for x, label, dx, anchor in ((100, "62 min on homework", 0, "middle"), (120, "43 min", -10, "end")):
        px, py = nearest(data["ai_line"], x)
        s.append(f'<circle cx="{sx(px):.1f}" cy="{sy(py):.1f}" r="4.5" fill="{c["ai"]}" '
                 f'stroke="{c["surface"]}" stroke-width="2"/>')
        ty = sy(py) + 24 if x == 100 else sy(py) + 4
        s.append(f'<text x="{sx(px) + dx:.1f}" y="{ty:.1f}" font-size="12" text-anchor="{anchor}" '
                 f'fill="{c["secondary"]}">{label}</text>')

    # Source
    s.append(f'<text x="{L - 40}" y="{H - 12}" font-size="11" fill="{c["muted"]}">'
             'Source: Strömberg, Lei &amp; Wu (2026), SSRN 6868618, Figure A11. '
             'Smoothed means; observational data. Redrawn for Just Learn.</text>')
    s.append('</svg>')
    return "\n".join(s)


for theme in THEMES:
    open(f"{out_dir}/homework-vs-exam-{theme}.svg", "w").write(svg(theme))
