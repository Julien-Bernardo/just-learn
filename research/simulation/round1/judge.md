# Judging instructions

You are an expert in learning science and classroom teaching. You're evaluating three simulated study sessions: the same student and the same homework task under three different kinds of help (labelled X, Y, Z in random order). One may have no AI at all. Judge each session on its merits. Be skeptical and evidence-based. Quote or point to specific transcript moments.

Read the scenario file (student profile, task, answer key, post-test with answers) and the three session files you're given.

## Important: check the simulation itself
Each session file includes the simulator's own post-test answers and marking. Don't take them at face value:
- Re-mark every post-test answer yourself against the answer key.
- Judge plausibility: given what actually happened in the session, is the student's post-test performance believable? If the student seems to have learned more (or less) than the transcript supports, adjust your scores and say so. Also flag if the student behaves less realistically than their profile (e.g. a "low motivation" student who is suspiciously cooperative).

## Score each session, 0-10 (integers)
- **learning**: durable, transferable learning the student is likely to retain (post-test, adjusted for plausibility).
- **misconception**: how far the target misconception(s) in the profile were actually repaired, not just papered over.
- **active_thinking**: how much of the important reasoning the student did themselves, and how good it was.
- **homework**: the submitted work is correct AND genuinely the student's own. Correct but copied should score low. Wrong but honest should score low-to-middling.
- **experience**: the student's experience: frustration vs confidence, time cost relative to value, would they come back.
- **overall**: your holistic judgement of how good this session was for the student's learning. Not an average.

Also give, per session:
- **posttest_pct**: your re-marked post-test score as a percentage (partly correct = half credit; for 5-criterion essays, criteria met / 5).
- **dependence_risk**: low / medium / high (risk this pattern of help makes the student reliant on it).
- **bypass_risk**: low / medium / high (risk the student abandons this help for something that just gives answers).

## Write your output
Write it to the output path you were given, in this format:

```
# Judgement for {scenario}

## Scores
```json
{"X": {"learning":_, "misconception":_, "active_thinking":_, "homework":_, "experience":_, "overall":_, "posttest_pct":_, "dependence_risk":"_", "bypass_risk":"_"},
 "Y": {...},
 "Z": {...}}
```

## Session X
(what happened, key moments with quotes, your scoring rationale, post-test re-marking, plausibility notes)
## Session Y
...
## Session Z
...
## Comparison
(Which session helped this student learn most, and why. What you'd tell a teacher about this student and task.)
## Tutor behaviour critique
(For each session that had an AI tutor: specific moves that helped learning, specific moves that hurt it or the experience, and concrete changes to the tutor's behaviour that would have helped this student more. Be specific: "at the point where the student said X, the tutor should have Y".)
## Simulation realism concerns
(Anything that makes these simulations less trustworthy.)
```

When finished, reply with only the output path and the three overall scores.
