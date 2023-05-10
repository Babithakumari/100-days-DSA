""" 
Brute Force Solution:

Traverse the array and find if the element exists return index else -1
But then time complexity is O(n)
The problem description asks us to solve the problem in O(logn)

-----------------------------------------------------------------------

Efficient Solution:

Variant of Binary search
Each time, 1 part of the array remains sorted: left or right
We need to find the sorted portion and apply binary search on the sorted half

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary search can only be applied on a sorted part of an array
        # Here, either left part remains sorted or right part remains sorted
        # whichever is sorted, we start searching based on that condition
        
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            
            if nums[mid]==target:
                return mid
            
            # left part sorted( left-mid sorted)
            if nums[left]<=nums[mid]:
                # if element smaller than mid and larger than left - search left
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                    
                # otherwise search right
                else:
                    left = mid+1
                    
            # right part sorted(mid-right sorted)
            else:
                # if element greater than mid and smaller than right - search right
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                  
                # otherwise search left
                else:
                    right = mid-1
                    
                
        return -1
        