# Next-day test

## Answers

**1.**

```python
def second_smallest(nums):
    smallest = float('inf')
    second = float('inf')
    for n in nums:
        if n < smallest:
            second = smallest
            smallest = n
        elif n < second and n != smallest:
            second = n
    if second == float('inf'):
        return None
    return second
```

its the same as second_largest but flipped. start both at inf (bigger than everything) instead of -inf, and < instead of >. skip dupes of the smallest with n != smallest. if second never changed from inf then theres no second distinct value so return None

**2.**

test cases:
- [] -> None. empty list, make sure it doesnt crash
- [7] -> None. only one element
- [4, 4, 4] -> None. all the same so no second distinct value
- [5, 5, 3] and [3, 5, 5] -> 5. duplicates, and dupes of the smallest shouldnt count as the second. also check both orders
- [1, 2, 3, 4] -> 2. already sorted
- [4, 3, 2, 1] -> 2. reverse sorted
- [-1, -2] -> -1. negatives (this is why you start at inf and not 0)
- [2, 1] -> 2. two elements that are different

basically the stuff from the lecture notes list, empty, one element, all equal, duplicates, negatives, sorted / reverse sorted

**3.**

trace on [2, 2, 5, 3]

start: smallest = inf, second = inf

n = 2: 2 < inf yes so second = inf, smallest = 2
-> smallest = 2, second = inf

n = 2: 2 < smallest? 2 < 2 no. elif 2 < inf yes but 2 != 2 is false so nothing
-> smallest = 2, second = inf

n = 5: 5 < 2 no. elif 5 < inf and 5 != 2 yes so second = 5
-> smallest = 2, second = 5

n = 3: 3 < 2 no. elif 3 < 5 and 3 != 2 yes so second = 3
-> smallest = 2, second = 3

loop done. second is 3, not inf, so return 3

final answer: 3
