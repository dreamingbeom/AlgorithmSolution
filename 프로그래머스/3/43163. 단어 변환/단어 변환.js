function solution(begin, target, words) {
    var answer = 0;
    const vis = {}
    words.forEach((item) => {
        vis[item] = false
    })
    const isConnected = (str1, str2) => {
        let cnt = 0
        for (let i=0; i < str1.length; i++) {
            if (str1[i] !== str2[i]) {
                cnt += 1
            }
        }
        return cnt === 1 ? true : false
    }

    vis[begin] = 0
    const bfs = (start) => {
        let q = []
        q.push(start)
        while (q.length > 0) {

            const str = q.shift()          
            words.forEach((item, idx) => {
            let res = isConnected(str, item)
            if (res && vis[item] === false) {
                vis[item] = vis[str] + 1
                q.push(item)
        }
    })
            
          
        }
    }
    bfs(begin)
    console.log(vis)
    if (vis[target]) {
        answer = vis[target]
    } else {
        answer = 0
    }
    return answer;
}