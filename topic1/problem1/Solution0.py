class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n: return

        sortedlist = []
        i, j = 0, 0

        while len(sortedlist) < len(nums1):
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    sortedlist.append(nums1[i])
                    i += 1
                else:
                    sortedlist.append(nums2[j])
                    j += 1
            elif i < m:
                sortedlist.append(nums1[i])
                i += 1
            else:
                sortedlist.append(nums2[j])
                j += 1
        
        for i in range(len(nums1)):
            nums1[i] = sortedlist[i]
