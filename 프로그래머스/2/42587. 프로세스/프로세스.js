function solution(priorities, location) {
    var answer = 0;
    const arr = priorities.map((item, idx) => [item, idx])
    const prior = [...priorities].sort((a, b) => b - a)
    const comple = []
    let maxP = 0
    
    while (arr.length > 0) {
        const first = arr.shift()
        if (first[0] === prior[maxP]) {
            comple.push(first)
            maxP++
        } else {
            arr.push(first)
        }
    }
    for (let i=0; i < comple.length; i++) {
        if (location === comple[i][1]) {
            answer = i+1
            return answer
        }
    }
    
    
}