def partition(lst, lo, hi):
    if len(lst) == 0:
        return 0

    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]

    return hi
def rec_qsort(lst, lo, hi):
    global height
    if lo < hi:
        pivot = partition(lst, lo, hi)
        print(lst[pivot])
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    global height
    height = 0
    rec_qsort(lst, 0, len(lst) - 1)
    return height
