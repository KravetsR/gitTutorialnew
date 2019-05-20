def count_positives_sum_negatives(arr):
    positive_num =[]
    negative_num = []
    result = []
    for x in arr:
        if x>0:
            positive_num.append(x)
            p = len(positive_num)
        elif x<0:
            negative_num.append(x)
            n = sum(negative_num)
    result.append(p)
    result.append(n)
    return result