func twoSum(nums []int, target int) []int {
    n := len(nums)

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if i != j && nums[i] + nums[j] == target {
                return []int{i, j}
            }
        }
    }

    return []int{}
}