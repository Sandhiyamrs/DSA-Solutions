def combinationSum(candidates, target):
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return res
