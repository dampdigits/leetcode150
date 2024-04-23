class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        major = [nums[0], 1]
        curr = [nums[0], 1]

        for num in nums:
            if num == curr[0]:
                curr[1] += 1
            else:
                if curr[1] > major[1]:
                    major[0] = curr[0]
                    major[1] = curr[1]
                
                curr[0] = num
                curr[1] = 1
        
        return major[0] if major[1] > curr[1] else curr[0]
