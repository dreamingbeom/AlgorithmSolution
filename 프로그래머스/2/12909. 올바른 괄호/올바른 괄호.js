function solution(s){
    var answer = true;
    const st = []
    for (let i=0; i <s.length; i++) {
        if (s[i] === '(') {
            st.push(s[i])
        } else {
            if (st.length === 0) {
                return false
            } else {
                st.pop()
            }
        }
    }
    
    if (st.length === 0) {
        answer = true
    } else {
        answer = false
    }

    return answer;
}