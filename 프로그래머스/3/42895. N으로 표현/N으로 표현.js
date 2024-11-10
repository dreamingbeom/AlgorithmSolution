function solution(N, number) {
    var answer = 0;
    if (N === number) return 1;
    const dp = Array.from(new Array(9), () => new Set());
    dp[1].add(N);
    for (cnt = 2; cnt <=8; cnt++) {
        dp[cnt].add(Number(String(N).repeat(cnt)))
        
        for (let i=1; i < cnt; i++) {
            for (let first of dp[i]) {
                for (let second of dp[cnt-i]) {
                    dp[cnt].add(first + second)
                    dp[cnt].add(first - second)
                    dp[cnt].add(first * second)
                    dp[cnt].add(first / second)
                }
            }
        }
        if (dp[cnt].has(number)) {
            return cnt
        }
    }
    return -1;
}

