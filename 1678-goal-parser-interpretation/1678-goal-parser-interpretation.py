class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        for i in range(len(command)):
            if command[i] == 'G':
                s += command[i]
            elif command[i] == '(' and command[i + 1] == ')':
                s += 'o'
                i += 2
            elif command[i] == '(' and command[i + 1] == 'a' and command[i + 2] == 'l' and command[i + 3] == ')':
                s += 'al'
                i += 3
        return s