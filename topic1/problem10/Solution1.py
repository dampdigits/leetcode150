class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = max_reach = next_position = 0

        for i in range(len(nums)-1):
            new_reach = i + nums[i]
            
            if new_reach > max_reach:
                max_reach = new_reach
            
            if i == next_position:
                next_position = max_reach
                jumps += 1
            
        return jumps
