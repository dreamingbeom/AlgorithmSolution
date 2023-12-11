def solution(array):
    idx = max(array)
    setarr = set(array)
    arr = list(setarr)
    total = [0] * (idx + 1)
    
    answer = 0
    for i in arr:
        total[i] = array.count(i)
    
    mx = max(total)
    ii = total.count(mx)
    if ii > 1:
        answer = -1
    else:
        answer = total.index(mx)

    return answer