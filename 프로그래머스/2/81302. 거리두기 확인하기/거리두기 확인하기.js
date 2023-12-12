


function solution(places) {
    var answer = [];
    places.forEach((arr) => {
        // places의 각 한 원소 arr에 대해서,
        const mat = []
        // 문자열로 나두면 인덱스를 찾기 힘드므로 2차원 행렬로 변형하기 위해 각 문자열요소를 가진
        // 배열을 담을 map 생성
        arr.forEach((item) => {
            // arr의 각 요소 문자열에 대해서,
            ar = item.split('')
            // 문자열을 배열로 만들어줘 => [P, X, O, P, X] 이런식으로 만들어진다
            mat.push(ar)
            // 각요소를 mat에 담아줘  
        })
        Plist = []
            
        for (let i=0; i < 5; i++) {
            for (let j=0; j <5; j++) {
                if (mat[i][j] === 'P') {
                    Plist.push([i,j])
                }
            } 
        }
        
        Pcomlist= []
        // 2중 포문돌면서 P의 인덱스 위치 찾기
        for (let i=0; i < Plist.length; i++) {
            for (let j=i; j < Plist.length; j++) {
                if (i !== j) {
                    Pcomlist.push([Plist[i], Plist[j]])
                }
                
            }
        }
        // P가 2개씩 묶인 조합 찾기
        notlaw = []
        Pcomlist.forEach((item) => {
            if (Math.abs(item[0][0] -item[1][0]) + Math.abs(item[0][1] - item[1][1]) <= 2)  {
                notlaw.push(item)
            }
        })
        
        // 맨해튼거리가 2이하인 친구들은 notlaw에 넣어주기
        let filternotlaw // 상하좌우 필터
        let filternotlawtotal // 상하좌우 필터한 것중 대각선까지
        if (notlaw.length === 0 ) {
            answer.push(1)
            // 만약 모두 거리를 잘지킨다면 1을 입력
        } else {
            filternotlaw = notlaw.filter((item) => {
                // 밑의 코드는 거리두기를 지키지않은 조합들 중, 파티션이 있어서 
                // 알고보니 지키고 있는 친구들을 필터하기 위한 조건문들
                // 파티션을 지킬 수 있는 경우의 수는 8가지 뿐 (2칸띄어진 상하좌우 , 대각선)
                // 먼저 상하좌우로 거리가 2씩 띄어져있으면서 중간에 파티션이 있다면 패스
                // 아니라면 filternotlaw 에 담기게 됨. 이친구들은 답없는 거리두기 안지킴
                if (item[0][0] === item[1][0]) {
                    if (item[0][1] - item[1][1] === 2) {
                        if (mat[item[0][0]][item[0][1]-1] !== 'X') {
                            return item
                        }    
                    } else if (item[0][1] - item[1][1] === -2) {
                        if (mat[item[0][0]][item[0][1]+1] !== 'X') {
                            return item
                            }
                    } else {return item}  
                } else if (item[0][1] === item[1][1]) {
                    if (item[0][0] - item[1][0] === 2) {
                        if (mat[item[0][0]-1][item[0][1]] !== 'X') {
                            return item
                        }
                    } else if (item[0][0] - item[1][0] === -2) {
                        if (mat[item[0][0]+1][item[0][1]] !== 'X') {
                            return item
                        }
                    } else {return item}
                } else {return item}
                // 위에는 상하좌우 체크
                
            })
            filternotlawtotal = filternotlaw.filter((item) => {
                // 왼쪽상
                if (item[0][0]-1 === item[1][0] && item[0][1]-1 === item[1][1] ) {
                    if (!(mat[item[0][0]-1][item[0][1]] === 'X' && mat[item[0][0]][item[0][1]-1] === 'X')) {return item}
                } // 왼쪽하 
                else if (item[0][0]+1 === item[1][0] && item[0][1]-1 === item[1][1]) {
                    if (!(mat[item[0][0]+1][item[0][1]] === 'X' && mat[item[0][0]][item[0][1]-1] === 'X')) {return item }
                } // 오른쪽 상
                else if (item[0][0]-1 === item[1][0] && item[0][1]+1 === item[1][1]) {
                    if (!(mat[item[0][0]-1][item[0][1]] === 'X' && mat[item[0][0]][item[0][1]+1] === 'X')) {return item}
                }
                // 오른쪽 하
                else if (item[0][0]+1 === item[1][0] && item[0][1]+1 === item[1][1]) {
                    if (!(mat[item[0][0]+1][item[0][1]] === 'X' && mat[item[0][0]][item[0][1]+1] === 'X')) {return item}
                } else {return item}
            })
            
        if (filternotlawtotal.length > 0) {
            answer.push(0)
        } else {answer.push(1)}
        }
        
        
        
        
        
    })
    return answer;
}