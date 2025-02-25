from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            tmp = min(height[left], height[right]) * (right - left)
            res = max(res, tmp)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res