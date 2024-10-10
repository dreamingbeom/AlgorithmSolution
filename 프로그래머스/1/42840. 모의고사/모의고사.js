function solution(answers) {
    var answer = [];
    let num1 = [1, 2, 3, 4, 5]
    let num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    let num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let cnt = [0, 0, 0]
    answers.forEach((item, i) => {
        idx1 = i % num1.length
        idx2 = i % num2.length
        idx3 = i % num3.length
        if (item === num1[idx1]) {
            cnt[0] += 1
        }
        if (item === num2[idx2]) {
            cnt[1] += 1
        }
        if (item === num3[idx3]) {
            cnt[2] += 1
        }
    })
    const max = Math.max(...cnt)
    cnt.forEach((item, i) => {
        if (max === item) {
            answer.push(i+1)
        }
    })
    return answer;
}