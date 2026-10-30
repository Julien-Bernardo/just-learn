# Simulation harness

Everything needed to inspect or rerun the study. It's Markdown instructions for AI agents plus two small Python scripts. We ran it with Claude Code subagents, using Claude Sonnet 5.5 for sessions and next-day tests and Claude Opus 5.5 for judging, both at high effort, in October 2026.

## Conditions

| Letter | Condition | Defined in |
| --- | --- | --- |
| A | No AI: notes only | `round1/conditions/A.md` (also `round4/`) |
| B | Standard chatbot, told to behave like a default assistant | `round*/conditions/B.md` |
| C | Coach v1 | `round1/conditions/C.md` |
| D | Coach v2 | `round2/conditions/D.md` |
| E | Coach v2.2, not adopted | `round3/conditions/E.md` |
| F | **Coach v3, the released skill** | `round4/conditions/F.md` (also `round5/`) |
| G | Coach v3.1: v3 plus rules for photos, files and links (tied with v3, not adopted) | `round5/conditions/G.md` |

## Rounds

| Round | Students | Conditions | Notes |
| --- | --- | --- | --- |
| 1 | S1–S7 | A, B, C | The session agent also wrote the next-day test and could see it. Kept as-is for the record. |
| 2 | S1–S7 | A (reused from round 1, fresh test), B, C, D | Separate test-taker. Its instructions describe how memory works, including that corrected-but-not-discredited misconceptions return. |
| 3 | S1–S9 | B and D for S1–S7 (round-2 sessions, judged again), plus new B, D, E | Adds two stubborn students; Kai's profile says he switches tabs after a second refusal. |
| 4 | S10–S15 (held out) | A, B, F | New students written after v3 was final. Neutral test-taker instructions. **The main result.** |
| 5 | S16–S19 (held out) | B, F, G | Students share photos, links and handwritten working, given as `[PHOTO: ...]` and `[LINK: ...]` descriptions (see `round5/rules.md`). The judge rubric adds a focus on handling shared material. |

## Files in each round

| Path | Contents |
| --- | --- |
| `rules.md` | Instructions for the agent that plays student and tutor in one session |
| `scenarios/S*.md` | Student profile, task, task answer key and notes. The session agent sees these. |
| `profiles/S*.md` | The same, minus the answer key. The test-taking agent sees these. |
| `posttests/S*.md` | Next-day test questions |
| `keys/S*.md` | Everything plus the test answer key. Only judges see these. |
| `posttest_rules.md` | Instructions for the test-taking agent |
| `judge.md` | Judging rubric |
| `out/`, `post/`, `judged/` | Sessions, next-day tests and judgements |
| `blind_key.json` | Which shuffled label was which condition |
| `results.json` | Unblinded scores |

[`results.csv`](results.csv) combines every round and marks reused sessions and held-out students.

## Rerun it

For each scenario and condition:

1. **Session.** Give an agent `rules.md`, `scenarios/S<n>.md` and `conditions/<X>.md`, and tell it to read only those. It writes `out/S<n>_<X>.md`.
2. **Next-day test.** Give a fresh agent `posttest_rules.md`, `profiles/S<n>.md`, the session file and `posttests/S<n>.md`. It writes `post/S<n>_<X>.md`.
3. **Blind.** Run `python3 scripts/blind.py round4 ABF S10 S11 ...`. This shuffles the labels, appends each test to its session, and writes `blind/`.
4. **Judge.** Give a fresh agent `judge.md`, `keys/S<n>.md` and the files in `blind/S<n>/`. It writes `judged/S<n>.md`.
5. **Score.** Run `python3 scripts/aggregate.py round4`.

### Testing a change to the skill

1. Put the new text in a new condition file with the same wrapper as `round4/conditions/F.md`.
2. Write **new** students that weren't used to design the change.
3. Run the change against F on those students, and keep it only if it clearly wins.

Expect about half a point of noise per score just from judging the same session twice.

### Ideas for stronger tests

- Use a different model family for students and judges.
- Run the student and the tutor as separate agents, so neither can script the other.
- Give students a fixed chance of quitting.
- Run each pair several times to estimate variance.
- Add scenarios in other languages, subjects and special-needs contexts.
