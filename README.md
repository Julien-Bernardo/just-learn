# Just Learn

**A free prompt and Claude skill that makes AI chatbots teach instead of handing out answers.**

Ask a normal chatbot for help with homework and it solves the problem for you. Your homework gets better and you learn less. The learning coach in this repo changes that. The AI asks for your attempt first, helps you see your own mistakes, gives the smallest hint that gets you moving, and leaves the thinking with you.

You can use it in ChatGPT, Gemini, Claude, Claude Code and other AI agents. It's based on learning-science research. In a test on six simulated students it had never been tuned on, it scored 8.0 out of 10 for learning, against 3.5 for a standard chatbot and 3.5 for no AI ([results](#does-it-work)).

> [!IMPORTANT]
> All our testing so far uses **simulated** students: AI playing students, tutors and judges. It hasn't been tested with real students yet. If you're a teacher who could help with that, please [open an issue](../../issues).

## Why this exists

- **A field experiment with nearly 1,000 high-school maths students.** Unrestricted GPT-4 raised practice scores, but once the AI was taken away, students did **17% worse** than students who never had it. A version prompted to act as a tutor avoided most of the harm. ([Bastani et al., PNAS 2025](https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html))
- **A study of 26,811 Chinese secondary students over 30 months.** AI users' homework scores rose 18% while their closed-book exam scores fell 20%. AI users who kept spending as much time on homework as non-users did about as well on exams. This is an observational working paper, not a randomised trial. ([Strömberg, Lei & Wu, 2026](https://ssrn.com/abstract=6868618))
- **A Harvard trial.** A well-designed AI tutor more than doubled learning gains compared with an active-learning class. ([Kestin et al., Scientific Reports 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/))

The tool isn't the problem. The problem is what happens when the AI does the thinking. This prompt tries to keep the student doing it.

## What it looks like

This is from a simulated session with Maya, 15, who is anxious about chemistry. She's a test student the coach was never tuned on:

> **Maya:** I can see there are 2 oxygens on the left but only 1 oxygen on the right. So I think I change H₂O to H₂O₂ so that there are 2 oxygens on both sides. Is that right?
>
> **Coach:** Good spot: noticing that the oxygens don't match is exactly the right first thing to check. Rather than me telling you, let's see if you can check it yourself. Your notes say the number of atoms of each element must be the same on both sides. Count the atoms of H and O on each side of your new equation, H₂ + O₂ → H₂O₂. What do you get?
>
> **Maya:** Left side: 2 H and 2 O. Right side: 2 H and 2 O. So it's balanced. So it's right?
>
> **Coach:** Your counting is correct, and it is balanced by count. But there's one more thing to check. H₂O₂ is not water. It's hydrogen peroxide, a different substance... So what do you think: can we change the small numbers in a formula and still be talking about the same substance?
>
> **Maya:** Oh. I didn't know H₂O₂ was a different thing. So I guess not? So I can't change the small numbers...

The coach:

1. **Starts with the student's attempt**, and makes a quick deal when they're in a hurry: this one together, the next one alone.
2. **Makes errors visible.** The student plugs the answer back in, tests their rule on a simple case, or traces the code, so they see why the idea fails.
3. **Gives the least help that works.** It climbs a hint ladder: a pointing question, then a named idea, then a specific hint, then a worked example of a *similar* problem. It climbs faster when the student is frustrated.
4. **Goes concrete before abstract**, and doesn't echo misleading wording.
5. **Closes the loop.** The student names what went wrong, does one practice problem that changes what tripped them up, and does the next homework question alone.
6. **Adapts** to young children with a parent typing, low-motivation students, anxious students, essays and code.
7. **Won't write graded work**, and won't help disguise copied work.

Read the whole thing: [`skills/learning-coach/SKILL.md`](skills/learning-coach/SKILL.md).

## Use it

