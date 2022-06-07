func smallerNumbersThanCurrent(nums []int) []int {
    n, ln := 0, len(nums)
    var smaller []int
    
    for i := 0; i < ln; i++ {
        n = 0
        for j := 0; j < ln; j++ {
            if i != j && nums[j] < nums[i] {
                n++
            }
        }
        smaller = append(smaller, n)
    }
    
    return smaller
}