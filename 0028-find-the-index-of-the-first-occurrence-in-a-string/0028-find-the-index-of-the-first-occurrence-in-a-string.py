class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0  # Edge case: empty needle should return 0
        l, r = 0, 0
        while l < len(haystack):
            if haystack[l] == needle[r]:
                r += 1
                if r == len(needle):
                    return l - r + 1  # Found the needle in haystack
            else:
                l -= r  # Reset l to the start of the last match attempt
                r = 0
            l += 1
        return -1