from typing import List


class Solution:
    def longestConsecutiveUnoptimized(self, nums: List[int]) -> int:
        hmap = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hmap:
                pointer = 1
                while num + pointer in hmap:
                    pointer += 1
                longest = max(longest, pointer)
        return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()

        counts = []
        count = 1
        y = nums[0]
        for x in nums[1:]:
            if x != y + 1:
                counts.append(count)
                count = 0
            y = x
            count += 1
        counts.append(count)
        return max(counts)


# TOPICS: array, unionfind
# DIFFICULTY: medium
# NOTES: check if input array can be sorted first
