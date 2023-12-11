function solution(array) {
    var answer = 0;
    const idx = Math.max(...array)
    const set = new Set(array)
    const arr = Array.from(set)
    const total = new Array(idx+1).fill(0)
    
    arr.forEach((item) => {
        let cnt = 0
        array.forEach((tem) => {
            if (tem === item) {
                cnt += 1
            }
        })
        total[item] = cnt
    })
    
    
    const mx = Math.max(...total)
    
    
    const gap = total.filter((item) => item === mx)
    console.log(gap)
    
    if (gap.length > 1) {
        answer = -1
    } else {
        answer = total.indexOf(mx)
    }
    
    

    return answer;
}