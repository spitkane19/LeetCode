class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        foundNum = []
        removeList = []
        for x in nums:
            if x not in foundNum:
                foundNum.append(x)
            else:
                removeList.append(x)

        for x in removeList:
            nums.remove(x)
        
        return len(nums)