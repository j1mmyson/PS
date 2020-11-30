func solution(n int) int64 {
    var num1 int64
    var num2 int64
    num1 = 0
    num2 = 1
    
    if n ==1{
        return 0
    }
    if n == 2{
        return 1
    }
    
    for i := 1; i<n; i++{
        num1, num2 = num2 % 1234567, num1+num2 % 1234567    
    }
    
    return num2 % 1234567
}
