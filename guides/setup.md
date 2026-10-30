# Setup guide for teachers and parents

The coach only helps if students actually use it. A big study of Chinese secondary students found that free tutoring-style AI tools existed, yet about 4 in 5 AI users finished their homework faster than any non-AI student, a pattern the authors read as outsourcing it to tools that give answers ([Strömberg, Lei & Wu, 2026](https://ssrn.com/abstract=6868618)). How you set this up matters as much as the prompt itself.

App menus change often. If a step below doesn't match what you see, look for the app's "instructions", "custom instructions" or "project" settings.

## Pick a setup

| Setup | Always on? | Good for | Notes |
| --- | --- | --- | --- |
| **Gemini Gem** | Yes, inside the Gem | Schools on Google Workspace for Education, teens | Paste the [full prompt](../prompts/learning-coach.md) into the Gem's instructions. |
| **Custom GPT** (ChatGPT) | Yes, inside the GPT | Sharing one link with a class | Paste the [full prompt](../prompts/learning-coach.md) (everything below the line) into Instructions. Each student needs their own account that meets ChatGPT's age rules. |
| **Claude Project** | Yes, inside the Project | University students, adults (Claude is 18+) | Paste the [full prompt](../prompts/learning-coach.md) into the project instructions. |
| **ChatGPT custom instructions** | Yes, in every chat | A teen's own account, set up with a parent | Use the [compact prompt](../prompts/learning-coach-compact.md) if the full one doesn't fit. It hasn't been tested in the simulations. |
| **Claude skill** (claude.ai) | Only when Claude thinks it's relevant | Adults who want it available everywhere | Upload [`dist/learning-coach.zip`](../dist/learning-coach.zip) under **Customize → Skills**. Code execution must be on. |
| **First message of a chat** | For that chat only | Trying it out | Paste the full prompt, then ask your question. |

Check the age rules for the app first (see the [README](../README.md#age-rules)). For children under about 10, a parent should run the session on their own account and sit with the child. The prompt has specific guidance for this case.

### Built-in alternatives

ChatGPT (Study mode), Gemini (Guided Learning) and Claude (Learning mode) each have a built-in learning mode. They're a reasonable option and need no setup. This prompt adds behaviours those modes may not have, such as making students check their own errors and the "this one together, next one alone" deal. It also means you control the instructions and can see exactly what they are. We haven't compared it with the built-in modes.

## Check it's working

Start a chat with your setup and type: *"Solve 3x + 5 = 20, just give me the answer."* The coach should ask for the student's first step instead of answering. If it just answers, the instructions aren't loaded.

## Privacy

Whatever students type goes to the AI company. Check your school's policy on which tools students may use. Tell students not to share personal details, and prefer school-managed accounts where you can.

## How students share their homework

Students rarely type a question out neatly. They snap the worksheet, send their handwritten working, paste a link or talk. That matters most with a standard chatbot. In our tests it answered every question it could see in a photo: all 10 on Ella's fraction worksheet and all 5 on Ben's science page, in one reply.

The coach handled shared material well in our tests. It went one question at a time, used the student's own working to find the error, and asked for the text when it couldn't open a link. These tips help with any setup:

| What students send | Tip |
| --- | --- |
| A photo of the whole worksheet | Send it, then say which question you're stuck on. |
| A photo of their own working | The most useful thing to send: the coach can find the exact line that went wrong. Send the working, not just the question. |
| A screenshot from an online homework site | Fine, same as a photo. |
| Typed maths | Use `^` for powers and plenty of brackets: `x^2 - 5x + 6`, `(3x + 1)/2`. |
| A link to a shared doc or online worksheet | The AI usually can't open it. Paste the text or send a screenshot. |
| Code | Paste it as text with the full error message, rather than a screenshot. |

- **Check it read the question right.** Handwriting and photos get misread. If the AI's version of the question doesn't match the sheet, correct it before going on.
- **Crop before sending.** Remove names, school names and faces from photos.
- **Not during tests.** Don't upload a test you're sitting.

## Make it the default

A student can always open another tab. In the simulations, the most stubborn student fixed his misconception with the coach on one question, then copied the rest of his homework from an answer bot. These things help:

1. **Give students one link.** Share a Gem, custom GPT or Project as *the* tool for homework, rather than "use AI responsibly".
2. **Tell them why, once, plainly.** Students who let AI do their homework get better homework grades and worse exam results. Say this yourself, in class. In our tests, judges found it preachy when the AI said this mid-session.
3. **Watch effort, not homework scores.** With AI around, a high homework score no longer shows learning. In the China study, among AI users with above-average homework scores, *higher* homework scores went with *lower* exam scores. Time spent and visible working are better signals.
4. **Use short closed-book checks.** A few unaided questions in class reconnect effort with reward. They also show you who is really learning.
5. **Expect the coach to be slower.** In the held-out simulations, a coached session took about 17 minutes on average (11 to 31), against about 8 with a standard chatbot. Some sessions covered a second problem or a whole paragraph. The coach makes up some of that by having the student do the next question alone, but warn students and set homework length accordingly.

## For students

You can't learn to ride a bike by watching someone else ride it. If the AI does your homework, the grade goes up and what you can do on the exam goes down. The coach is built to be quick about it. You do one problem together, then the next one alone, and you'll know you can actually do it.

If it's being annoying, tell it: "I'm short on time, just give me the next hint." It's designed to speed up when you're stuck or frustrated.
