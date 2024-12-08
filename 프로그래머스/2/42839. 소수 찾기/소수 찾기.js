function solution(numbers) {
    var answer = 0;
    const arr = numbers.split('')
    const total = new Set()
    const pur = (current, remain, target) => {
        if (current.length === target ) {
            const str = current.join('')
            total.add(Number(str))
        }
        
        for (let i=0; i<remain.length; i++) {
            current.push(remain[i])
            const newRe = remain.filter((item, idx) => idx !== i)
            pur(current, newRe, target)
            current.pop()
        }
    }
    const prime = (x) => {
        if (x < 2) return false
        const sq = x ** 0.5
        for (let i=2; i <=sq; i++) {
            if (x % i === 0) {
                return false
            }
        }
        return true
        
    }
    for (let i=1; i<=arr.length; i++) {
        pur([], arr, i)
    }
    total.forEach((item) => {
        const dap = prime(item)
        if (dap) {
            answer++
        }
    })
    return answer;
}