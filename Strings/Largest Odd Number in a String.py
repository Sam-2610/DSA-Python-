def largest_odd_number(s):
    """
    Given a string of digits `s`, return the largest-valued odd integer
    (as a string) that is a prefix of `s`, or "" if no such prefix exists.

    Key idea: a prefix's value only depends on where it ends. A LONGER
    prefix is always >= a shorter one numerically (more digits), so we
    want the longest possible prefix that still ends in an odd digit --
    i.e. we need the RIGHTMOST odd digit in the string, not the first
    one found scanning left to right.
    """
    ind = -1
    n = len(s)

    # FIX: scan from the right (n-1 down to 0), not left to right, and
    # include every index (the original `range(0, n-1)` also skipped
    # the last character entirely).
    for i in range(n - 1, -1, -1):
        # FIX: convert the character to an int properly. `s[i] - '0'`
        # is a C/C++ trick that doesn't work in Python -- strings can't
        # be subtracted. Use int(s[i]) instead.
        if int(s[i]) % 2 == 1:
            ind = i
            break  # first odd digit found scanning from the right = rightmost odd digit

    if ind == -1:
        return ""  # no odd digit anywhere in the string -> no valid answer

    # Strip any leading zeros from the prefix s[0:ind+1]
    # (e.g. "0114" with ind=2 should give "11", not "0114"[:3])
    i = 0
    while i <= ind and s[i] == '0':
        i += 1

    # FIX: was `s[i:ind - i - 1]`, an unrelated/incorrect end index.
    # The correct slice is up through and including `ind`.
    return s[i:ind + 1]


def main():
    s = input("Enter the String : ")
    result = largest_odd_number(s)
    print("Largest Odd Number : ", result)


if __name__ == "__main__":
    main()