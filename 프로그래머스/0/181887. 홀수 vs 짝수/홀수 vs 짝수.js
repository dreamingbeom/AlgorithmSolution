function solution(num_list) {
    var answer = 0;
    let cnt = [0, 0]
    num_list.forEach((item, i) => {
        if (i % 2 === 0) {
            cnt[0] += item
        } else {
            cnt[1] += item
        }
    })
    answer = Math.max(...cnt)
    return answer;
}