func subtractProductAndSum(n int) int {
    p_d := 1
    s_d := 0
    
    for n > 0 {
        m := n % 10
        p_d *= m
        s_d += m
        n = n / 10
    }
    return p_d - s_d
}