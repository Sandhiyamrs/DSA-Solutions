def combinationSum(candidates, target):
    res = []

    def dfs(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            dfs(i, path + [candidates[i]], total + candidates[i])

    dfs(0, [], 0)
    return res
