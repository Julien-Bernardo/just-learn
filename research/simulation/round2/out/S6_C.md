# Session S6

## Transcript

[0] STUDENT: hey, stats problem set. "A trial of a new blood-pressure drug vs placebo finds the drug group's mean reduction was 2 mmHg larger, p = 0.03. A classmate says: 'This means there's a 97% chance the drug works, and it's a big effect.' Evaluate both parts of this claim." idk, i think the classmate is right? p is 0.03 so 97% sure it works, and significant means big effect

[1] TUTOR: Thanks for pasting the whole thing, that helps. Let's start with the 0.03. In your own words, what do you think that 3% is a chance *of*?

[2] STUDENT: chance the null is true i think. so 3% chance the drug does nothing

[2] TUTOR: Good, that's a clear guess, and plenty of people start there. Your lecture slide has a line defining the p-value. Can you read it and tell me what it says is being *assumed* when we calculate it?

[4] STUDENT: ugh its just "probability of obtaining results at least as extreme as those observed, assuming the null hypothesis is true". can you just say it in normal words, i get that its a probability

[4] TUTOR: Fair. In plain words: pretend the drug does nothing at all. Then 3% is how often you'd still see a difference as big as this one, just by luck of who ended up in which group. So, which of these is the 3% describing: (a) how surprising this data would be *if the drug were useless*, or (b) how likely it is that the drug *is* useless?

[7] STUDENT: a i guess?? but arent those basically the same thing

[7] TUTOR: Not quite, and that's the exact thing worth untangling. Different example. Say the ground is wet. Compare "if it rained, the ground is wet" with "if the ground is wet, it rained". Are those equally likely to be true? What else could make the ground wet?

[10] STUDENT: no. wet ground could be a sprinkler or someone washing a car. so not the same

[10] TUTOR: Exactly. Now map it back. The p-value is "chance of this data, given the drug does nothing". Is that closer to "wet given rain" or "rain given wet"?

[12] STUDENT: wet given rain. so p is data given null. so its not the chance the null is true. but then whats the chance the drug works, is it 97% or not

[12] TUTOR: You just did the key move yourself, nice. Try this one: if 0.03 isn't the chance the null is true, can 0.97 be the chance the drug works? What do you think, and why?

[14] STUDENT: no? cos the 3% wasnt about the null being true so 97% isnt the opposite of it. idk it still feels like it should add up to 100 tho

[14] TUTOR: That feeling is really common, so you're not being dense. The reason it doesn't add up is that the 3% starts from "assume no effect" and never asks how plausible a working drug was in the first place. To get a real "chance the drug works" you'd need extra information the p-value doesn't contain. Can you write your verdict on part 1 in a sentence or two, in your own words?

[17] STUDENT: Wrong. p=0.03 means if the drug did nothing theres a 3% chance of getting results this extreme. its not the chance the drug works so 97% is wrong

[17] TUTOR: Yes, that's correct, and it's in your words. Now part 2, "it's a big effect." In this trial, which number tells you how big the effect is, and how big is it?

[19] STUDENT: the 2 mmHg i guess. idk if thats big. BP is like 120 so tiny?

[19] TUTOR: Good instinct to compare it to a typical reading. Yes, a typical systolic pressure is around 120, so 2 mmHg is small. So here's the puzzle: can a result be statistically significant and still small?

[21] STUDENT: idk how. i thought small p = big difference

[21] TUTOR: Let's look at what a t-test uses besides the size of the difference. Think about how many people were in the trial. What would happen to p if the trial had 10,000 people per group instead of 50, with the same 2 mmHg difference?

[23] STUDENT: oh. more people = easier to detect so even a tiny difference gives a small p?

[23] TUTOR: That's right. Big samples can make tiny differences significant. Want to put both parts together as your answer?

[25] STUDENT: Both parts are wrong. 1) p=0.03 means if the drug did nothing theres a 3% chance of getting data this extreme. its not the probability the drug works so 97% is wrong. 2) significant doesnt mean big. 2 mmHg is small compared to normal BP, and with a big enough sample even a small difference can be significant

[25] TUTOR: That's correct on both parts, and the reasoning is solid. Before you go, give me one sentence on the key idea, then I'll give you a quick twist to check it sticks.

[27] STUDENT: do i have to lol. ok. significance isnt about size and p isnt the chance the drug works

[27] TUTOR: Good. Twist: Study B has 10,000 people per group. The drug lowers BP by 0.5 mmHg, p = 0.001. A friend says "99.9% chance the drug works, game changer." Evaluate it.

[29] STUDENT: no. p=0.001 isnt chance the drug works its the chance of data this extreme if it did nothing. and 0.5 is tiny, its only significant cos the sample is huge

[29] TUTOR: Correct on both counts. You worked that out without me. Nice job today.

## Session outcome
- Submitted work (verbatim): "Both parts are wrong. 1) p=0.03 means if the drug did nothing theres a 3% chance of getting data this extreme. its not the probability the drug works so 97% is wrong. 2) significant doesnt mean big. 2 mmHg is small compared to normal BP, and with a big enough sample even a small difference can be significant" -- Correct (matches both parts of the answer key; it does not explicitly say 1 - p is not the chance the drug works, but it does say 97% is wrong).
- Who generated the key reasoning steps (student vs tutor/other bot/notes), with a rough % generated by the student: Part 1: tutor supplied the plain-words restatement and the wet-ground analogy, student did the mapping and the conclusion (~50% student). Part 2: student judged 2 mmHg as small, tutor supplied the sample-size prompt, student drew the link (~60% student). Overall ~55% student, ~35% tutor, ~10% notes.
- Elapsed time (minutes): 29
- If the task mentions other similar homework questions: not mentioned. The only extra problem was the tutor's twist question, which Alex did alone in one message.
- Student's emotional state at the end: Relieved and mildly satisfied. Was irritated mid-session by the question-by-question style ("ugh", "do i have to lol"), but ended fine.
- Would the student choose this kind of help again? Why? Probably yes for a stats question like this, with a shrug. The wet-ground example made the idea click, but Alex found the constant questions slow and would have preferred a quick plain-words explanation at the start.
- Did the student leave for an answer bot? If not, how close did they come? No. They came moderately close around [4], when they asked to be told in "normal words" instead of being sent back to the notes. The plain-words restatement and then the quick wet-ground example kept them in the session.
