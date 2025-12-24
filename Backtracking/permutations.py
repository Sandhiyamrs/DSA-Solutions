def permute(nums):
    res = []

    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            backtrack(path + [nums[i]], used)
            used[i] = False

    backtrack([], [False] * len(nums))
    return res
