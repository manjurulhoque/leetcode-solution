func absDiffInt(x, y int) int {
   if x < y {
      return y - x
   }
   return x - y
}

func countKDifference(nums []int, k int) int {
    n := 0
    
    for i := 0; i < len(nums); i++ {
        for j := 0; j < len(nums); j++ {
            if i < j && absDiffInt(nums[i], nums[j]) == k {
                n++
            }
        }
    }
    
    return n
}