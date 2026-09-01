def reverseWords(s):
    """
    Reverse the order of words in a string, collapsing any run of
    multiple spaces down to a single space and ignoring leading/
    trailing spaces entirely.

    e.g. " amazing coding skills " -> "skills coding amazing"

    FIX: originally had a stray `self` first parameter, left over from
    a LeetCode-style `class Solution:` wrapper that isn't present here.
    main() called it with only one argument, so `s` got bound to `self`
    and the real `s` parameter was left missing -> TypeError.

    Approach: scan from the END of the string toward the start, picking
    off one word at a time and appending it to the result (which
    naturally reverses their order), skipping over any spaces between
    words as we go.
    """
    result = ""

    # Pointer starting from the end of the string
    i = len(s) - 1

    # Traverse from right to left
    while i >= 0:
        # Skip any trailing/inter-word spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # If we ran off the start while skipping spaces, we're done
        if i < 0:
            break

        # `i` now points at the last character of a word
        end = i

        # Move left until we hit a space or the start of the string
        while i >= 0 and s[i] != " ":
            i -= 1

        # `i` now points one-before the first character of the word
        # (or -1 if the word starts at index 0), so the word itself is:
        word = s[i + 1:end + 1]

        # Separate words in the output with a single space
        if result != "":
            result += " "

        # Append this word (words come out in reverse order naturally,
        # since we're scanning right-to-left)
        result += word

    return result


# Driver code
def main():
    s = " amazing coding skills "
    print(reverseWords(s))


if __name__ == "__main__":
    main()