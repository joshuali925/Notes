def merge_sort(A, low=0, high=None):
    if high is None:
        high = len(A) - 1

    if low >= high:
        return

    mid = (low + high) // 2

    left = A[low:mid + 1]
    right = A[mid + 1:high + 1]
    
    merge_sort(left)
    merge_sort(right)

    i = j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            A[k] = right[j]
            j += 1
        else:
            A[k] = left[i]
            i += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1


x = [1, 4, 6, 3, 1, 5, 20, 4, 2, 77, 8]
merge_sort(x)
print(x)
