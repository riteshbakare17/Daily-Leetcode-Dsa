class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            seen[ch] = right
            ans = max(ans, right - left + 1)

        return ans