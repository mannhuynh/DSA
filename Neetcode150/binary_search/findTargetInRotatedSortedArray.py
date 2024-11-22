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

        # First, we need to find the pivot index where the rotation occurred
        left, right = 0, len(nums) - 1  # Initialize our search space
        
        # We use binary search to find the pivot
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # we know that the rotation occurred after the middle index
            if nums[mid] > nums[right]:
                left = mid + 1
            else:  # Otherwise, the pivot must be before or at the middle index
                right = mid
        
        # Now we have found the pivot index. We'll use it to partition our array.
        pivot = left

        # Next, we perform a binary search within the rotated array
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            # If we find the target element in this iteration, return its index immediately!
            if nums[mid] == target:
                return mid
                
            # Otherwise, partition our array based on whether it's been rotated to the left or right
            if nums[left] <= nums[mid]:  # If the left half is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left half, so shrink our search space to the left half
                    right = mid - 1
                else:  # Otherwise, the target must be in the right half
                    left = mid + 1
            else:  # If the right half is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right half, so shrink our search space to the left
                    left = mid + 1
                else:  # Otherwise, the target must be in the left half
                    right = mid - 1

        # If we've reached this point without finding the target element, return -1 to indicate failure.
        return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 1))  
