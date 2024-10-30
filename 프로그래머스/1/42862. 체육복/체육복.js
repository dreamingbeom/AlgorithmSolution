function solution(n, lost, reserve) {
    var answer = 0;
    let arr = new Array(n+2).fill().map((item) => [false, 0])
    lost.sort((a, b) => a - b)
    arr.forEach((item, idx) => {
        if (!lost.includes(idx)) {
            item[0] = true
        }
    })
    reserve.forEach((item) => {
        if (!lost.includes(item)) {
         arr[item][1] = 1   
        } else {
            arr[item][0] = true
        }
    })
    
    
    for (let i=0; i < lost.length; i++) {
        let idx = lost[i]
        if (arr[idx-1][1] === 1) {
            arr[idx][0] = true
            arr[idx-1][1] = 0
            continue
        }
        if (arr[idx+1][1] === 1) {
            arr[idx][0] = true
            arr[idx+1][1] = 0
        }
    }
    
    
    arr.forEach((item) => {
        if (item[0]) {
            answer += 1
        }
    })
    
    answer -= 2
    return answer;
}
