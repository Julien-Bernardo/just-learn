"""Blind one round for judging.

Usage: python3 blind.py ROUND_DIR CONDITIONS SCENARIO [SCENARIO ...]
Example: python3 blind.py round4 ABF S10 S11

For each scenario, gives the conditions random letters (X, Y, Z, ...), appends each
next-day test to its session, strips the scenario ID from the header, writes
ROUND_DIR/blind/<scenario>/session_<letter>.md, and records the mapping in
ROUND_DIR/blind_key.json.
"""
import json, os, random, sys

rnd, conds, scenarios = sys.argv[1], sys.argv[2], sys.argv[3:]
letters = "XYZW"[: len(conds)] if len(conds) <= 3 else "WXYZ"[: len(conds)]
kp = os.path.join(rnd, "blind_key.json")
key = json.load(open(kp)) if os.path.exists(kp) else {}
rng = random.Random()
for s in scenarios:
    labs = list(letters); rng.shuffle(labs)
    m = dict(zip(conds, labs)); key[s] = m
    os.makedirs(os.path.join(rnd, "blind", s), exist_ok=True)
    for c, lab in m.items():
        sess = open(os.path.join(rnd, "out", f"{s}_{c}.md")).read().replace(f"# Session {s}", f"# Session {lab}", 1)
        post = open(os.path.join(rnd, "post", f"{s}_{c}.md")).read().replace(
            "# Next-day test", "## Next-day test (taken by the student the next day; written by a separate simulator who saw only the profile and this session record)", 1)
        open(os.path.join(rnd, "blind", s, f"session_{lab}.md"), "w").write(sess.rstrip() + "\n\n" + post)
json.dump(key, open(kp, "w"), indent=1)
print(key)
