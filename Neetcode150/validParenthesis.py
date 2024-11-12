def isValid(s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        lastChar = ""
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
                if len(stack) > 0:
                    lastChar = stack[-1]
            else:
                mappingToClose = closeToOpen[c]
                if len(stack) > 0 and  lastChar == mappingToClose:
                    stack.pop()
                    if len(stack) > 0:
                        lastChar = stack[-1]
                else:
                    return False
            
        # for c in s:
            # if c in closeToOpen:
            #     if stack and stack[-1] == closeToOpen[c]:
            #         stack.pop()
            #     else:
            #         return False
            # else:
            #     stack.append(c)

        if not stack:
            return True
        else:
            return False

s="([{}])"
print(isValid(s))
