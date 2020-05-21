def quick_sort(a, first, last):
    if first < last:
        pivot = a[last]
        p = first - 1
        for j in range(first, last + 1):
            if a[j] <= pivot or j == last:
                p += 1
                a[p], a[j] = a[j], a[p]
        
        quick_sort(a, first, p - 1)
        quick_sort(a, p + 1, last)
