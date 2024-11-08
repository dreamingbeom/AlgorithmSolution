function solution(array, commands) {
    var answer = [];
    commands.forEach((item) => {
        let [i, j, k] = item
        let arr = array.slice(i-1, j)
        arr = arr.sort((a, b) => a - b)
        answer.push(arr[k-1])
    })
    return answer;
}