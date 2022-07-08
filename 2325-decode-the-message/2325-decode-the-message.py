class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dict = {}
        c = ord('a')
        
        for i in key:
            if i != ' ':
                if i not in key_dict:
                    key_dict[i] = chr(c)
                    c += 1
                    if(c > 122):
                        break
        ans = ''
        for i in message:
            if i == ' ':
                ans += i
            else:
                ans += key_dict[i]
        return ans