from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # Preorder with marker
    res = []
    def dfs(node):
        if not node:
            res.append("#")
            return
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(res)

def deserialize(data):
    vals = deque(data.split(","))
    def dfs():
        if not vals:
            return None
        val = vals.popleft()
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
