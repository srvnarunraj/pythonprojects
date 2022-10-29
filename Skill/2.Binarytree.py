# Definition
# for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def traverse(root1):
        # base condition
        if root1 is None:
            return None
        # visit left tree
        root1.traverse(root1.left)
        # visit base node
        print(root1.val)
        # visit right node
        root1.traverse(root1.right)


root = TreeNode(6)
root.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(8)
print("Binary tree is : ")
TreeNode.traverse(root)