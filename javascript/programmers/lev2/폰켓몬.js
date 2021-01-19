function solution(nums) {
    var answer = [];
    
    nums.forEach(function(num){
        if(!answer.includes(num)){
            answer.push(num);
        }
    })
    
    answer = nums.length/2 < answer.length ? nums.length/2 : answer.length;
    return answer;
}