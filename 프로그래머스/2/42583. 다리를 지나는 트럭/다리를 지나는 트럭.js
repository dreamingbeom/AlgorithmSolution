function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let cnt = 0
    let currentWeight = 0
    const len = truck_weights.length
    const s1 = []
    const s2 = []
    while (len !== s1.length) {
        cnt++
        if (s2.length > 0 && cnt - s2[0][1] === bridge_length) {
            const hasTruck = s2.shift()
            currentWeight -= hasTruck[0]
            s1.push(hasTruck)
        }

        if (currentWeight + truck_weights[0] <= weight) {
           const truck = truck_weights.shift()
           currentWeight += truck
            s2.push([truck, cnt])
        }
        
        
        
    }
    
    return answer = cnt;
}