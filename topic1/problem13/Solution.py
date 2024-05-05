class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        ans[0] = 1

        for i in range(1, N):
            ans[i] = ans[i-1] * nums[i-1]

        product = 1
        for i in range(N-1, -1, -1):
            ans[i] *= product
            product *= nums[i]
        
        return ans
