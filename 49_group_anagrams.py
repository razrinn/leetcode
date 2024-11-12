from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_comps = {}
        res = []

        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str not in char_comps:
                res.append([word])
                char_comps[sorted_str] = len(res) - 1
            else:
                res[char_comps[sorted_str]].append(word)

        return res


# TOPICS: array, hashtable, string, sorting
# NOTES: is it acceptable to sort the string or should I handle the anagram check manually?
