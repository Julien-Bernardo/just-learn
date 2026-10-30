# Next-day test

## Answers

**1.**

ok i think its basically the one from last night but flipped. i remember it started with None for both and had an elif

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

(the elif is so numbers that arent a new smallest still get a chance to be second, and the != is so duplicates dont count. i think. could also do sorted(set(nums)) and take [1] if len >= 2 but im not 100% sure on that so going with the loop)

**2.**

test cases:
- [] (empty list, should be None, make sure it doesnt crash)
- [7] (one element, None)
- [3, 3, 3] (all equal, None since no second distinct)
- [5, 1, 4] -> 4 (normal case, like the one from the autograder)
- [2, 2, 5, 3] -> 3 (duplicates of the smallest)
- [1, 2] (just two elements)
- [3, 2, 1] and [1, 2, 3] (reverse sorted and already sorted, order might matter)
- [-1, -5, -3] (negatives)

why: the lecture notes said to test empty, one element, all equal, duplicates, negatives, sorted and reverse sorted so i just went through those. mostly these are the cases where my code might break or return the wrong thing

**3.**

trace on [2, 2, 5, 3]

start: smallest = None, second = None

n = 2: smallest is None so first branch. second = None, smallest = 2
-> smallest 2, second None

n = 2: not < 2. elif: 2 != 2 is False so skip
-> smallest 2, second None

n = 5: not < 2. elif: 5 != 2 true and second is None true, so second = 5
-> smallest 2, second 5

n = 3: not < 2. elif: 3 != 2 true and 3 < 5 true, so second = 3
-> smallest 2, second 3

return 3
