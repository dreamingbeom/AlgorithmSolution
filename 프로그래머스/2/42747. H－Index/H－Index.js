function solution(citations) {
    var answer = 0;
    const len = citations.length
    const arr = citations.sort((a, b) => b - a)
    // 0 1 3 5 6
    // 0 1 2 3 4
    for (let i=0; i<len; i++) {
        
        if (i < arr[i]) {
            answer += 1
        }
        
    }
    return answer;
}