class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        number = i = 0
        N = len(s)
        
        while i < N-1:
            if nums[s[i]] < nums[s[i+1]]:
                number += nums[s[i+1]] - nums[s[i]]
                i += 2
            else:
                number += nums[s[i]]
                i += 1
        
        return number if i == N else number + nums[s[N-1]]
