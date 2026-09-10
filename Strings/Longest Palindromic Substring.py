class Solution:
    def longestPalindrome(self, s):
        # Trivial case: single character or empty string is already a palindrome
        if len(s) <= 1:
            return s
        
        Max_Len = 1
        Max_Str = s[0]

        # Insert '#' between every character (and at both ends) so every
        # palindrome - odd or even length - gets a single unambiguous center
        s = '#' + '#'.join(s) + '#'

        # dp[i] = radius of the palindrome centered at index i in the transformed string
        dp = [0 for _ in range(len(s))]

        center = 0  # center of the rightmost palindrome found so far
        right = 0   # right boundary of that palindrome

        for i in range(len(s)):
            # If i is within the current rightmost palindrome, we can reuse
            # previously computed info via mirror symmetry to get a lower bound for dp[i]
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])

            # Try to expand the palindrome centered at i outward,
            # character by character, as long as both sides match
            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i] - 1] == s[i + dp[i] + 1]:
                dp[i] += 1

            # If this palindrome extends beyond the current rightmost boundary,
            # update the center and right boundary to this new palindrome
            if i + dp[i] > right:
                center = i
                right = i + dp[i]

            # Track the longest palindrome seen so far
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                # Extract the substring from the transformed string and remove '#' padding
                Max_Str = s[i - dp[i]:i + dp[i] + 1].replace('#', '')

        return Max_Str