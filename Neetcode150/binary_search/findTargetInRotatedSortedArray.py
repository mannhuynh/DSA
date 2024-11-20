from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for an element in a rotated sorted array.
        
        Args:
            nums (List[int]): A rotated sorted array of integers.
            target (int): The element to be searched.
        
        Returns:
            int: The index of the target element if found, -1 otherwise.
        """

        # Find the pivot index where the array is rotated
        # We use binary search to find the pivot index in O(log n) time complexity
        left, right = 0, len(nums) - 1
        while left < right:
            # Calculate the middle index using integer division (//) to avoid floating point numbers
            mid = (left + right) // 2
            
            # If the middle element is greater than the last element, it means the pivot is between the left and middle elements
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the pivot is either at the middle or the last index, so we update right to mid for further search
                right = mid
        
        # Determine the pivot index where the array is rotated
        # The loop ends when left >= right, indicating that left and right have converged to the same value, which is the pivot index
        pivot = left

        # Perform binary search on the non-rotated part of the array (left subarray)
        # We first check if the target element can be in this subarray
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            # If the middle element is equal to the target, we found it!
            if nums[mid] == target:
                return mid

            # We need to check whether the left part of the subarray is sorted or not
            # This is necessary because in a rotated array, elements within each segment are sorted
            if nums[left] <= nums[mid]:
                # If we know that all the numbers on the left side are sorted and smaller than the middle number
                if nums[left] <= target < nums[mid]:
                    # We can safely reduce our search space by discarding the right part of this subarray
                    right = mid - 1
                else:
                    # Otherwise, we need to keep searching in the right part of this subarray
                    left = mid + 1
            else:
                # If the left part is not sorted, it means that the middle element must be a pivot
                # In this case, all numbers to its left are greater than themselves and those to its right are less than themselves
                if nums[mid] < target <= nums[right]:
                    # So we can safely reduce our search space by discarding the left part of this subarray
                    left = mid + 1
                else:
                    # Otherwise, we need to keep searching in the left part of this subarray
                    right = mid - 1

        # If the target element is not found after the search process is finished, return -1
        return -1

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 3))
