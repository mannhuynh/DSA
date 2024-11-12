class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        result = 0
        while l < r:
            h_l = height[l]
            h_r = height[r]
            if h_l < h_r:
                l += 1
                max_l = max(h_l, max_l)
                result += (max_l - h_l)
            else:
                r -= 1
                max_r = max(h_r, max_r)
                result += (max_r - h_r)    
        return result


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))       



"""
The code you provided is a solution to the "Trapping Rain Water" problem on LeetCode. Here's a breakdown of how it works:

Problem Statement:

Given an array height representing the heights of buildings in a row, where the water can only be trapped between two adjacent buildings if their height difference exceeds the current maximum height of the left and right buildings, calculate the total amount of rainwater that can be trapped.

Code Explanation:

The code uses a simple yet efficient approach to solve this problem. It maintains two pointers, l and r, starting from both ends of the array height. These pointers are used to keep track of the current maximum height of the left and right buildings.

Here's how it works:

Initialize l = 0 and r = len(height) - 1, which represent the indices of the first and last buildings, respectively.
Set max_l = height[l] and max_r = height[r] to initialize the maximum heights of the left and right buildings.
Initialize a result variable result to 0, which will store the total amount of rainwater that can be trapped.
The main loop runs until l < r. Inside the loop:

If h_l < h_r, increment l by 1. This means we're moving towards the building with the smaller height.
Update max_l = max(h_l, max_l) to keep track of the maximum height of the left buildings so far.
Add (max_l - h_l) to result. This is the amount of rainwater that can be trapped between the current left building and the previously tallest left building (i.e., max_l).
If h_l >= h_r, decrement r by 1. This means we're moving towards the building with the smaller height.
Update max_r = max(h_r, max_r) to keep track of the maximum height of the right buildings so far.
Add (max_r - h_r) to result. This is the amount of rainwater that can be trapped between the current right building and the previously tallest right building (i.e., max_r).
The loop continues until l >= r, at which point we return the final result.

Example Use Case:

In your example, the input array is [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. The code correctly calculates the total amount of rainwater that can be trapped between these buildings.

Here's a step-by-step breakdown of how the code runs:

Initially, l = 0 and r = 11.
We update max_l to 0 and max_r to 3.
Since h_l < h_r, we increment l by 1. Now, l = 1.
Update max_l to 1. Add (max_l - h_l) = (1 - 0) = 1 to result.
Continue this process until l >= r.
The final result is the total amount of rainwater that can be trapped between these buildings.
"""
