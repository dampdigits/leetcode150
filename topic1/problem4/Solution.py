class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        count = reps = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[index] and reps == 2: continue
            
            if nums[i] != nums[index]: reps = 1
            else: reps += 1

            nums[index +1] = nums[i]
            count += 1
            index += 1

        return count
