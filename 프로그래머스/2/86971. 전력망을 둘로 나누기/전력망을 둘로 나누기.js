function solution(n, wires) {
    var answer = -1;
    const node = []
    for (let i=0; i <= n; i++) {
        node.push([])
    }
    wires.forEach(([start, end]) => {
        node[start].push(end)
        node[end].push(start)
    })
    let total = 1000000
    const bfs = (target, ex) => {
        let cnt = 0
        const vis = new Array(n+1).fill(false)
        vis[target] = true
        const q = [target]
        while (q.length) {
            let start = q.shift()
            node[start].forEach((item) => {
             if (item !== ex && vis[item] === false) {
                vis[item] = true
                q.push(item)
            }               
            })
        }
        let cntt = vis.filter(x => x === true).length
        let cntf = n - cntt 
        cnt = Math.abs(cntt - cntf)
        return cnt
    }
    wires.forEach(([a, b]) => {
        const ansa = bfs(a, b)
        const ansb = bfs(b, a)
        total = Math.min(total, ansa, ansb)
    })
    answer = total

    return answer;
}