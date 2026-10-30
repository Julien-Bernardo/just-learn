# Next-day test

## Answers

**1.**

```python
def second_smallest(nums):
    if not nums:
        return None
    smallest = nums[0]
    second = None
    for n in nums:
        if n < smallest:
            second = smallest
            smallest = n
        elif n != smallest and (second is None or n < second):
            second = n
    return second
```

(the n < second part is the one i messed up before, want the smaller one not the bigger one. so it's < there)

**2.** Test cases:

- `[]` -> None. nums[0] would crash on an empty list so i need the check at the top
- `[7]` -> None. only one element, nothing to be second (my first version just returned the 7 itself)
- `[4, 4, 4]` (all equal) -> None. its distinct so equal ones dont count as a second
- `[2, 2, 5, 3]` / `[3, -2, -2, 9]` (duplicates of the smallest) -> 3. checks that a dupe of the smallest doesn't get counted as second
- negatives, like `[-1, -5, -3]` -> -3. to make sure it doesnt break with negative numbers (like if i had started second at 0 or something)
- already sorted `[1, 2, 3, 4]` -> 2 and reverse sorted `[4, 3, 2, 1]` -> 2. the order changes which if/elif branch runs, so i want to see it works both ways
- `[5, 1, 4]` type one where the number in the middle should become second. that was the first bug i had

**3.** Trace on `[2, 2, 5, 3]`:

start: smallest = 2, second = None

- n = 2: 2 < 2 no. elif 2 != 2 is False so nothing happens. smallest = 2, second = None
- n = 2: same thing, nothing. smallest = 2, second = None
- n = 5: 5 < 2 no. elif 5 != 2 yes and second is None yes, so second = 5. smallest = 2, second = 5
- n = 3: 3 < 2 no. elif 3 != 2 yes, and second is None no, but 3 < 5 yes, so second = 3. smallest = 2, second = 3

returns 3
