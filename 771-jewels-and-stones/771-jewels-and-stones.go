func numJewelsInStones(jewels string, stones string) int {
    c := 0
    
    for _, ch := range stones {
        if strings.Contains(jewels, string(ch)) {
            c += 1
        }
    }
    
    return c
}