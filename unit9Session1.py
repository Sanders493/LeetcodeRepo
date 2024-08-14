from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def print_tree_bfs(root: TreeNode) -> None:
    queue = deque()
    node: TreeNode | None = root
  
    queue.append(node)

    while queue:
        node = queue.popleft()  
        if node:
          print(node.val)
  
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)

# node1 = TreeNode(6)
# node1.left = TreeNode(4)
# node1.right = TreeNode(12)
# node1.left.left = TreeNode(3)
# node1.left.right = TreeNode(5)
# node1.right.right = TreeNode(14) 
# print_tree_bfs(node1)

# Problem 1: Is Symmetric Tree
def is_mirror(left: TreeNode | None, right: TreeNode | None) -> bool:
  if not left and not right:
    return True
  if not left or not right:
    return False
  if left.val != right.val:
    return False
  return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
def is_symmetric(root: TreeNode | None):
  if not root:
    return True
  return is_mirror(root.left, root.right)
  
'''
       1
     /   \
    /     \
   2       2
  / \     / \
 3   4   4   3
'''

# Problem 2: Root-to-Leaf Paths
def binary_tree_paths(root: TreeNode | None):
  if not root:
    return [""]
  paths: list[str] = []
  
  def helper(node: TreeNode | None, elements: list[str]) -> None:
    if node:
  
'''

  10
 /  \
7    12
 \  
  8  
Happy case:
f(TreeNode(10, 7(None, 8), 12)) => ["10 -> 7 -> 3", "10 -> 12"]

Edge cases:
f(None) => [""]
f(TreeNode(10, None, None)) => ["10"]

Plans:
1. Recursively going through each node and returning a string containing the value at each return call
2. Use a while loop and a queue.

Detailed Plan(Recursive):

'''