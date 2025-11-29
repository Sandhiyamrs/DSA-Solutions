import bisect

def length_of_lis(nums):
    if not nums:
        return 0

    tails = []  # tails[i] = smallest tail for increasing subseq of length i+1

    for x in nums:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x

    return len(tails)
