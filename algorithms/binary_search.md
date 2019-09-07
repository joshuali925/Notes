# Integer Binary Search
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
- while in loop, searches `[low, high)` (i.e. `low <= mid < high`)
- `low == high` when exits loop
- returns inserting position, a integer in `[low, high]`
    - first index where `A[index] >= target`
    - or `len(A)` (`high`) if `A[-1] < target`
- modify `if` to get first index where `if` is false
    - find peak element
    - TODO: peak

## Search For First Occurrance
- change return to `return low if A[low] == target else -1`
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
