function solution(triangle) {
    var answer = 0;
    for (let i=triangle.length-2; i >= 0; i--) {
        for (let j=0; j < triangle[i].length; j++) {
            triangle[i][j] += Math.max(triangle[i+1][j], triangle[i+1][j+1])
        }
    }
    return answer = triangle[0][0];
}