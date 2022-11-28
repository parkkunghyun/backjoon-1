function solution(k, score) {
    var answer = [];
    var answerDay = []
    
    for (let i =0; i<score.length; i++) {
        if (answer.length >=k) {
            if (answer[0] >score[i]) { answerDay.push(answer[0]) }
            else {
                //console.log(answer)
                answer.shift()
                answer.push(score[i])
                answer.sort((a,b)=> {
                    return a-b;
                })
                //console.log(answer)
                answerDay.push(answer[0])
            }
        }else{
            answer.push(score[i])
            answer.sort((a,b)=> {
                    return a-b;
                })
            answerDay.push(answer[0])
        }
    }
    return answerDay;
}