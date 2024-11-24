function solution(numbers) {
    var answer = '';
    let arr = numbers.sort((a, b) => {
        let strA = String(a)
        let strB = String(b)
        return Number(strB+strA) - Number(strA+strB)
    })
    answer = arr[0] === 0 ? "0" : arr.join('')
    
    return answer;
}