class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        left = 0
        maxi = 0
        n = len(s)
        
        
        for right in range(n):
            current_char = s[right]
            
            if current_char in char_dict and char_dict[current_char] >= left:
                left = char_dict[current_char] + 1
            
            maxi = max(maxi, right - left + 1)
            char_dict[current_char] = right
            
            
        return maxi