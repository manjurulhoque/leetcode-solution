func romanToInt(s string) int {
    roman := map[byte]int{
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
    }

    res := 0
    n := len(s)

    for i := 0; i < n; i++ {
        if i + 1 < n && roman[s[i]] < roman[s[i + 1]] {
            res += roman[s[i + 1]] - roman[s[i]]
            i++
        } else {
            res += roman[s[i]]
        }
    }

    return res
}