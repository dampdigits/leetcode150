class Solution:
    def trap(self, height: List[int]) -> int:
        area = lmax = 0

        for i in range(1, len(height)):
            x = i

            while lmax < x and height[x] > height[x-1]:
                area += min(height[x], height[lmax]) - height[x-1]
                height[x-1] = min(height[x], height[lmax])
                x -= 1
            
            if height[lmax] < height[i]: lmax = i
        
        return area