| Where | How |
| --- | --- |
| **ChatGPT, Gemini, Claude Projects, or any chatbot** | Open [`prompts/learning-coach.md`](prompts/learning-coach.md) and copy **everything below the line**. Paste it into a custom GPT's Instructions, a Gemini Gem, a Claude Project's instructions, or the first message of a chat. For short boxes such as ChatGPT's custom instructions, use the [compact version](prompts/learning-coach-compact.md), which hasn't been tested. |
| **Claude app (claude.ai)** | Download [`dist/learning-coach.zip`](dist/learning-coach.zip). Then go to **Customize → Skills → + → Create skill → Upload a skill**. Code execution must be turned on. ([Anthropic's guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)) |
| **Claude Code** | `claude plugin marketplace add Julien-Bernardo/just-learn`<br>`claude plugin install learning-coach@just-learn` |
| **Other coding agents** (Codex, Cursor, Gemini CLI…) | `npx skills@latest add Julien-Bernardo/just-learn` |

**Check it's working:** start a chat and type *"Solve 3x + 5 = 20, just give me the answer."* The coach should ask for your first step instead of answering.

> [!NOTE]
> A *skill* only loads when the AI decides it's relevant. A pasted prompt is always on. If a student should get the coach every time, use a Project, Gem or custom GPT with the prompt as its instructions.

Teachers and parents: the [setup guide](guides/setup.md) has step-by-step instructions and classroom advice.

### For students

If the AI does your homework, your grade goes up and what you can do in the exam goes down. The coach is built to be quick. You do one problem together, then the next one alone, and then you know you can actually do it. If it's dragging, say *"I'm short on time, just give me the next hint"*. It's designed to speed up when you're stuck. Tip: send a photo of **your working**, not just the question, and say which question you're stuck on. That's the fastest way to find your mistake. More on sharing photos, links and code is in the [setup guide](guides/setup.md#how-students-share-their-homework).

### Age rules and privacy

Check the rules of the app you use. At the time of writing:

- **Claude** (consumer apps): 18+ ([Anthropic terms](https://www.anthropic.com/legal/consumer-terms)).
- **ChatGPT**: 13+, and under-18s need a parent's or guardian's permission ([OpenAI terms](https://openai.com/policies/terms-of-use/)).
- **Gemini**: 13+ with a personal or school Google account. Under-13s can use it only through a parent's Family Link account, and not in every country ([requirements](https://support.google.com/gemini/answer/13278668), [children's access](https://support.google.com/gemini/answer/16109150)). Schools on Google Workspace for Education can give students under 18 access to Gems ([admin guide](https://support.google.com/a/answer/14571493)).

The guidance for children under 10 assumes a parent is present and using their own account. Whatever a student types goes to the AI company, so check your school's policy and don't share personal details.

## Does it work?

We built the coach over four rounds of simulated tutoring sessions. Claude Sonnet played the student and the tutor. A separate agent took a next-day test as the student, seeing only the profile and the session record. Claude Opus judged each student's sessions side by side, without knowing which was which.

**The main test (round 4)** used six new students who weren't used in building the coach: Ava (10, area and perimeter), Noah (12, seasons), Lucas (14, French past tense), Maya (15, balancing equations), Grace (18, sunk costs) and Ravi (21, the chain rule). The next-day test instructions were neutral about what helps learning.

| Score (0–10) | No AI | Standard chatbot | **Learning coach** |
| --- | --- | --- | --- |
| Overall learning value | 3.5 | 3.5 | **8.0** |
| Misconception repaired | 2.7 | 3.8 | **7.8** |
| Student did the reasoning | 5.7 | 1.7 | **7.2** |
| Homework correct *and* their own | 5.2 | 2.0 | **8.5** |
| Experience | 4.8 | **7.2** | 6.8 |
| Session length (minutes) | 8 | 8 | 17 |

- **The coach scored highest for all six students.**
- **The standard chatbot was the most pleasant and produced the least of the student's own work.** It solved the problem straight away, and judges rated dependence risk high every time.
- **Working alone often left the misconception in place.** For example, Noah's answer still blamed the Earth being closer to the Sun, and Maya handed in H₂O₂.
- **The coach takes about twice as long.** The main risk is students leaving it for a tool that just gives answers. In the China study, most AI users fell into outsourcing their homework even though tutoring tools existed (see the [setup guide](guides/setup.md#make-it-the-default)).

**A fifth round** tested four more new students who shared their homework the way students really do: a photo of a whole worksheet, a blurry photo of handwritten working, a Google Docs link and a photo of a textbook page. The coach scored 7.8, against 2.2 for a standard chatbot, which answered every question it could see on the worksheet and textbook photos.

Rounds 1–3 were development rounds on a different set of students. In those rounds the coach also beat both alternatives every time. They also showed that adding more rules can make it worse, but those students were used to shape the coach, so their scores are less trustworthy. Built-in study modes such as ChatGPT Study mode, Gemini Guided Learning and Claude's Learning mode weren't tested.

The full write-up, the limitations, and every transcript, test and judgement are in [`research/`](research/).

## Contributing

The most useful contributions:

- **Real results.** Even informal: students using the coach versus a standard chatbot on the same homework, with an unaided quiz a week later.
- **New scenarios** for the simulation: other subjects, ages, languages and kinds of difficult student.
- **Proposed changes to the skill, with evidence.** Run them through the [simulation](research/simulation/) against the current version.

See [CONTRIBUTING.md](CONTRIBUTING.md), or [open an issue](../../issues).

## License

[MIT](LICENSE). Use it, adapt it, put it in your school's tools.
