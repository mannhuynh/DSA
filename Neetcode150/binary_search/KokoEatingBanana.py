"""Koko Eating Bananas
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.
Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
Example 2:
Input: piles = [25,10,23,4], h = 4
Output: 25"""

import math
class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        l, r = 1, max(piles)

        # while l < r :
        #     mid = (l+r)//2
        #     if sum((p-1)//mid + 1 for p in piles) <= h:
        #         r = mid 
        #     else: 
        #         l = mid + 1
        # return l
        
        # Initialize the result variable to store the minimum eating rate.
        res = r
        # The while loop continues until the left and right pointers meet or cross each other.
        while l <= r:
            # Calculate the middle value between the left and right pointers.
            mid = (l+r)//2
            # Initialize a variable to keep track of the total time needed to eat all bananas.
            total_time = 0
            # Iterate over each pile in the piles array.
            for p in piles:
                # For each pile, calculate how many hours it would take to finish eating all bananas at the current eating rate (mid).
                # If there are less than mid bananas left, you can finish eating the pile in one hour.
                total_time += p//mid + 1

            # Check if the total time needed is less than or equal to h hours.
            if total_time <= h:
                # If it is, update the result variable with the current eating rate (mid) and move the right pointer to mid - 1.
                res = mid
                r = mid - 1
            else: 
                # If not, move the left pointer to mid + 1.
                l = mid + 1
        # Return the minimum eating rate found.
        return res

sol = Solution()
# print(sol.minEatingSpeed([25,10,23,4],4))

p = [1,4,3,2]
h = 9
print(sol.minEatingSpeed(p,h))
print(-10//3)
