function solution(answers) {
    var answer = [];
    const num1 = [1, 2, 3, 4, 5]
    const num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    const num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let cnt = [0, 0, 0]
    answers.forEach((item, idx) => {
        if (item === num1[idx%5]) {
            cnt[0] += 1
        }
        if (item === num2[idx%8]) {
            cnt[1] += 1
        }
        if (item === num3[idx%10]) {
            cnt[2] += 1
        }
    })
    let max = Math.max(...cnt)
    cnt.forEach((item, idx) => {
        if (item === max) {
            answer.push(idx+1)
        }
    })
    return answer;
}