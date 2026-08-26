func intToRoman(num int) string {
    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	symbols := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}

    n := len(values)
    var result strings.Builder

    for i := 0; i < n; i++ {
        for num >= values[i] {
            num -= values[i]
            result.WriteString(symbols[i])
        }
    }

    return result.String()
}