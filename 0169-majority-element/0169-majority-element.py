class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        nmbr = 0
        list = []
        nums.sort()

        for x in nums:
            if x not in list:
                list.append(x)
                nmbr = 1
            else:
                nmbr += 1
            
            if nmbr >= max:
                answer = x
                max = nmbr
        
        return answer
            