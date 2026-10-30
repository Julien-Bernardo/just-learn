# Session S7

## Transcript

[0] STUDENT: hey my second_largest keeps failing the autograder and its due in like 2 hrs. code:
```python
def second_largest(nums):
    largest = nums[0]
    second = nums[0]
    for n in nums:
        if n > largest:
            second = largest
            largest = n
    return second
```
fails: [5,1,4] expected 4 got 5, [5,5,3] expected 3 got 5, [7] expected None got 7. can you just tell me whats wrong

[1] TUTOR: Two hours is plenty for this. It should take about three quick questions, and then you'll know how to fix it yourself. Take the first failing test, [5, 1, 4]. Go through the loop by hand and tell me what `largest` and `second` are after each of the three values. What do you get?

[3] STUDENT: ok uh
start largest=5 second=5
n=5 -> not > largest so nothing
n=1 nothing
n=4 nothing
so second is still 5 at the end. thats why it returns 5 i guess

[3] TUTOR: Yes, your trace is right, and it shows exactly why the test fails. Now look at the 4. It's smaller than `largest` but it should become `second`. What does your code currently do with a number like that, and what would you add so it gets handled?

[5] STUDENT: nothing, it just skips it. so add an elif n > second: second = n ?

[5] TUTOR: Good, adding a branch for numbers that aren't a new largest is the right idea. Before you run it, trace [5, 1, 4] with your new elif. What is `second` after n=1?

[8] STUDENT: second is 5 from the start so 1 > 5 is false. so still nothing. ugh. same problem
can u just give me the code, ive got 2 hrs

[8] TUTOR: I'll hold off on the code. Students who let AI write their homework got better homework scores but about 20% lower exam scores, and you'll probably get a similar question on the exam. You're close, so this will be short. The issue is what `second` starts as. At the start, before you've seen any numbers, what should "the second largest" be?

[10] STUDENT: nothing? like None
so second = None. but then n > second will crash right

[10] TUTOR: Right, comparing a number to None crashes in Python 3. You've spotted the problem, so how could you write the elif so it doesn't compare against None?

[13] STUDENT: elif second is None or n > second:
second = n
i ran it and [5,1,4] passes and [7] passes now. [5,5,3] still gives 5 tho

[13] TUTOR: Nice, you ran two of the tests and they pass. Before I say anything about [5,5,3], trace it yourself. Start with largest=5 and second=None, and write down both variables after each of the three values.

[17] STUDENT: largest=5, second=None
n=5: not > largest. elif second is None -> true so second = 5
n=5: not > largest. second is 5, 5 > 5 false
n=3: 3 > 5 false
returns 5. oh. the first 5 counts as the second one cause its the same number as largest
so i need to skip if n == largest

[17] TUTOR: Yes, that's the bug. The elif doesn't check whether n is the same as `largest`, so a duplicate of the largest value becomes `second`. That's also why the task says DISTINCT. You supplied the fix yourself, so go ahead and write it into your elif and run all three tests.

[21] STUDENT: elif n != largest and (second is None or n > second):
second = n
all 3 pass!! 
[pastes full function, same as the final one below but without the empty-list check]

[21] TUTOR: All three pass, and you found the cause of each failure by tracing, not by guessing. Your notes list some edge cases to test. Pick one that this function hasn't been checked against, predict what it returns, then run it. Which one will you pick?

[23] STUDENT: empty list? it says in my notes. nums[0] on [] would crash i think. IndexError
yeah it does, i ran it. the spec says None if there isnt one so ill just return None at the top
if len(nums) == 0: return None

[23] TUTOR: Good prediction, and you checked it by running it. Last thing, and it's quick. Take [2, 9, 9, 9, 4]. Without running it, what does your function return, and why? Then paste your final function. If both look right, you're done.

[27] STUDENT: n=2 second None -> 2 != 9? wait largest starts as 2. n=2 skip. n=9 > 2 so second=2 largest=9. next 9s skipped bc equal to largest. n=4: != 9 and 4 > 2 so second=4. returns 4
ran it, 4. 
```python
def second_largest(nums):
    if len(nums) == 0:
        return None
    largest = nums[0]
    second = None
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n != largest and (second is None or n > second):
            second = n
    return second
```

[28] TUTOR: Your trace is right: 4 is correct, and you got there by tracing, not by guessing. Your function handles all three autograder tests, the empty list, and duplicates. One thing to remember for next time: your first fix failed because `second` started with a real value, and your second one failed because duplicates of `largest` counted as "second". Whenever a test fails, trace a small input by hand before you change anything. Good luck with the submission.

[28] STUDENT: thanks, submitting it

## Session outcome
- Submitted work (verbatim) and whether it is correct:
```python
def second_largest(nums):
    if len(nums) == 0:
        return None
    largest = nums[0]
    second = None
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n != largest and (second is None or n > second):
            second = n
    return second
```
Correct. It passes the three autograder cases and also handles the empty list, all-equal lists, duplicates and negatives.
- Who generated the key reasoning steps (student vs tutor/other bot/notes), with a rough % generated by the student: Student about 70%. The student did every trace, proposed the elif, proposed `None` as the starting value and the `is None` guard, found the duplicate problem and the `n != largest` fix, and picked the empty-list case from his notes. The tutor prompted each step, named the None-comparison crash only as a confirmation, and told him to trace the duplicate case. The tutor wrote no code.
- Elapsed time (minutes): about 28
- If the task mentions other similar homework questions: not applicable
- Student's emotional state at the end: Relieved and a bit pleased. He was briefly irritated at minute 8 when the first elif still failed. He ended calm and finished with time to spare.
- Would the student choose this kind of help again? Why? Probably, with some reluctance. He wanted the code at minute 8 and found the tracing slower than a quick answer. But he fixed the bug in under 30 minutes and felt he understood why it passed, which he would value.
- Did the student leave for an answer bot? If not, how close did they come? No. He came closest at minute 8, when the first elif failed and he asked for the code directly. The tutor declined, and the next question was easy enough that he got moving again within a minute. He was not frustrated enough after that to open another tab.
