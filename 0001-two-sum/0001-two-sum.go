func twoSum(nums []int, target int) []int {
    arr := []int{}

    for i := 0; i < len(nums); i++ {
        for j := 0; j < len(nums); j++ {
            if i != j && nums[i] + nums[j] == target {
                arr = append(arr, i)
                arr = append(arr, j)
                return arr
            }
        }
    }

    return []int{}
}