function solution(k, dungeons) {
    var answer = -1;
    
    const per = (arr, selectNumber) => {
        const result = []
        if (selectNumber === 1) return arr.map((el) => [el])
        
        arr.forEach((el, idx, origin) => {
            const rest = origin.filter((item, i) => i !== idx )
            const permutations = per(rest, selectNumber-1)
            const attached = permutations.map((permutation) => [el, ...permutation])
            result.push(...attached)
        })
        return result
    }
    const res = per(dungeons, dungeons.length)
    let max = 0
    res.forEach((arr) => {
       let cnt = 0
       let copy = k
       for (let i=0; i < arr.length; i++) {
           if (copy >= arr[i][0]) {
               copy -= arr[i][1]
               cnt += 1
           } else {
               break
           }
       }
        max = Math.max(max, cnt)
    })
    
    return answer = max;
}