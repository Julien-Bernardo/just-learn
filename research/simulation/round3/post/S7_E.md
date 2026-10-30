# Next-day test

## Answers

**1.**

basically same as last night but flipped. < instead of >

```python
def second_smallest(nums):
    if len(nums) == 0:
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

(second starts as None not nums[0] bc otherwise it counts as a real value, and the != smallest is so duplicates dont count as second)

**2.**

- empty list [] -> None (nums[0] would crash otherwise)
- one element [7] -> None
- all the same [4, 4, 4] -> None, no distinct second
- duplicates of the smallest like [2, 2, 5, 3] -> 3, makes sure the duplicate 2 doesnt become second
- two different values [1, 2] -> 2
- negatives [-1, -5, -3] -> -3
- already sorted [1, 2, 3] -> 2
- reverse sorted [3, 2, 1] -> 2

why: these are the edge cases from our notes, they're where it breaks. the sorted/reverse ones check that the order doesnt matter

**3.** trace on [2, 2, 5, 3]

start: smallest=2, second=None

n=2: 2 < 2 no. elif 2 != 2 false -> skip. smallest=2, second=None
n=2: same, skip. smallest=2, second=None
n=5: 5 < 2 no. elif 5 != 2 true and second is None true -> second=5. smallest=2, second=5
n=3: 3 < 2 no. elif 3 != 2 true and 3 < 5 true -> second=3. smallest=2, second=3

returns 3
