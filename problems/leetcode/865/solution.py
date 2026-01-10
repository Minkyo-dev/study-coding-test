import sys
import os
from typing import Optional
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

@profile_time_memory
def mysolution():
    pass

@profile_time_memory
def othersolution(root: Optional[TreeNode]):
    def dfs( root, depth=0):
        if not root.left and not root.right:
            return root, depth
        if root.left and root.right:
            leftNode, leftDepth = dfs(root.left, depth+1)
            rightNode, rightDepth = dfs(root.right, depth+1)
            if leftDepth > rightDepth:
                return leftNode, leftDepth
            elif leftDepth < rightDepth:
                return rightNode, rightDepth
            else:
                return root, leftDepth
        if root.left:
            return dfs(root.left, depth+1)
        if root.right:
            return dfs(root.right, depth+1)
    return dfs(root, 0)[0]

if __name__ == "__main__":
    root = TreeNode(
        val=3, 
        left=TreeNode(
            val=5,
            left=TreeNode(val=6),
            right=TreeNode(
                val=2,
                left=TreeNode(val=7),
                right=TreeNode(val=4)
            )
        ),
        right=TreeNode(
            val=1,
            left=TreeNode(val=0),
            right=TreeNode(val=8)
        )
    )
    print(root)

    # mysolution(root)
    othersolution(root)
    