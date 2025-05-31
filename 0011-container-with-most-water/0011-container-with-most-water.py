class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            # Calculate current area
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            max_area = max(max_area, area)
            
            # Move the pointer at the shorter line
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
        