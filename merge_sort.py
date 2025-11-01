class Solution(object):
    def sortArray(self, nums):
        if len(nums) > 1: 
            mid = len(nums) // 2 # take the middle 
            #divied in half 
            left = nums[:mid]
            right = nums[mid:]
            #sort both half array 
            self.sortArray(left)
            self.sortArray(right)
            #merge both array 
            i = 0 
            j = 0 
            k = 0 #for merge array 
            #make a loop to compare left most and right most 
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                else:
                    nums[k] = right[j]

arr = [38, 27, 43, 10]
sortArray()

