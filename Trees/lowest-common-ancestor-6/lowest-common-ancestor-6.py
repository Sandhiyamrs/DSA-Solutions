class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    return root if left and right else left or right

# Example usage
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                TreeNode(1, TreeNode(0), TreeNode(8)))
p = root.left  # Node 5
q = root.right  # Node 1
lca = lowestCommonAncestor(root, p, q)
print("Output:", lca.val)
