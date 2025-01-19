function solution(n, wires) {
    var answer = 10000000;
    
    const tree = new Array(n+1).fill().map(() => [])
    wires.forEach((item) => {
        const [s, e] = item
        tree[s].push(e)
        tree[e].push(s)
    })
    const bfs = (start, notS, notE, vis) => {
        const q = []
        let cnt = 0
        q.push(start)
        while (q.length > 0) {
            const s = q.shift()
            vis[s] = true
            cnt += 1
            tree[s].forEach((e) => {
                if (vis[e] === false &&
                    !(s === notS && e === notE) &&
                    !(s === notE && e === notS)
                    ) {
                    
                    q.push(e)
                }
            })
        }
        return cnt 
    }
    for (let i=0; i < wires.length; i++) {
        const [notS, notE] = wires[i]
        const total = []
        const vis = new Array(n+1).fill(false)
        for (let j=1; j <= n; j++) {
            if (vis[j] === false) {
                const cnt = bfs(j, notS, notE, vis)
                if (cnt !== 0) {
                    total.push(cnt)
                }
            }
        }
    total.sort((a, b) => b - a)
    answer = Math.min(answer, total[0] - total[1])
    }
    
    return answer;
}
    