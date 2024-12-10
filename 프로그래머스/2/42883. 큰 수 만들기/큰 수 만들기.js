function solution(number, k) {
    var answer = '';
    const s = []
    for (let num of number) {
        while (k > 0 && s[s.length-1] < num) {
            s.pop()
            k--
        }
        s.push(num)
    }
    
    s.splice(s.length-k, k)
    answer = s.join('')
    return answer;
}