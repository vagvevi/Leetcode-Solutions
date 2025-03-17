class Solution {
    public int lengthOfLongestSubstring(String s) {
                HashMap<Character, Integer> charIndex = new HashMap<>();
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            
            // If character is already in map and within current window
            if (charIndex.containsKey(currentChar) && charIndex.get(currentChar) >= left) {
                left = charIndex.get(currentChar) + 1; // Move left pointer
            }

            charIndex.put(currentChar, right); // Update the last seen index
            maxLength = Math.max(maxLength, right - left + 1); // Update max length
        }

        return maxLength;
    }
}