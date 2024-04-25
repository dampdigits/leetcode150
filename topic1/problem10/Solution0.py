class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        # Minimum jumps required from each
        # position in nums to reach end position
        min_jumps = [inf] * N
        
        # Min jumps required from end
        # position to reach end position
        min_jumps[-1] = 0

        # Finding minimum jumps required
        # starting from 2nd last position
        for i in range(N-2, -1, -1):

            # Find which position to jump to from current position
            # so that the total jumps required to reach end is minimum
            for j in range(nums[i] +1):
                if i+j < N:
                    min_jumps[i] = min(min_jumps[i], min_jumps[i+j] +1)
        
        return min_jumps[0]
