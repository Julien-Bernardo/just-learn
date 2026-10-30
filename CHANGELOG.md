# Changelog

## 0.3.0 (2026-10-30)

First public release.

- **Learning coach v3.** This is v2 with every example made generic, so none of them come from the development test students, and "2 minutes" replaced by "a few quick steps". It was tested on six held-out students it was never tuned on, scoring 8.0/10 against 3.5 for a standard chatbot and 3.5 for no AI.
- Paste-in prompts for ChatGPT, Gemini and Claude Projects: the full version, plus an untested compact one.
- A Claude Code plugin with its marketplace, and a ZIP for uploading to claude.ai.
- A setup guide for teachers and parents.
- The full simulation record, with scripts to rerun it.

## Development versions (not released)

- **v1.** The first draft. It beat a standard chatbot and working alone in round 1 (7.1 vs 2.1 and 3.6).
- **v2.** Added rules from the round-1 judges:
  - make the error visible before fixing it;
  - concrete before abstract;
  - use correct language, not the student's misleading wording;
  - name every error at the end;
  - vary the practice problem;
  - "this one together, next one alone";
  - adapt to young children, low motivation, anxiety, writing and code.

  It scored 8.4 against v1's 7.3 in round 2. Its examples turned out to be drawn from round-1 judges' critiques, and those judges had seen the test answers, which is why v3 exists.
- **v2.2, not adopted.** It added about ten rules to v2:
  - honest step-based time estimates;
  - matching the struggle to prior knowledge;
  - "never jump to rung 5";
  - asking why the other option is wrong;
  - asking why a student changed their mind;
  - "confirm only what's right";
  - covering the student's stated weak spot;
  - retrieval quizzing;
  - pushing on the weakest link in essays;
  - "protect the effort", including quoting a 20% exam-penalty statistic to students.

  It scored 7.1 against v2's 7.7 in round 3. Every per-student gap was within judge noise, sessions were about 4 minutes longer, and judges found the statistic preachy. With no evidence it helped, the shorter v2 was kept. Its text is in `research/simulation/round3/conditions/E.md`, and its ideas may be worth testing one at a time.
