def majority_element2():
    # ------------------------------------------------------------------
    # 1. Read input array from the user
    # ------------------------------------------------------------------
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        x = int(input(f"Enter Element {i + 1}: "))
        arr.append(x)

    # ------------------------------------------------------------------
    # 2. Boyer-Moore Voting Algorithm (extended for "more than n/3" case)
    # ------------------------------------------------------------------
    # At most 2 elements can appear more than n/3 times in an array,
    # so we track two candidates (ele1, ele2) and their vote counts.
    cnt1 = 0
    cnt2 = 0
    ele1 = float('-inf')  # first candidate for majority element
    ele2 = float('-inf')  # second candidate for majority element

    for i in range(n):
        # If ele1 has no votes AND the current element isn't already ele1,
        # claim this element as the new candidate for ele1.
        if cnt1 == 0 and ele1 != arr[i]:
            cnt1 = 1
            ele1 = arr[i]

        # Same logic for the second candidate, ele2.
        elif cnt2 == 0 and ele2 != arr[i]:
            cnt2 = 1
            ele2 = arr[i]

        # If current element matches an existing candidate, add a vote.
        elif arr[i] == ele1:
            cnt1 += 1
        elif arr[i] == ele2:
            cnt2 += 1

        # Otherwise, the current element opposes both candidates,
        # so both candidates lose a vote (this is the "cancellation" step).
        else:
            cnt1 -= 1
            cnt2 -= 1

    # ------------------------------------------------------------------
    # 3. Verification pass
    # ------------------------------------------------------------------
    # The voting step only finds POTENTIAL candidates — it doesn't
    # guarantee they actually appear more than n/3 times.
    # So we recount their real occurrences in the full array here.
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if arr[i] == ele1:
            cnt1 += 1
        if arr[i] == ele2:
            cnt2 += 1

    # Correct threshold: an element must appear MORE than n/3 times.
    # Using integer division (n // 3) + 1 gives the smallest integer
    # count that satisfies "> n/3".
    mini = n // 3 + 1

    # ------------------------------------------------------------------
    # 4. Build the final result (checked once, after full counting)
    # ------------------------------------------------------------------
    arr2 = []
    if cnt1 >= mini:
        arr2.append(ele1)
    if cnt2 >= mini:
        arr2.append(ele2)

    arr2.sort()
    print(arr2)


majority_element2()