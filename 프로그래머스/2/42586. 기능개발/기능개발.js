function solution(progresses, speeds) {
    var answer = [];
    const arr = progresses.reverse()
    const speed = speeds.reverse()
    let i = 10
    while (arr.length > 0) {
        let cnt = 0
        arr.forEach((item, idx) => {
            arr[idx] += speed[idx]
        })
        while (arr[arr.length-1] >= 100) {
            arr.pop()
            cnt += 1
        }
        if (cnt > 0) {
            answer.push(cnt)
        }
        i--
    }
    return answer;
}