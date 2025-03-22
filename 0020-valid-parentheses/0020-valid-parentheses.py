class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # Hash map to store mappings of closing to opening parentheses
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Loop through each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket doesn't match the stack's top element
                if mapping[char] != top_element:
                    return False
            else:
                # It was an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is still empty, return True, otherwise False
        return not stack