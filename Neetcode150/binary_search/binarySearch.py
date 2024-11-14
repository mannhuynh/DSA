"""Binary Search
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(log n) time complexity.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3
Example 2:
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0 or (len(nums)>0 and nums[-1]<target):
            return -1
        if (len(nums)>0 and nums[0]>target):
            return -1
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
