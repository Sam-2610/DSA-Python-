def CheckAnagrams(str1, str2):
    # Case: when both of the strings have different lengths
    if len(str1) != len(str2):
        return False  # Strings can't be anagrams if lengths are different

    # Initialize a frequency array to store character counts
    freq = [0] * 26

    # Count frequency of each character in str1
    for char in str1:
        freq[ord(char) - ord('A')] += 1  # Increment frequency for each character in str1

    # Decrement frequency for each character in str2
    for char in str2:
        freq[ord(char) - ord('A')] -= 1  # Decrement frequency for each character in str2

    # Check if all frequencies are zero, meaning both strings have the same characters
    for count in freq:
        if count != 0:
            return False  # If any frequency is non-zero, they are not anagrams

    return True  # The strings are anagrams if all frequencies are zero

# Driver code
if __name__ == "__main__":
    Str1 = "INTEGER"
    Str2 = "TEGERNI"

    # Check if the strings are anagrams and output the result
    if CheckAnagrams(Str1, Str2):
        print("True")  # Output "True" if they are anagrams
    else:
        print("False")  # Output "False" if they aren't anagrams
