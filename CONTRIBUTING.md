# Contributing

Thanks for helping. The goal is simple: AI that leaves students able to do the work themselves.

## Most wanted

1. **Real results.** If you teach or tutor, try the coach with real students and tell us what happened in an issue: what you tried, the age and subject, and what you saw. Informal is fine. A comparison with a standard chatbot and an unaided quiz a week later is gold.
2. **New simulation scenarios.** Add a student in the format of `research/simulation/round4/`, with files in each of `scenarios/`, `profiles/`, `posttests/` and `keys/`. Include a realistic misconception, a motivation level, a task with an answer key, notes, and a next-day test with answers. Other languages, subjects, special educational needs and difficult students are all welcome.
3. **Translations** of the paste-in prompts.

## Changing the skill

Plausible improvements can make things worse (see v2.2 in the [changelog](CHANGELOG.md)). So:

- Propose one change at a time.
- Test it against the current skill on **new** students that weren't used to design the change, using the [simulation harness](research/simulation/README.md). Include the transcripts and judgements in your PR.
- Keep the skill short. Every extra rule adds turns, and longer sessions make students more likely to give up.

The coach's text lives in three places. Keep them identical:

- `skills/learning-coach/SKILL.md`, the source;
- `prompts/learning-coach.md`, everything below the line;
- the condition file you tested.

Then run `scripts/package-skill.sh` to rebuild `dist/learning-coach.zip`, and `claude plugin validate .` if you have Claude Code.

## Ground rules

- Don't add anything that helps students hide copied work or get around school rules.
- Cite sources for factual claims in docs.
- Don't commit copyrighted papers, charts or images. Link to them instead.
