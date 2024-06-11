class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest substring without repeating characters.
        
        Args:
            s (str): The input string.
        
        Returns:
            int: The length of the longest substring without repeating characters.
        
        Example:
            Input: s = "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3.

            Input: s = "bbbbb"
            Output: 1
            Explanation: The answer is "b", with the length of 1.

            Input: s = "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3.
        """
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
