class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index ,count = 1, 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
                count += 1
        
        return count + 1
