class Solution:
    def frequencySort(self, s):
        # Create a list of tuples to store frequency and character
        freq = [(0, chr(i + ord('a'))) for i in range(26)]

        # Count the frequency of each character in the string
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] = (freq[index][0] + 1, ch)

        # Sort by frequency in descending order, then by character in ascending order
        freq.sort(key=lambda x: (-x[0], x[1]))

        # Collect characters that have non-zero frequency
        result = [ch for f, ch in freq if f > 0]
        return result

# Main block to test the function
if __name__ == "__main__":
    sol = Solution()
    s = "tree"
    result = sol.frequencySort(s)
    print(result)
