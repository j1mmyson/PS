function solution(number) {
    let answer = 0;
    number = String(number);
    
    for (let i in number) {
        answer += +number[i];
    }
    
    return answer;
}