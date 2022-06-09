class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        arr = [num]
        
        for i in range(len(s)):
            if s[i] == '9':
                list1 = list(s)
                list1[i] = '6'
                str1 = ''.join(list1)
                arr.append(int(str1))
            elif s[i] == '6':
                list1 = list(s)
                list1[i] = '9'
                str1 = ''.join(list1)
                arr.append(int(str1))
        
        return max(arr)