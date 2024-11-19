function solution(name) {
    var answer = 0;
    let len = name.length
    let move = len - 1
    for (let i=0; i < len; i++) {
        answer += Math.min(name[i].charCodeAt() - 65, 91 - name[i].charCodeAt())
        let index = i + 1
        while (index < len && name[index] === 'A') {
            index++
        }
        move = Math.min(move, i * 2 + len - index);

        move = Math.min(move, (len - index) * 2 + i);
    }
    return answer + move;
}