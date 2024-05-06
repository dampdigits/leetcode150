class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1] * N

        for i in range(1, N):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] +1
        
        total_candies = candies[-1]

        for i in range(N-2, -1, -1):
            if (ratings[i+1] < ratings[i] and candies[i] <= candies[i+1]):
                candies[i] = candies[i+1] +1

            total_candies += candies[i]
        
        return sum(candies)
