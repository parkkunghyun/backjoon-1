
function solution(s){
    var answer = false;
    let stack = 0
    for (let i of s) {
        if (i == ')' && stack==0 ) {
            return answer
        }
        if (i == '(') {
            stack +=1
        }
        if (i == ')'){
            stack -=1
        }
        //console.log(stack)
    }
    if (stack ==0){
        answer = true
    }
    // 1. )부터 들어오는 경우 -> false
    // 2, (개 남는 경우 -> false
    // 3. )개 (보다 많은 경우 

    return answer;
}