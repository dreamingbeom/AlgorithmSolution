function solution(n, computers) {
    var answer = 0;
    let ghp = new Array(n+1).fill().map(() => [])
    let vis = new Array(n+1).fill(false)
    computers.forEach((arr, idx) => {
        arr.forEach((item, i) => {
            if (idx !== i && item === 1) {
                ghp[idx+1].push(i+1)
            }
        })
    })
    let cnt = 0
    for (let i=1; i <= n; i++) {
        if (vis[i] === true) {
            continue
        }
        let q = []
        q.push(i)
        vis[i] = true
        while (q.length > 0) {
            const num = q.shift()
            for (item of ghp[num]) {
                if (vis[item] === false) {
                    vis[item] = true
                    q.push(item)
                }
            }
        }
        cnt++
        
    }
    return answer = cnt;
}