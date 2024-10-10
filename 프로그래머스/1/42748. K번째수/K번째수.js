function solution(array, commands) {
    var answer = [];
    commands.forEach((item) => {
        let arr = array.slice(item[0]-1, item[1])
        arr = arr.sort((a, b) => a - b)
        answer.push(arr[item[2]-1])
    })
    return answer;
}