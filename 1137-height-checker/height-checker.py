class Solution:
    
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        i = j = count = 0

        while i < len(heights) and j < len(expected):
            if heights[i] != expected[j]:
                count += 1
            i += 1
            j += 1
        
        return count
