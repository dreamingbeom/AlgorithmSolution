function solution(n, edge) {
    var answer = 0;
    let gph = new Array(n+1).fill().map(() => {
        return []
    })
    let dis = new Array(n+1).fill(-1)
    edge.forEach((item) => {
        gph[item[0]].push(item[1])
        gph[item[1]].push(item[0])
    })
    dis[1] = 0
    let q = []
    q.push(1)
    
    while (q.length > 0) {
        let current = q.shift()
        for (let i of gph[current]) {
            if (dis[i] === -1) {
                dis[i] = dis[current] + 1
                q.push(i)
            }
        }
        
    }


    let max = Math.max(...dis)
    dis.forEach((item) => {
        if (item === max) {
            answer += 1
        }
    })
    
    return answer;
}