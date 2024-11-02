function solution(sizes) {
    var answer = 0;
    let arr = []
    sizes.forEach((item) => {
        item[0] >= item[1] ? arr.push([item[0], item[1]]) : arr.push([item[1], item[0]])
    })
    arr.sort((a, b) => b[0] - a[0])
    let garo = arr[0][0]
    arr.sort((a, b) => b[1] - a[1])
    let sero = arr[0][1]
    answer = garo * sero
    return answer;
}