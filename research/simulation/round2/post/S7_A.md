# Next-day test

## Answers

**1. second_smallest**

ok this is basically second_largest flipped. flip the > to < and start `second` at something from the list, not 0 (last night 0 broke the negatives). so max(nums) I think

```python
def second_smallest(nums):
    if len(nums) < 2:
        return None
    smallest = nums[0]
    second = max(nums)
    for n in nums:
        if n < smallest:
            second = smallest
            smallest = n
        elif n < second and n != smallest:
            second = n
    if second == smallest:
        return None
    return second
```

(the `!= smallest` is so a repeat of the smallest doesn't get in as second, and the check at the end is for like [2,2,2] where nothing ever changes)

**2. Test cases**

- [] -> None, empty list, nothing to look at (the len check)
- [7] -> None, one element, there's no second
- [2, 2, 2] -> None, all equal, so no DISTINCT second. this one gave me the wrong answer last night til I added the end check
- [2, 2, 5, 3] -> 3, duplicates of the smallest, makes sure the repeat 2 doesn't count as second
- [-5, -1, -3] -> -3, negatives. (this is why I can't start second at 0)
- [1, 2, 3] -> 2, already sorted
- [3, 2, 1] -> 2, reverse sorted
- [5, 1, 4] -> 4, the normal case

**3. Trace on [2, 2, 5, 3]**

len is 4 so it doesn't return None

```
start:  smallest = 2   second = max(nums) = 5
n=2:    2 < 2 no.  2 < 5 yes but 2 != 2 no   -> smallest 2, second 5
n=2:    same as above                        -> smallest 2, second 5
n=5:    5 < 2 no.  5 < 5 no                  -> smallest 2, second 5
n=3:    3 < 2 no.  3 < 5 yes and 3 != 2 yes  -> second = 3, smallest 2
end:    second (3) == smallest (2)? no
return 3
```

answer: 3
