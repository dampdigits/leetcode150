class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_removed = []
        count = 0

        for num in nums:
            if num != val:
                val_removed.append(num)
                count += 1
        
        nums[:] = val_removed
        return count
