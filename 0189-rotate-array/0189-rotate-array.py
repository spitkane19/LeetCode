class Solution(object):
    def rotate(self, nums, k):
        lngth = len(nums)
        fake_list = list(nums)
        real_k = k % lngth       
        for i, x in enumerate(nums):
            move = i + real_k - lngth
            fake_list[move] = x
        nums[:] = fake_list
            