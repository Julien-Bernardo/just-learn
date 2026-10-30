# Session S7

## Transcript

[0] STUDENT: my second_largest function keeps failing the autograder and its due in 2 hrs. can u fix it

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
failures:
second_largest([5, 1, 4]) expected 4 got 5
second_largest([5, 5, 3]) expected 3 got 5
second_largest([7]) expected None got 7

[0] TUTOR: Happy to help you get this sorted, and 2 hours is plenty if we're efficient. I'd rather help you see the bug than just hand you a fix, since you'll need to do this kind of thing on your own on the exam. First: what have you tried so far, and what do you think the code is doing when it gets [5, 1, 4]?

[2] STUDENT: i tried changing second = nums[1] and also >= instead of > but its still failing. it just returns 5. idk why

[3] TUTOR: Thanks, that helps. Changing a line and rerunning is a normal first move, but here it's a bit like guessing in the dark. Try this instead: go through [5, 1, 4] by hand, one loop step at a time, and write down what largest and second are after each step. What do you get?

[6] STUDENT: ok. start largest=5 second=5. n=5 not > largest so nothing. n=1 no. n=4 no. so returns 5. so second never changes lol

[7] TUTOR: Yes, that's exactly it. Nice, you found it by tracing instead of guessing. The only thing that ever changes second is the `if n > largest` branch. Look at the 4: it's not bigger than largest, but it's still the answer we want. What do you think the code should do when it sees a number like that?

[9] STUDENT: update second if its bigger than second? like elif n > second: second = n

[10] TUTOR: Good idea, that's the missing piece. Before you run it, predict: with that elif added, what happens on [5, 1, 4]? Trace it the same way.

[12] STUDENT: n=1: 1>5 no. n=4: 4>5 no. still 5. oh. second starts at 5 so nothing can beat it

[13] TUTOR: Exactly. Second starts out equal to the biggest thing, so nothing is ever allowed to replace it. So what should second start as, so that the first real number it sees can beat it?

[15] STUDENT: 0?

[16] TUTOR: Reasonable thought. Test it in your head on [-3, -5, -8]. What would your function return?

[18] STUDENT: 0 which is wrong ok. ugh can u just tell me what to put, i dont have all day

[19] TUTOR: I get the time pressure. I'm not going to hand it over, because the next problem like this on a test won't have me around, and you're one idea away. Here's a nudge: you need a starting value that's smaller than any number that could ever be in the list. Python has a way to write "smaller than everything", or you could use a value that means "nothing yet". What could you use?

[21] STUDENT: None maybe? or -infinity. ill try none

[24] STUDENT: got an error

```python
def second_largest(nums):
    largest = None
    second = None
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second:
            second = n
    return second
```
TypeError: '>' not supported between instances of 'int' and 'NoneType'

[24] TUTOR: Good, you tried it, and errors like this are useful. Read it closely: which comparison is failing, and why can't Python do it?

[26] STUDENT: n > largest. largest is None at the start and u cant compare a number to None. so none wont work unless i add extra checks. -inf is easier

[26] TUTOR: Either works, and picking the simpler one is a fair call. Go ahead and switch to -inf. Before you run it, which of your three failing tests do you expect to pass now?

[28] STUDENT: [5,1,4] i think. not sure about the others

```python
def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second:
            second = n
    return second
```
ran it. [5,1,4] gives 4 now. [5,5,3] gives 5 and [7] gives -inf

[29] TUTOR: Your prediction was right, and [5,1,4] is fixed, so that's real progress. Take [5, 5, 3] and trace it. What's second right after the second 5 is processed, and why?

[32] STUDENT: first 5: second=-inf largest=5. second 5: not > largest so goes to elif, 5 > -inf yes so second=5. oh its the same as largest. so i need n != largest in the elif

[33] TUTOR: Yes, that's the bug. Duplicates of the largest are sneaking in as the second largest. Add it and run it. Then look at what [7] gives you. What do you want it to give, and what's different about that list?

[36] STUDENT: added it, [5,5,3] passes now. [7] gives -inf but should be None. theres no second distinct value so second never changed from -inf. so at the end if second is still -inf return None

```python
def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n
    if second == float('-inf'):
        return None
    return second
```
all 3 pass

[37] TUTOR: That's right, and your reasoning for the None case is exactly why it works. The autograder probably has hidden tests beyond those three, though. Name two or three inputs you'd want to try before submitting, and run them.

[40] STUDENT: empty list, all the same like [4,4,4], negatives. ran them. [] gives None, [4,4,4] gives None, [-1,-2] gives -2

[41] TUTOR: Those are the right ones, and all three results are correct. Last step: in one sentence, what's the key idea behind the fix?

[43] STUDENT: second needs its own starting value thats smaller than everything, and you have to skip duplicates of the largest. and trace it instead of guessing

[44] TUTOR: That's a solid summary. Quick twist to check it stuck: what if duplicates DID count, so [5, 5, 3] should return 5? What would you change in your function?

[46] STUDENT: just take out the != largest part? i think

[46] TUTOR: Maybe, but don't trust "i think". Trace [5, 5, 3] and [3, 5, 5] and tell me what you get.

[49] STUDENT: [5,5,3]: first 5 second=-inf largest=5. second 5 elif 5 > -inf so second=5. 3 no. returns 5 good. [3,5,5]: 3 -> largest=3. 5 -> second=3 largest=5. 5 -> elif 5>3 so second=5. returns 5 good. ok thx gonna submit

[49] TUTOR: Both traces are right, and you checked it by tracing instead of rerunning. Good luck with the submission.

## Session outcome
- Submitted work (verbatim) and whether it is correct:
```python
def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n
    if second == float('-inf'):
        return None
    return second
```
Correct. It passes all three autograder cases, plus [], [4,4,4] and [-1,-2]. A list that contains float('-inf') itself would be a theoretical edge case, but that is not an expected test.
- Who generated the key reasoning steps (student vs tutor/other bot/notes), with a rough % generated by the student: About 75% student. The student did the traces, spotted that second never updates, proposed the elif, saw that second starts too high, chose -inf after reading the TypeError, found the n != largest fix, and reached the None return. The tutor supplied the traced-input prompts, the nudge toward "smaller than everything / None" after the student asked to be told, and the idea of checking edge cases beyond the failing tests.
- Elapsed time (minutes): about 49 (marker times show roughly 49 minutes from first message to submission)
- If the task mentions other similar homework questions: not applicable
- Student's emotional state at the end: Relieved and mildly satisfied. He passes the autograder with time to spare, but is a bit worn down by how long it took.
- Would the student choose this kind of help again? Why? Probably yes, with reservations. He got working code he understands and needed less than the 2 hours. The step-by-step questioning annoyed him at the "just tell me" point, and he would likely want it faster if the deadline were tighter.
- Did the student leave for an answer bot? If not, how close did they come? No. He came closest at [18], when he asked to just be told what to put and mentioned the time pressure. He was already making progress by then and had enough time left, so he stayed.
