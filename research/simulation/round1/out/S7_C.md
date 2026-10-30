# Session S7

## Transcript

[0 min]

STUDENT: hey my second_largest function is failing the autograder, due in 2 hrs. heres the code
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
fails: second_largest([5, 1, 4]) expected 4 got 5, second_largest([5, 5, 3]) expected 3 got 5, second_largest([7]) expected None got 7. can u fix it

TUTOR: Happy to help, and two hours is plenty to get this sorted. Before I say anything: what have you tried so far, and what do you think is happening on the first failing test, [5, 1, 4]?

[3 min]

STUDENT: i tried changing second to 0 and then to nums[1] and stuff but then a different test broke so i changed it back. idk. for [5,1,4] largest would be 5 and second is... 5? which is wrong

TUTOR: Thanks, that's useful. Switching things and rerunning can work sometimes, but it didn't tell you why it broke. Your notes suggest a different approach: trace the code by hand and write down each variable after every step. Can you do that for [5, 1, 4]? What are largest and second after each value of n?

[6 min]

STUDENT: ok
start: largest=5 second=5
n=5: 5>5 no
n=1: 1>5 no
n=4: 4>5 no
so nothing ever changes and it returns 5

TUTOR: Yes, that trace is exactly right. So in the correct answer second should be 4. Look at what happens when n=4 comes in. What should the code do with it, and is there a line that does that?

[9 min]

STUDENT: oh the if only checks if its bigger than largest. 4 isnt so it just gets skipped. i need another case, like elif n > second then second = n

TUTOR: Good, you found the missing case yourself. Add that elif and run [5, 1, 4] by hand again before you run it on the computer. What do you predict you'll get?

[12 min]

STUDENT: i added it and ran it, still gives 5 lol. 4 > second and second is 5 so false

TUTOR: Right, so the new line is there but it never fires. Look at the value second starts with. What's the problem with starting it at nums[0]?

[15 min]

STUDENT: oh its already as big as the largest so nothing can beat it. so it should start lower. 0?

TUTOR: Starting lower is the right idea. Test your 0 on a list like [-3, -8, -5]. What would your function give, and is that okay?

[18 min]

STUDENT: second would stay 0 which isnt even in the list. so thats wrong. maybe None? then i need to check if second is None first
```python
def second_largest(nums):
    largest = None
    second = None
    for n in nums:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif second is None or n > second:
            second = n
    return second
```

TUTOR: Nice, that handles negatives, and you chose None because of a case you thought through. Go ahead and run it against the autograder tests and tell me what you see.

[22 min]

STUDENT: [5,1,4] passes and [7] passes now. [5,5,3] fails, gets 5 expected 3. idk why

TUTOR: Two out of three is real progress. You know how to find out why: trace [5, 5, 3] and write down largest and second after each n. Start with the first 5 and then the second 5.

[25 min]

STUDENT: n=5: largest None so largest=5 second=None
n=5: not > 5 so goes to elif, second is None so second=5
n=3: 3>5 no, goes to elif but 3 > 5 no
returns 5. oh the second 5 got put in as second. but its the same number as largest so it doesnt count

TUTOR: That's it, you spotted exactly where it goes wrong. The problem says the second largest must be a distinct value. What would you need to add to the elif so a repeat of the largest gets ignored?

[28 min]

STUDENT:
```python
        elif n != largest and (second is None or n > second):
            second = n
```
that passes all 3 now

TUTOR: Congratulations, that's the fix, and you got there by tracing instead of random changes. Before you submit, can you put the key idea in one sentence? What was wrong with the original and what did you change?

[30 min]

STUDENT: second started as the same as largest so it could never be updated, so now it starts as None and only updates for numbers that are different from largest and bigger than second

TUTOR: Good summary. One twist before you go: what does your final function return for [3, 9, 9, 9]? Work it out by hand first, then check it.

[32 min]

