function solution(array) {
    var answer = 0;
    array.sort((a, b) => a - b)
    const len = array.length
    let index = Math.floor(len / 2)
    console.log(array)
    answer = array[index]
    
    return answer;
}