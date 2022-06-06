func numberOfSteps(num int) int {
    step := 0
    
    for num > 0 {
        if num % 2 == 0 {
            step += 1
            num /= 2
        } else {
            step += 1
            num -= 1
        }
    }
    
    return step
}