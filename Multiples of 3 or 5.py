def solution(number):
    res = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)
    return sum(res)