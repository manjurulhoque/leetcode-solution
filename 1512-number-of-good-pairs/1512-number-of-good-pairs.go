func numIdenticalPairs(nums []int) int {
    count := 0
    ln := len(nums)
    // fmt.Println(ln)
    for i := 0; i < ln; i++ {
        for j := i + 1; j < ln; j++ {
            // fmt.Println(nums[i])
            if nums[i] == nums[j] {
                count += 1
            }
        }
    }
    
    return count
}