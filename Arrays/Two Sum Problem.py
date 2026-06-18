def two_sum(nums, target):
    seen = {}                            # stores {number : index}

    for i, num in enumerate(nums):
        complement = target - num        # what number do we need?

        if complement in seen:           # have we seen it before?
            return [seen[complement], i]
        
        seen[num] = i                    # store current number
    
    return []