from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            s_word = "".join(sorted(word))
            hmap[s_word] = hmap.get(s_word, []) + [word]

        return list(hmap.values())

    # second run, use defaultdict
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for word in strs:
            s_word = "".join(sorted(word))
            hmap[s_word].append(word)

        return list(hmap.values())