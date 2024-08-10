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
        print(queue.popleft())

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

node1.
        
# def is_symmetric(root):
# pass