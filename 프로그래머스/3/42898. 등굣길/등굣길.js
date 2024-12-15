function solution(m, n, puddles) {
    const mat = new Array(n+1).fill(0).map(() => new Array(m+1).fill(0))
    puddles.forEach((item) => {
        mat[item[1]][item[0]] = -1
    })
    
    mat[1][1] = 1
    
    for (let i=1; i <= n; i++) {
        for (let j=1; j <= m; j++) {

            if (mat[i][j] === -1 || (i === 1 && j === 1)) {
                continue
            }
            
            if (mat[i-1][j] > 0) {
                mat[i][j] += mat[i-1][j] % 1000000007
            }
            if (mat[i][j-1] > 0) {
                mat[i][j] += mat[i][j-1] % 1000000007
            }
            
        }
    }
    
    return mat[n][m] % 1000000007;
}