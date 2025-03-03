class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if (length <= 1):
            return length

        res = 1
        tmp = s[0]
        hmap = {s[0]: 0}
        l, r = 0, 1

        while r < length:
            if r == length - 1 and s[r] not in hmap:
                tmp += s[r]
                res = max(res, len(tmp))
                break

            char = s[r]

            if char not in hmap:
                hmap[char] = r
                tmp += char
            else:
                res = max(res, len(tmp))
                new_l = hmap[char] + 1
                tmp = s[new_l:r + 1]

                for i in range(new_l - l):
                    del hmap[s[l + i]]
                hmap[char] = r
                l = new_l
            r += 1

        return res

    # second run
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l, r = 0, 0
        visited = {}
        res = 0

        while r < len(s):
            if s[r] in visited and visited[s[r]] >= l:
                res = max(res, r - l)
                l = visited[s[r]] + 1
            visited[s[r]] = r
            r += 1

        return max(res, r - l)