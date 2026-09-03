def isomorphicString(s, t):
    """
    Check whether two strings `s` and `t` are isomorphic: there must be a
    one-to-one character mapping s[i] -> t[i] that's consistent across
    the whole string in BOTH directions (no character in s maps to two
    different characters in t, and vice versa).

    Technique: instead of keeping two dictionaries mapping char->char,
    keep two arrays that record the LAST position each character was
    seen at (1-indexed, 0 meaning "never seen"). At each index i, if
    s[i] and t[i] were last seen at different positions, the mapping is
    inconsistent -> not isomorphic. This implicitly checks both
    directions at once, since m1 tracks s's characters and m2 tracks
    t's characters, compared against the SAME index each time.

    NOTE: originally had a stray `self` first parameter, left over from
    a class-based (e.g. LeetCode `class Solution:`) template that isn't
    present here -- that caused main()'s 2-argument call to raise a
    TypeError. Removed here to match how it's actually called.
    """
    # Arrays to track last-seen positions of characters (0 = not seen yet).
    # 256 entries covers the extended ASCII range.
    m1, m2 = [0] * 256, [0] * 256

    n = len(s)

    for i in range(n):
        # If s[i] and t[i] don't have matching "last seen" positions,
        # the character mapping is inconsistent -> not isomorphic.
        if m1[ord(s[i])] != m2[ord(t[i])]:
            return False

        # Record that s[i]/t[i] were last seen at index i (stored as i+1
        # so that 0 can unambiguously mean "never seen").
        m1[ord(s[i])] = i + 1
        m2[ord(t[i])] = i + 1

    return True


def main():
    s = input("Enter the String : ")
    t = input("Enter the String : ")

    # NOTE: this assumes len(s) == len(t), as isomorphic strings must be
    # the same length by definition. If they differ, indexing t[i] past
    # its own length will raise an IndexError -- LeetCode's version of
    # this problem guarantees equal lengths in its constraints, but
    # standalone user input has no such guarantee.
    result = isomorphicString(s, t)

    if result:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()