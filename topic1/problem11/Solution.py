class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        for i, num in enumerate(citations):
            if num >= len(citations) - i:
                return len(citations) - i

        return 0
