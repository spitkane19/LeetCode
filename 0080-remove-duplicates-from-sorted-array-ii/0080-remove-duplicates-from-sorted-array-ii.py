class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=1
        for r in range(1, len(nums)):
            if l == 1 or nums[r] != nums[l-2]:
                nums[l] = nums[r]
                l +=  1
                    
        return l