STUDENT: n=3: largest=3 second=None. n=9: 9>3 so second=3 largest=9. then 9s: not > 9, elif n != largest is false so skip. returns 3. ran it and it gives 3

TUTOR: Correct. For tomorrow, try writing second_smallest from scratch without looking at this chat, and then list the test cases you'd use to check it. Why those cases?

[34 min]

STUDENT: ok ill try it later, need to submit this first. thx

TUTOR: Sounds good. Come back if you get stuck, and good luck with the submission.

## Session outcome
- Submitted work (verbatim) and whether it is correct:
```python
def second_largest(nums):
    largest = None
    second = None
    for n in nums:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif n != largest and (second is None or n > second):
            second = n
    return second
```
Correct. It handles duplicates, fewer than 2 distinct values (empty list, one element, all equal) and negatives, and it passes all three autograder cases.
- Who generated the key reasoning steps (student vs tutor/notes), with a rough % generated by the student: Student about 75%. Notes and tutor supplied the strategy of tracing by hand, the prompt to look at second's starting value, the negatives test, and the "distinct" reminder. Student wrote all traces and all code, and found the missing elif, the None initialisation, and the != check.
- Elapsed time (minutes): about 34
- Student's emotional state at the end: Relieved and somewhat satisfied. He mostly wants to submit, and is a bit surprised that tracing found the bug quickly.
- Would the student choose this kind of help again? Why? Probably yes, for this kind of bug. It was slower than being handed the fix, but he finished with working code that he wrote. He would grumble if it were closer to the deadline.
- If an unrestricted AI chatbot that just gives answers had been one tab away, would this student have switched to it during this session? Why? Probably, at least once. Around minute 12 (the added elif still returned 5) and again at minute 22 (the duplicate case failing) he was close to pasting everything into a chatbot. The questions were short and each one kept him moving, and the deadline was not tight, so he stayed. Under a tighter deadline he would have switched.

## Post-test (next day: no notes, no help, no AI)

Q1.
```python
def second_smallest(nums):
    smallest = None
    second = None
    for n in nums:
        if smallest is None or n < smallest:
            second = smallest
            smallest = n
        elif n != smallest and (second is None or n < second):
            second = n
    return second
```
(Sam's note on the paper: "same as yesterday but flipped the > to <. started at None bc starting at nums[0] doesnt work, and the != so dupes dont count")

Q2.
Test cases:
- [3, 1, 2]: normal case, should give 2
- [1, 1, 2]: duplicate of the smallest, should give 2 and not 1
- [5]: only one element, should be None
- []: empty list, should be None
- [2, 2, 2]: all the same, should be None
- [-1, -5, -3]: negatives, to check it doesn't depend on starting at 0

Q3. Trace on [4, 4, 2, 9]:
```
start:   smallest=None second=None
n=4:  smallest is None -> second=None, smallest=4
n=4:  4<4 no. 4 != 4 false -> skip.  smallest=4 second=None
n=2:  2<4 yes -> second=4, smallest=2
n=9:  9<2 no. 9 != 2 true, but second is 4 and 9<4 false -> skip
return second = 4
```
Answer: 4

## Post-test marking
- Q1: correct. It is the mirrored version of the function from the session, with None initialisation and the != check, and it works for normal lists, duplicates, and lists with fewer than 2 distinct values.
- Q2: partly correct. It includes duplicates of the min, single element, empty, all equal and negatives, but gives no case where the answer appears first in the list (or is otherwise in an awkward position), and the reasons are brief.
- Q3: correct. Every step is right and it ends with 4.
- Total: 2/3 correct, with Q2 partly correct (about 2.5/3).

## Simulator's note
I was unsure how much of the structure of the final function Sam would remember a day later without notes. I assumed it would carry over because he built it by iterating on his own code and traced the same pattern twice, and that the "answer appears first" test case would be missed because it was never discussed. The edge-case list in Q2 probably comes more from the lecture notes than from this session.
