"""Daily Temperatures
Solved 
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            # if len(stack)>0:
            #     temp_last_index = temperatures[stack[-1]]
            while len(stack)>0 and temp>temperatures[stack[-1]]:
            # while len(stack)>0 and temperatures[i]>temperatures[stack[-1]]:
                last_index = stack.pop()
                res[last_index]= i - last_index
                # temp_last_index = temperatures[i]
            stack.append(i)
        return res
        
sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]
# Input: temperatures = [30,38,30,36,35,40,28]
# print(sol.dailyTemperatures([30,38,30,36,35,40,28]))
# Output: [1,4,1,2,1,0,0]
