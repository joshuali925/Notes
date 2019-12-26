# Permutation
- choose `r` items from `nums`
- order matters
```python
def permutation(nums, r):
    ans = []

    def bt(curr, used):
        if len(curr) == r:
            ans.append(curr)
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            bt(curr + [nums[i]], used)
            used[i] = False

    bt([], [False] * len(nums))
    return ans

permutation([1, 2, 3], 2)  # [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
```


# Combination
- choose `r` items from `nums`
- order doesn't matter
```python
def combination(nums, r):
    ans = []

    def bt(curr, pos):
        if len(curr) == r:
            ans.append(curr)
            return

        for i in range(pos, len(nums)):
            bt(curr + [nums[i]], i + 1)

    bt([], 0)
    print(f'ans: {ans}')
    return ans

combination([1, 2, 3], 2)  # [[1, 2], [1, 3], [2, 3]]
```
