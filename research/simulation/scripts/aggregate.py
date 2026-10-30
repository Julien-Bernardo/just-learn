"""Unblind a round's judgements and print mean scores per condition.

Usage: python3 aggregate.py ROUND_DIR
Writes ROUND_DIR/results.json.
"""
import json, os, re, statistics as st, sys

rnd = sys.argv[1]
key = json.load(open(os.path.join(rnd, "blind_key.json")))
rows = []
for s in sorted(key):
    txt = open(os.path.join(rnd, "judged", f"{s}.md")).read()
    data = json.loads(re.search(r"```json\s*(\{.*?\})\s*```", txt, re.S).group(1))
    for cond, lab in key[s].items():
        d = dict(data[lab]); d.update(scenario=s, cond=cond); rows.append(d)
json.dump(rows, open(os.path.join(rnd, "results.json"), "w"), indent=1)
dims = ["overall", "learning", "misconception", "active_thinking", "homework", "experience", "posttest_pct", "minutes"]
for c in sorted({r["cond"] for r in rows}):
    rs = [r for r in rows if r["cond"] == c]
    print(c, f"n={len(rs)}", "  ".join(f"{d}={st.mean(r[d] for r in rs if r.get(d) is not None):.1f}" for d in dims if any(r.get(d) is not None for r in rs)))
