def count_positives_sum_negatives(arr):
    if not arr: 
        return []
    x = 0
    b
    y = 0
    for i in arr:
        if i > 0:
            x += 1
        elif i < 0:
            y += i
    return [x, y]

   