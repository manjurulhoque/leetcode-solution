func isPalindrome(x int) bool {
    reversed := 0
    org := x

    for x > 0 {
        remainder := x % 10
        reversed = reversed * 10 + remainder
        x /= 10
    }

    return org == reversed
}