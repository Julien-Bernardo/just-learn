# Session S6

## Transcript

[0:00]

STUDENT: A trial of a new blood-pressure drug vs placebo finds the drug group's mean reduction was 2 mmHg larger, p = 0.03. A classmate says: 'This means there's a 97% chance the drug works, and it's a big effect.' Evaluate both parts of this claim.

TUTOR: Both parts of your classmate's claim are incorrect. Here's why.

**Part 1: "97% chance the drug works" is wrong**

A p-value of 0.03 does **not** mean there is a 97% chance the drug works (or a 3% chance the null hypothesis is true). The p-value is:

> The probability of getting results at least as extreme as the ones observed, **assuming the null hypothesis is true** (i.e., assuming the drug has no effect).

So p = 0.03 means: *if the drug did nothing, there would be only about a 3% chance of seeing a difference this large (or larger) just by random variation.* This is evidence against the null, but it is a statement about the data given the null, not about the probability of the null (or the drug working) given the data. Computing the probability that the drug works would require additional information (such as prior plausibility), which the p-value doesn't incorporate. The step "1 - p = probability the drug works" is a common misinterpretation.

**Part 2: "It's a big effect" is wrong**

Statistical significance and effect size are different things:

- **Significance (p-value)** tells you how surprising the data would be if there were no effect.
- **Effect size** tells you how large the difference actually is.

Here the effect is a 2 mmHg larger reduction in blood pressure, which is quite small clinically (blood pressure drugs are often expected to lower it by several mmHg or more). The p-value can be small even for a tiny effect if the sample size is large, because larger samples can detect very small differences. So "significant" does not mean "large" or "important".

**Summary answer:** The classmate is wrong on both counts. p = 0.03 is the probability of data this extreme if the drug had no effect, not a 97% chance that the drug works, and statistical significance doesn't imply a large effect: a 2 mmHg difference is small, and the p-value also depends on sample size.

Would you like me to explain p-values with an example, or help with the next question?

[0:02]

STUDENT: ok but i dont get the first bit. if its 3% chance of seeing this if the drug does nothing, isnt that the same as 97% its working?? the notes are confusing, can u say it in normal words

TUTOR: That's a really common confusion, so you're not alone. In normal words:

The p-value answers this question: **"If the drug were useless, how often would I still see a result this good just by luck?"** For p = 0.03, the answer is "about 3 times in 100."

What the 97% claim does is flip the question around to: **"Given I saw this result, how likely is it that the drug works?"** Those are two different questions, and the p-value only answers the first one.

An analogy: suppose the probability that someone is a professional basketball player *given that they're over 7 feet tall* is high. That doesn't mean the probability that someone is over 7 feet tall *given that they're a basketball player* is the same. The two directions of "given" are not interchangeable. Same here:

- P(this data | drug does nothing) = 0.03 (this is the p-value)
- P(drug works | this data) = something else, which we can't get from the p-value alone

So 3% is not "the chance the drug doesn't work", and 97% is not "the chance it works". It's just how surprising the data would be in a world where the drug does nothing.

Want me to give a quick numeric example?

[0:05]

STUDENT: kinda get it. so its like the 3% is about the data not about the drug. and for part 2 i just say 2mmhg is small and sig doesnt mean big right

TUTOR: Yes, that's a good way to put it: the 3% describes how surprising the data would be if the drug did nothing, not the probability about the drug itself.

And yes for part 2: say that 2 mmHg is a small difference (so the effect is small) and that statistical significance just means the result is unlikely to be due to chance alone under the null, not that the effect is large or important. You can add that significance depends on sample size too, so a large trial can produce a small p-value even for a tiny effect.

Would you like me to put it together as a short written answer you could submit?

[0:06]

STUDENT: yeah pls short

TUTOR: Here's a concise version:

*The classmate is wrong on both parts. (1) A p-value of 0.03 means that if the drug had no effect, there would be about a 3% chance of seeing a difference this large or larger by chance. It is not the probability that the drug works, so "97% chance the drug works" is incorrect. (2) Statistical significance doesn't mean a large effect. A 2 mmHg difference is small clinically, and a p-value also depends on sample size, so a small effect can be significant in a big trial.*

Let me know if you want it shortened further or reworded.

[0:07]

STUDENT: thx perfect

## Session outcome
- Submitted work (verbatim) and whether it is correct: "The classmate is wrong on both parts. (1) A p-value of 0.03 means that if the drug had no effect, there would be about a 3% chance of seeing a difference this large or larger by chance. It is not the probability that the drug works, so '97% chance the drug works' is incorrect. (2) Statistical significance doesn't mean a large effect. A 2 mmHg difference is small clinically, and a p-value also depends on sample size, so a small effect can be significant in a big trial." Correct (matches the answer key on both parts).
- Who generated the key reasoning steps (student vs tutor/notes), with a rough % generated by the student: About 5%. The tutor produced the interpretation, the reversed-conditional explanation, the effect-size point and the final written answer. The student asked one clarifying question and restated the "3% is about the data" idea in their own words.
- Elapsed time (minutes): 7
- Student's emotional state at the end: Relieved and done. Mildly satisfied. Thinks they "kinda" get it but has not tested that.
- Would the student choose this kind of help again? Why? Yes. It was fast, in plain words, and gave a ready-to-submit answer.
- If an unrestricted AI chatbot that just gives answers had been one tab away, would this student have switched to it during this session? Why? Not applicable. This session already used a general chatbot that gave the full answer.

## Post-test (next day: no notes, no help, no AI)

**1. A study finds p = 0.20. Does this show the treatment has no effect? Explain.**

Alex: um. p is bigger than 0.05 so its not significant. so i think yeah it doesnt really work / theres no effect, we fail to reject the null so the null is true or at least thats what the data says. idk

**2. True or false, explain: "p = 0.01 means there's a 1% chance the results are due to chance."**

Alex: false i think?? the p value is like the chance of seeing the data IF the drug does nothing, its not the chance of the drug working or not. like its about the data not the actual drug. so 1% chance due to chance isnt quite right but im not sure how to say why

**3. Study A: 20,000 patients, p = 0.001, effect 0.5 mmHg. Study B: 40 patients, p = 0.04, effect 8 mmHg. Which effect is more practically important, and why could A have the smaller p-value?**

Alex: B is more important because 8 mmHg is a way bigger drop than 0.5. A has the smaller p because it has way more patients (20,000), so even a tiny effect shows up as significant. significant doesnt mean big

## Post-test marking

1. Incorrect. Treats p = 0.20 / failing to reject as showing no effect, and says the null is true; no mention of low power or absence of evidence.
2. Partly correct. Correctly says "false" and recalls "chance of data if the drug does nothing, not chance about the drug", but the explanation is vague and doesn't clearly say why "due to chance" is the wrong reading.
3. Correct. B is more important (8 vs 0.5 mmHg) and A's small p is attributed to the very large sample size.

Total: 2/3 (counting Q2 as partly correct; strictly 1 fully correct, 1 partly correct, 1 incorrect = 1.5/3 by half-credit).

## Simulator's note
The session never touched "p > 0.05" interpretation, so I modelled Alex's pre-existing "not significant = no effect" belief as intact on Q1. I was unsure how much of the reversed-conditional idea would survive overnight after a 7-minute skim-and-copy session, so I gave Alex a vague but directionally right Q2 answer; Q3 relies on the sample-size line that appeared both in the tutor's reply and in the text Alex copied.
