def selection_sort(lst):
    count = 0
    moves = 0
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):
            count += 1
            if lst[j] < lst[min_index]:
                min_index = j
        # place smallest at the beginning (swap min index with i)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        moves += 1
        return(count,moves)