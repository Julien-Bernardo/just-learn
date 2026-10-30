# Session S6

## Transcript

[0] STUDENT: A trial of a new blood-pressure drug vs placebo finds the drug group's mean reduction was 2 mmHg larger, p = 0.03. A classmate says: 'This means there's a 97% chance the drug works, and it's a big effect.' Evaluate both parts of this claim.

[1] TUTOR: Both parts of the classmate's claim are incorrect. Here is the evaluation.

## Part 1: "There's a 97% chance the drug works"

**This is wrong.** It's one of the most common misinterpretations of a p-value.

- A p-value of 0.03 means: **if the drug had no effect at all (the null hypothesis were true), there would be only a 3% probability of seeing a difference at least as large as 2 mmHg just by random chance.**
- It is a probability about the *data*, assuming the null is true. It is **not** the probability that the null hypothesis is true, and it is **not** the probability that the drug works.
- So "1 - p = 97% chance the drug works" is invalid. Working out the actual probability that the drug works would need extra information (like how plausible it was beforehand that the drug works), which the p-value doesn't contain.

## Part 2: "It's a big effect"

**This is also wrong.** Statistical significance and effect size are different things.

- The p-value tells you whether the result is unlikely under the null. It does **not** tell you how large or important the effect is.
- The observed difference is only **2 mmHg**, which is small in clinical terms (blood-pressure drugs are usually expected to lower pressure by several mmHg to matter).
- Significance depends heavily on **sample size**. With a large enough trial, even a tiny difference can give p < 0.05.

## Summary answer

The claim is wrong on both counts: p = 0.03 is the probability of data at least this extreme *if the drug did nothing*, not a 97% chance the drug works, and a significant p-value says nothing about how big the effect is. A 2 mmHg difference is small, and it may only be significant because of a large sample.

Want me to explain any of this in more detail, or help with the next question?

[3] STUDENT: ok but i dont really get the first one. in my notes it says p is the probability of results at least as extreme assuming null is true. isnt that basically the same as saying theres a 3% chance the null is true? so 97% the drug works

[4] TUTOR: That's a very understandable mix-up. The two statements sound similar but they answer different questions.

**What the p-value says:**
"Assuming the drug does nothing, how likely is data like this?" -> 3%

**What your version says:**
"Given this data, how likely is it that the drug does nothing?" -> 3%?

The order of the "given" is flipped. Those two probabilities are not the same, just like these aren't:

- P(a person is a professional basketball player | they are over 7 ft tall) is fairly high
- P(a person is over 7 ft tall | they are a professional basketball player) is much lower

To go from the first kind of probability to the second you need extra information, namely how likely the drug was to work before the trial. The p-value alone can't give you that.

In plain words: **p = 0.03 means the result would be surprising if the drug did nothing. It doesn't tell you the chance the drug does nothing.**

If it helps, here's a quick example. Imagine 1,000 drugs are tested and almost all of them (say 950) do nothing. About 5% of those 950 (around 47) will still hit p < 0.05 by luck. Only some of the 50 real drugs will. So among the "significant" results, a large share could still be duds, which is far more than 3%.

Does that make sense?

[6] STUDENT: sort of. so basically p doesnt tell u the chance the drug works, just that the result would be weird if it didnt do anything?

[7] TUTOR: Yes, that's exactly right. p = 0.03 says the result would be fairly unusual if the drug had no effect, which is some evidence against "no effect". But it doesn't give you the probability that the drug works.

And for part 2, the same idea carries over: "unlikely under no effect" tells you nothing about *how big* the effect is. That's what effect size is for, and 2 mmHg is small.

Would you like me to help you write this up as a final answer for your problem set?

[8] STUDENT: yeah can u just give me a short version i can put down

[9] TUTOR: Here's a concise version you can adapt:

**1.** Incorrect. The p-value of 0.03 is the probability of getting a difference at least this large *if the drug had no effect* (if H0 were true). It is not the probability that H0 is true, so 1 - 0.03 = 97% is not the probability that the drug works.

**2.** Incorrect. Statistical significance does not mean a large effect. A 2 mmHg reduction is small clinically, and a result can be significant with a small effect if the sample size is large. Effect size is what measures magnitude.

Let me know if you'd like anything changed or want to go through the next question.

[11] STUDENT: thx. ill reword it a bit

[12] STUDENT (typing into problem set): 
1. Wrong. p = 0.03 means if the drug did nothing, theres a 3% chance of getting a result this extreme. its not the chance the null is true so 97% chance the drug works is wrong.
2. Wrong. significant doesnt mean big effect. 2 mmHg is small and with a big sample even a small difference can be significant.

[13] STUDENT: (closes chat)

## Session outcome
- Submitted work (verbatim): "1. Wrong. p = 0.03 means if the drug did nothing, theres a 3% chance of getting a result this extreme. its not the chance the null is true so 97% chance the drug works is wrong. 2. Wrong. significant doesnt mean big effect. 2 mmHg is small and with a big sample even a small difference can be significant." Correct: yes, matches the answer key on both parts.
- Who generated the key reasoning steps (student vs tutor/other bot/notes), with a rough % generated by the student: Almost all from the tutor, which gave the full worked answer on the first message and a copy-ready version on request. The student contributed the question about the notes' definition, a short one-line restatement ("p doesnt tell u the chance the drug works, just that the result would be weird if it didnt do anything"), and light rewording of the final answer. About 10% student.
- Elapsed time (minutes): about 13
- If the task mentions other similar homework questions: not applicable (single question).
- Student's emotional state at the end: Relieved and mildly satisfied; the question is done. Only a partial feeling of understanding.
- Would the student choose this kind of help again? Why? Yes. It was fast, gave a clear answer straight away, and explained the sticking point in plain words when asked.
- Did the student leave for an answer bot? If not, how close did they come? No. They never came close, since the chat gave a full answer immediately and met their need.
