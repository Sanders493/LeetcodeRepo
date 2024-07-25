class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

# Problem 1: Build A Binary Tree
node3 = TreeNode(4)
node2 = TreeNode(3)
node1 = TreeNode(2)
root = TreeNode(1)
root.right = node1
root.left = node2
node1.right = node3


# Problem 2-3: 3-Node Product I
def check_tree(root: TreeNode) -> bool:
   if not root or not root.left or not root.right:
      return False
   product = root.left.val * root.right.val
   return product == root.val
   
# print(check_tree(root))

# Problem 4: Find Rightmost Node I
def right_most(root: TreeNode) -> object | None:
   if not root:
      return None

   current: TreeNode = root
   while current.right:
      current = current.right
      
   return current.val
      
# print(right_most(root))

# Problem 5: Find Rightmost Node II
def right_most_II(root: TreeNode) -> object | None:
   if not root:
      return None
   if not root.right:
      return root.val
      
   return right_most_II(root.right)
   
# print(right_most_II(root))

# Problem 6: Post-order Traversal
def postorder_traversal(root: TreeNode) -> object | None:
   if not root:
      return [None]

   elements = []
   def helper(root, lst):
      if root:
         helper(root.left, lst)
         helper(root.right, lst)
         lst.append(root.val)

   helper(root, elements)
   return elements

# print(postorder_traversal(root))

# Problem 7: Binary Tree Product
def tree_product(root: TreeNode) -> int:
   if not root:
      return 1

   def helper(root) -> int:
      if not root: 
         return 1

      left = helper(root.left)
      right = helper(root.right)
      return root.val * left * right
         
   return helper(root)

# print(tree_product(root))

# Problem 8: Binary Tree Is Leaf
def is_leaf(root: TreeNode | None, value: object) -> bool:
   if not root:
      return False
      
   if root.val == value:
      return root.left is None and root.right is None

   return is_leaf(root.left, value) or is_leaf(root.right, value)
# print(is_leaf(root, 3))

# Problem 9: Binary Search Tree Is Leaf
def is_leaf_bst(root: TreeNode | None, target: object) -> bool:
   if not root:
      return False

   print(root.val)
   if root.val == target:
      return (root.left is None) and (root.right is None)
   elif target < root.val:
      return is_leaf_bst(root.left, target)
   else:
      return is_leaf_bst(root.right, target)
      

print(is_leaf_bst(node1, 6))