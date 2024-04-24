class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, j in enumerate(nums):
            if i <= farthest:
                farthest = max(farthest, i+j)
            
        return farthest >= len(nums)-1
