from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count.items(), key=lambda x:x[1])[0]
