def longest_common_prefix(strs):
    """
    Find the longest common prefix shared by all strings in `strs`.

    Trick: sort the strings lexicographically. In sorted order, the
    FIRST and LAST strings are the two that diverge earliest among all
    pairs in the list -- so the common prefix of the whole list equals
    the common prefix of just these two. This avoids comparing every
    string against every other string.

    e.g. ["flower", "flow", "flight"] sorted -> ["flight", "flow", "flower"]
         comparing "flight" vs "flower" char by char gives "fl".
    """
    if not strs:
        # FIX: was `return " "` (a space character) instead of an empty
        # string. The common prefix of zero strings should be "".
        return ""

    strs.sort()

    first = strs[0]   # lexicographically smallest after sorting
    last = strs[-1]    # lexicographically largest after sorting
    ans = []

    # Compare character by character only up to the shorter of the two,
    # since the prefix can't be longer than either string.
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            # First mismatch found -> everything matched so far is the
            # common prefix.
            return ''.join(ans)
        ans.append(first[i])

    # One string is a prefix of the other (loop ran to completion) ->
    # the whole matched portion is the common prefix.
    return ''.join(ans)


def main():
    strs = []
    m = int(input("Enter the Number of Strings : "))
    for i in range(m):
        x = input(f"Enter the String {i} : ")
        strs.append(x)

    result = longest_common_prefix(strs)
    print("Longest Common Prefix : ", result)


if __name__ == "__main__":
    main()