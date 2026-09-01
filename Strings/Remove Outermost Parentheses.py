def remove_parantheses(s):
    """
    Remove the outermost parentheses of every "primitive" substring in a
    valid parentheses string.

    A primitive string is a non-empty valid parentheses string that
    cannot be split into two smaller non-empty valid parentheses strings
    (e.g. "(()())" is primitive, but "()()" is two primitives "()" + "()").

    Approach: walk the string tracking nesting `depth`.
      - On '(': only keep it if depth > 0 (i.e. it's NOT the outermost
        opening bracket of a primitive), then increase depth.
      - On ')': decrease depth first, then only keep it if depth > 0
        (i.e. it's NOT the outermost closing bracket of a primitive).

    Builds the output separately from the input (using a list, joined at
    the end) instead of mutating/growing the input string in place, which
    is both incorrect and inefficient.
    """
    output = []
    depth = 0

    for ch in s:
        if ch == '(':
            if depth > 0:
                output.append(ch)   # not the outermost '(' -> keep it
            depth += 1
        else:  # ch == ')'
            depth -= 1
            if depth > 0:
                output.append(ch)   # not the outermost ')' -> keep it

    return ''.join(output)


def main():
    # FIX: must be an actual string literal (with quotes). Without quotes,
    # ((())) is parsed by Python as nested grouping around an empty tuple
    # () -- not the string "((()))" -- so remove_parantheses saw an empty
    # tuple with length 0 and did nothing.
    result = "((()))"
    print(remove_parantheses(result))


if __name__ == "__main__":
    main()