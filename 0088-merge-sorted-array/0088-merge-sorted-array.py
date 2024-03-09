class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
           return
        length = len(nums1)
        indx = length-1
        while n > 0 and m > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[indx] = nums2[n-1]
                n -= 1

            else:
                nums1[indx] = nums1[m-1]
                m -= 1
            indx -= 1
        while n > 0:
            nums1[indx] = nums2[n-1]
            n -= 1
            indx -= 1    
