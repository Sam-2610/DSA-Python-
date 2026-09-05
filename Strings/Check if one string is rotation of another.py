def rotate_string(s, goal):
    """
    Check if 'goal' is a rotation of 's'.
    A string rotation means shifting characters from the front
    to the back (e.g. "abcde" rotated becomes "cdeab", "eabcd", etc.)

    Trick: if you concatenate s with itself (s + s), every possible
    rotation of s will appear as a substring somewhere in that
    doubled string. So we just need to check if 'goal' is a
    substring of (s + s).
    """
    # Different lengths can never be rotations of each other
    if len(s) != len(goal):
        return False

    # Concatenate s with itself to contain all rotations as substrings
    double_s = s + s

    # 'in' returns a proper boolean, unlike .find() which returns
    # an index (or -1) — that was the original bug
    return goal in double_s


def main():
    s = input("Enter the String: ")
    goal = input("Enter the goal String: ")  # fixed duplicate prompt text
    result = rotate_string(s, goal)
    print(result)


if __name__ == "__main__":
    main()