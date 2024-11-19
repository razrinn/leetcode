from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1

            if total > target:
                right -= 1

            if total == target:
                return [left + 1, right + 1]


# TOPICS: array, twopointer, binarysearch
# DIFFICULTY: medium
