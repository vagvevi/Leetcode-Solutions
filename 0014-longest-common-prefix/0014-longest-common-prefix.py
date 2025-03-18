class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # If there is only one string in the list, return it as the common prefix
        if len(strs) == 1:
            return strs[0]
        
        # Sort the list lexicographically
        strs.sort()
        
        # Initialize the common prefix as an empty string
        common_prefix = ""
        
        # Compare the first and the last string in the sorted list
        first, last = strs[0], strs[-1]
        
        i = 0
        # Iterate through the characters of the first and last string
        while i < len(first) and i < len(last):
            if first[i] == last[i]:
                common_prefix += first[i]
                i += 1
            else:
                break
        
        return common_prefix
        