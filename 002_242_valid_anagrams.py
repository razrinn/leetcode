from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap = {}

        for i in s:
            hmap[i] = hmap.get(i, 0) + 1

        for i in t:
            if i not in hmap:
                return False
            new_val = hmap.get(i, 0) - 1
            if new_val < 0:
                return False
            hmap[i] = new_val

        return True