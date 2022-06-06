func xorOperation(n int, start int) int {
    c := 0
    
    for i := 0; i < n; i++ {
        c ^= (start + 2 * i)
    }
    return c
}