class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeOpen = {")" : "(", "}" : "{", "]" : "["}

        for par in s:
            if par in closeOpen:
                if stack and stack[-1] == closeOpen[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        
        return not stack