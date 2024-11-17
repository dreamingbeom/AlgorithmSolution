function solution(n, times) {
    var answer = 0;
    const sorted = times.sort((a, b) => a - b)
    let res = -1
    let start = 1
    let end = sorted[sorted.length-1] * n
    
    while (start <= end) {
        let mid = Math.floor((start + end) / 2)
        let man = sorted.reduce((cnt, time) => cnt + Math.floor(mid /time), 0)
        
        if (man >= n) {
            res = mid
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    
    return res;
}