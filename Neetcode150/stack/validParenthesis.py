"""Validate Parentheses
Solved 
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.
"""
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
