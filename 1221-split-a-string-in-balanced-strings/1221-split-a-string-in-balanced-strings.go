func balancedStringSplit(s string) int {
    l, r, n := 0, 0, 0
    
    for i := 0; i < len(s); i++ {
        if s[i] == 'L' {
            l++
        }
        if s[i] == 'R' {
            r++
        }
        if l == r {
            n++
        }
    }
    
    return n
}