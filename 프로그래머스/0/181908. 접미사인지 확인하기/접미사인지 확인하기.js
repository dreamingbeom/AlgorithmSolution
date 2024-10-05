function solution(my_string, is_suffix) {
    var answer = 0;
    for (let i=0; i < my_string.length; i++) {
        const str = my_string.slice(i, my_string.length)
        if (str === is_suffix) {
            return 1
        }
    }
    return answer;
}