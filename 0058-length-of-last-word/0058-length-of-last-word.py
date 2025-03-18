class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        if words:
            a= words[-1]
            return len(a)
        else:
            return 0