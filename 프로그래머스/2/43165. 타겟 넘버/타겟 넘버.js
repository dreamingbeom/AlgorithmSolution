function solution(numbers, target) {
    var answer = 0;
    const dfs = (arr, target, temp = [], idx = 0) => {
        if (temp.length === arr.length) {
            
            let gap = 0
            temp.forEach((item) => {
                gap += item
            })
            if (gap === target) {
                answer += 1
            }
            return
        }
        temp.push(arr[idx])
        dfs(arr, target, temp, idx+1)
        temp.pop()
        
        temp.push(-arr[idx])
        dfs(arr, target, temp, idx+1)
        temp.pop()
    }
    dfs(numbers, target)
    return answer;
}