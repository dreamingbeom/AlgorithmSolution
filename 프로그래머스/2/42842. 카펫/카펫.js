function solution(brown, yellow) {
    var answer = [];
    const s = brown + yellow

    for (let i=1; i <= yellow; i++) {
        if (yellow % i === 0) {
           const g = yellow / i
           if (i >= g && (g+2) * (i+2) === s) {
               return [i+2, g+2]
           }
        }
    }
    return answer;
}