class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sortedlist = nums1[:m] + nums2
        
        for i in range(len(nums1)):
            nums1[i] = sortedlist[i]
        
        nums1.sort()
