"""Find Minimum in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
    Input: nums = [3,4,5,6,1,2]
    Output: 1
Example 2:
    Input: nums = [4,5,0,1,2,3]
    Output: 0
Example 3:
    Input: nums = [4,5,6,7]
    Output: 4
"""
class Solution:
    def findMin(self, nums) -> int:
        # Initialize the minimum element as the first element of the array
        res = nums[0]
        # Define the left and right indices for binary search
        l_idx = 0  # left index
        r_idx = len(nums)-1  # right index

        # Perform binary search to find the minimum element
        while l_idx <= r_idx:
            # Check if the subarray from left to right is sorted in ascending order
            if nums[l_idx] < nums[r_idx]:
                # If sorted, the minimum element must be in this subarray
                res = min(res, nums[l_idx])  # update the minimum element
                return res  # return the minimum element immediately

            # Continue binary search if subarray is not sorted
            mid = (l_idx + r_idx) //2

            # Update the result where it is the mid element
            res = min(nums[mid], res)

            # If pivot is greater than or equal to leftmost element, 
            # the minimum element must be in the right half of the array
            if nums[mid] >=  nums[l_idx]:
                l_idx = mid +1
            # Otherwise, the minimum element must be in the left half of the array
            else:
                r_idx = mid -1
        # Return the minimum element when search is complete
        return res

sol = Solution()
print(sol.findMin([4,5,6,7,3]))
