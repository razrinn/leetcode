# used claude for solution. need to revisit
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store the count of each character in the current window
        char_count = {}

        # Variables to track the window and result
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Add the current character to our count
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Calculate the current window size
            window_size = right - left + 1

            # Get the count of the most frequent character in the current window
            # This is the O(26) operation that makes this O(26n) overall
            most_frequent_count = max(char_count.values()) if char_count else 0

            # Calculate how many characters we need to replace
            chars_to_replace = window_size - most_frequent_count

            # If we need to replace more characters than k allows,
            # shrink the window from the left
            if chars_to_replace > k:
                char_count[s[left]] -= 1
                # If a character count becomes 0, we can remove it from the dictionary
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            else:
                # Update the max length if this window is valid
                max_length = max(max_length, window_size)

        return max_length