class TreeNode():
   def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


#Problem 1: Is Even-valued
def is_even(root):
   if root:
      if root.val % 2 != 0:
         return False
      return is_even(root.left) and is_even(root.right)
   else:
      return True

# nod1 = TreeNode(10)
# nod1.right = TreeNode(8)
# nod1.left = TreeNode(2)
# nod1.left.left = TreeNode(4)
# nod1.left.right = TreeNode(6)
# nod1.right.right = TreeNode(1)

# print(is_even(nod1))

# Problem 2.1: Binary Tree Height
def height(root: TreeNode | None) -> int:
   if not root:
      return 0
   print(root.val)
   return max(height(root.left), height(root.right)) + 1
   
# print(height(nod1))

# Problem 2.2: Binary Tree Max
def tree_max(root: TreeNode | None) -> TreeNode | None:
   if not root:
      return None
   elements: list[TreeNode] = []
   def helper(node: TreeNode | None, lst: list[TreeNode]):
      if node:
         helper(node.left, lst)
         lst.append(node)
         helper(node.right, lst)
         
   helper(root, elements)
   
   max_val: float = float("-inf")
   max_node: TreeNode | None = None
   
   for node in elements:
      if node.val > max_val:
         max_val = node.val
         max_node = node
         
   return max_node

# print(tree_max(nod1).val)
      

class TreeNode():
  def __init__(self, key, value, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

# Problem 3: BST Insert 
def insert(root: TreeNode | None, key: int, value: object):
   if not root:
      return None
   current = root
   while current:
      if current.key == key:
         current.val = value
         break
      elif current.key > key:
         if not current.left:
            current.left = TreeNode(key, value)
            break
         current = current.left
      else:
         if not current.right:
            current.right = TreeNode(key, value)
            break
         current = current.right

   return root
   
node1 = TreeNode(10, "Neiji")
node1.left = TreeNode(8, "Sasuke")
node1.right = TreeNode(15, "Itachi")
node1.left.left = TreeNode(1, "Kakashi")
node1.left.right = TreeNode(6, "Ino")

# insert(node1, 0, "Naruto")
# print(node1.left.left.left.val)

# Problem 4: BST Remove I
def remove_bst(root: TreeNode | None, key: int) -> TreeNode | None:
   if not root:
      return None

   current = root
   while current:
      if current.key == key:
         pass
      elif current.key > key:
         current = current.
   # Locate the node to be removed
   # If the node is a leaf node:
      # Remove the node by redirecting the appropriate child reference of its parent to None
   # If the node has one parent:
      # Replace the node with its child, updating its parent's nodes child reference appropriately
   # If the node has two children:
      # Find the node's inorder successor (smallest node in right subtree)
      # Swap the value of the node and its inorder successor
      # Recursively remove the successor (which now has the current node's value)
   # Return the root of the updated tree
   