# Binary Search
```python
def binary_search(A, target):
    low, high = 0, len(A)
    while low < high:
        mid = (low + high) // 2
        if A[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low
```
- loop invariant: `(-inf, low)` are all too small, `[high, inf)` are all too large, `[low, high)` unknown
- while in loop, searches within `[low, high)`
    - `low <= mid < high` is always true
- `low == high` when exits loop
- returns inserting position, `domain = [low, high]`
    - returns first index where `A[index] >= target`
    - or `len(A)` if `A[-1] < target`
    - if `A[mid] >= target`, we then search within `[low, mid)` works because:
        - if `mid` is the first occurrance, loop eventually exits with `low == mid` which is the inserting position

## Search For First Occurrance
- change return to `return low if low < len(A) and A[low] == target else -1`
```python
A = [1, 2, 2, 4, 4, 4, 7, 10]
binary_search(A, 3)  # -1
binary_search(A, 4)  # 3
```

## Search For Last Occurrance
- use `binary_search(A, target + 1) - 1`
    - find inserting position of `target + 1`, then go back one
- **assumes presence** of target
```python
binary_search(A, 4 + 1) - 1  # last 4 is at index 5
```

## Search For Closest Value
```python
def closest_value_index(A, target):
    low = binary_search(A, target)  # A[low - 1] < target <= A[lo]
    left = max(0, low - 1)  # low - 1
    right = min(len(A) - 1, low)  # low
    if abs(target - A[left]) < abs(A[right] - target):
        return left
    return right
```

## Find Peak Element
```python
    ...
    low, high = 1, len(A) - 1
    ...
        if A[mid] < A[mid + 1]:
    ...
```

# Variation
```python
def binary_search2(A, target):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            high = mid - 1
    return low
```
- `low` would be the inserting position
- `high = mid = low - 1` when exits loop
    - `high` can be `-1`
- modify `else` for specific requirements when searching
    - if `A[mid] == target`, move `high` to the left and search towards the left
    - put `low = mid + 1` in `else` when searching for rightmost target
        - `high` would be the index in this case
        - `low` can be out of bounds since its `high + 1`
