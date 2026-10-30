# Research

On six simulated students it was never tuned on, the released learning coach (v3) scored 8.0/10 for learning, against 3.5 for a standard chatbot and 3.5 for no AI. It came out best for all six students. This is evidence from simulations, not real classrooms. This folder has the evidence behind the design, the results, the limitations, and every transcript, test and judgement.

## The evidence the design is built on

| Finding | Source |
| --- | --- |
| Unrestricted GPT-4 raised practice scores, but students did 17% worse on unaided exams afterwards. A tutor-prompted version avoided most of the harm. | [Bastani et al., PNAS 2025](https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html) |
| Across 26,811 Chinese secondary students over 30 months, AI users' homework scores rose 18% while closed-book exam scores fell 20%. The full penalty on entrance exams appeared only after about two years. About 4 in 5 AI users finished homework faster than any non-AI student, a pattern the authors read as outsourcing. AI users who kept up their homework time learned about as well as non-users. | [Strömberg, Lei & Wu, SSRN 2026](https://ssrn.com/abstract=6868618) (working paper, observational) |
| A purpose-built AI tutor more than doubled learning gains compared with an active-learning physics class at Harvard. | [Kestin et al., Scientific Reports 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/) |
| Struggling with a problem before being taught ("productive failure") improves learning. | [Sinha & Kapur 2021 meta-analysis](https://doi.org/10.3102/00346543211019105) |
| Beginners with nothing to build on learn better from worked examples first. | Cognitive-load research: the worked-example and expertise-reversal effects (Sweller; Kalyuga) |

## How the simulation works

- **Students.** Each simulated student has a well-known misconception, a realistic motivation level, a homework task, and the notes they'd have.
- **Sessions.** One Claude Sonnet agent plays *both* the student and the tutor in the same context. It's told to be realistic, including letting the student quit for an answer bot, and never told what result to expect.
- **Next-day test.** A separate agent takes a transfer test as the student, seeing only the profile and the session record. Round 1 used a different method (see the [limitations](#limitations)).
- **Judging.** Claude Opus compares all of a student's sessions side by side, under shuffled labels. It re-marks the tests, judges whether they're plausible, and scores six dimensions from 0 to 10. Its rubric defines good homework as correct *and* the student's own.
- **Conditions.**
  - *No AI*: notes only.
  - *Standard chatbot*: told to behave like a default assistant, which "readily gives full worked solutions". That is deliberate, to represent today's default behaviour.
  - *Learning coach*: one of its versions.

## Results

### Held-out test (round 4): the main result

These six students were written after the coach's text was final, and none of them were used to develop it. The next-day test instructions were neutral about what helps learning.

| Score (0–10) | No AI | Standard chatbot | Coach v3 |
| --- | --- | --- | --- |
| Overall learning value | 3.5 | 3.5 | **8.0** |
| Durable learning | 3.5 | 4.2 | **8.0** |
| Misconception repaired | 2.7 | 3.8 | **7.8** |
| Student did the reasoning | 5.7 | 1.7 | **7.2** |
| Homework correct *and* their own | 5.2 | 2.0 | **8.5** |
| Experience | 4.8 | **7.2** | 6.8 |
| Next-day test, judge-marked (%) | 67 | 97 | 100 |
| Session length (minutes) | 8 | 8 | 17 |
| Dependence risk rated high | 0/6 | 6/6 | 0/6 |

| Student | No AI | Standard chatbot | Coach v3 |
| --- | --- | --- | --- |
| Ava, 10, area and perimeter | 2 | 3 | **8** |
| Noah, 12, seasons | 1 | 5 | **9** |
| Lucas, 14, French past tense | 5 | 2 | **7** |
| Maya, 15, balancing equations | 2 | 4 | **8** |
| Grace, 18, sunk costs | 5 | 3 | **8** |
| Ravi, 21, chain rule | 6 | 4 | **8** |

Note the next-day test row. With neutral instructions, the test-taker credited students who had only *read* the chatbot's solution, giving the standard chatbot 97%. The judges discounted this when scoring durable learning (4.2). Real-world data suggests the opposite of a 97% score: in Bastani et al., unaided exam scores fell 17%.

### Development rounds (1–3)

These rounds built and compared versions of the coach on nine other students: Leo (7), Mia (9), Jayden (13), Priya (16), Tom (17), Alex (19) and Sam (20), plus Kai (15) and Zoe (17) in round 3. Their scores are less trustworthy than round 4's (see [limitations](#limitations)). Overall learning value:

| Round | No AI | Standard chatbot | Coach v1 | Coach v2 | Coach v2.2 |
| --- | --- | --- | --- | --- | --- |
| 1 (7 students) | 3.6 | 2.1 | 7.1 | – | – |
| 2 (7 students) | 3.4* | 2.3 | 7.3 | 8.4 | – |
| 3 (9 students) | – | 2.2* | – | 7.7* | 7.1 |

\* Reused sessions:

- Round 2's no-AI sessions are round 1's, given a fresh test.
- Round 3's standard-chatbot and v2 sessions for the first seven students are round 2's, judged again.

Judged again, those same 14 sessions changed score in 7 cases. v2 averaged 8.4 the first time and 7.9 the second. That is the size of the judge noise.

What the development rounds showed:

- **v1 → v2.** Round-1 judges found specific failures, and each became a rule:
  - praising the student's misleading wording;
  - abstract questions for anxious students;
  - near-copy practice problems;
  - very long sessions.

  v2 beat v1 for all seven students and was about 30% shorter.
- **v2 → v2.2: no evidence it helped.** v2.2 added about ten extra rules, plus the China study's exam statistic for the tutor to quote when students pushed for answers. It scored lower than v2 for six of nine students, but each gap was 1 point, the same size as the judge noise. Its sessions were about 4 minutes longer, and judges described the statistic as preachy in six sessions. Shorter won: we kept v2.
- **v2 → v3.** An independent review found that v2's examples had been drawn from round-1 judges' critiques, and those judges had seen the test answers. For example, v2 suggested asking "what if p had been 0.20?", which is a test question. v3 is v2 with every example replaced by a generic one, and "2 minutes" replaced by "a few quick steps". v3 was then tested only on the held-out students.
- **Stubborn students.** Kai (15) was written to have an answer bot in the next tab and to switch after a second refusal. With both coach versions he fixed one of his two misconceptions on one question, then used the other tab for at least some of the remaining questions. No simulated student ever left mid-session, in any round.

### Findings consistent with the research, though not independent of the design

Some patterns in the transcripts match what the coach is designed around. They aren't independent discoveries, because the simulation's own instructions partly encode them:

- The standard chatbot solved each problem in its first reply. That's how its condition was written.
- In rounds 2–3, the test-taker was told that misconceptions which are only corrected tend to come back. Round 4's neutral instructions removed this.

Other observations didn't depend on those instructions:

- The chatbot offered to write answers "you could submit", and in two sessions helped a student reword a copied paragraph so it wouldn't look copied.
- Students working alone often read their notes as confirming what they already believed.
- The coach's best moments came when students saw their own error, for example by counting atoms or substituting a value.

## Limitations

- **Simulated students.** The same model family plays student, tutor, test-taker and judge. In sessions, one agent plays both student and tutor, so it can script a whole exchange. Judges repeatedly flagged "low motivation" students who were more cooperative than real ones would be.
- **No real students.** Real retention, motivation and tool-switching are untested. The China study suggests most students choose answer-giving tools when they can.
- **Short-term tests that hit the ceiling.** The coach scored 100% on the round-4 test. Real learning penalties build over months.
- **Leakage in development.** Rounds 1–3 tested versions on the students they were tuned on, and v2 contained test-related examples. Only round 4 is clean on this point. One author (Claude, directed by the repo owner) wrote both v3 and the round-4 students, but v3 was finished before those students were written.
- **Small samples.** 15 students in total, one run per condition per round. Judges re-scoring the same sessions moved scores by about 0.5 on average.
- **What wasn't tested.** Built-in study modes (ChatGPT Study mode, Gemini Guided Learning, Claude's Learning mode), the compact prompt, and other languages for the coach's own instructions.

## What would settle it

A real pilot: students doing the same homework with the coach or a standard chatbot, an unaided quiz a week later, and a record of how often they switch tools. If you can run one, please open an issue.

## Files

- [`simulation/`](simulation/): every round's instructions, scenarios, transcripts, tests and judgements, plus scripts to rerun it.
- [`simulation/results.csv`](simulation/results.csv): every judged session across all rounds.
