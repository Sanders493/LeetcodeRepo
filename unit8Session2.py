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

# class TreeNode():

#    def __init__(self, key, value, left=None, right=None):
#       self.key = key
#       self.val = value
#       self.left = left
#       self.right = right


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


# node1 = TreeNode(10, "Neiji")
# node1.left = TreeNode(8, "Sasuke")
# node1.right = TreeNode(15, "Itachi")
# node1.left.left = TreeNode(1, "Kakashi")
# node1.left.right = TreeNode(6, "Ino")

# insert(node1, 0, "Naruto")
# print(node1.left.left.left.val)


# Problem 4: BST Remove I
def find_smallest_child(root: TreeNode) -> TreeNode:
   min_node: TreeNode = TreeNode(float("inf"), "temp")

   def helper(node: TreeNode | None) -> None:
      nonlocal min_node
      if node:
         if node.key < min_node.key:
            min_node = node
         helper(node.right)
         helper(node.left)

   helper(root)

   return min_node


def remove_bst(root: TreeNode | None, key: int) -> TreeNode | None:
   if not root:
      return None

   if root.key > key:
      root.left = remove_bst(root.left, key)
   elif root.key < key:
      root.right = remove_bst(root.right, key)
   else:
      if not root.left:
         return root.right
      if not root.right:
         return root.left

      temp_node: TreeNode = find_smallest_child(root.right)
      root.key = temp_node.key
      root.val = temp_node.val
      root.right = remove_bst(root.right, temp_node.key)

   return root


# node1 = TreeNode(10, "Neiji")
# node1.left = TreeNode(8, "Sasuke")
# node1.right = TreeNode(15, "Itachi")
# node1.left.left = TreeNode(1, "Kakashi")
# node1.left.right = TreeNode(9, "Ino")
# node1.right.left = TreeNode(13, "Madara")
# node1.right.right = TreeNode(17, "Shoji")
# remove_bst(node1, 10)
# print(node1.val)


# Problem 5: BST In-order Successor
def inorder_successor(root: TreeNode | None, current: TreeNode):
   if not root:
      return None
   node: TreeNode | None = root
   prev: TreeNode | None = None
   while node:
      if node.key > current.key:
         if not node.left:
            print(f"Node with key {current.key} not found")
            return None
         prev = node
         node = node.left
      elif node.key < current.key:
         if not node.right:
            print(f"Node with key {current.key} not found")
            return None
         prev = node
         node = node.right
      else:
         if not node.right:
            if prev:
               if prev.key < root.key and prev.key > node.key:
                  return prev
               elif node.key < root.key:
                  return root
            else:
               return None
         return find_smallest(node.right)


def find_smallest(node: TreeNode) -> TreeNode:
   min_node = node

   def helper(node: TreeNode | None) -> None:
      nonlocal min_node
      if node:
         if node.key < min_node.key:
            min_node = node
         helper(node.left)
         helper(node.right)

   helper(node)
   return min_node


# print(inorder_successor(node1, node1.right).val)

## Version 3


# Problem 1: Is Odd-valued
def count_odds(root: TreeNode | None) -> int:
   if not root:
      return 0
   if root.val % 2 != 0:
      return 1 + count_odds(root.left) + count_odds(root.right)
   else:
      return 0 + count_odds(root.left) + count_odds(root.right)


# node1 = TreeNode(1)
# node1.left = TreeNode(3)
# node1.right = TreeNode(2)
# node1.left.left = TreeNode(8)
# node1.right.right = TreeNode(13)
# print(count_odds(node1))


# Problem 2: Binary Tree Min
def tree_min(root: TreeNode | None) -> TreeNode | None:
   if not root:
      return None
   min_node: TreeNode = TreeNode(float("inf"))

   def helper(node: TreeNode | None) -> None:
      nonlocal min_node
      if node:
         if node.val < min_node.val:
            min_node = node
         helper(node.left)
         helper(node.right)

   helper(root)
   return min_node


# node1 = TreeNode(15)
# node1.left = TreeNode(3)
# node1.right = TreeNode(2)
# node1.left.left = TreeNode(8)
# node1.right.right = TreeNode(13)
# print(tree_min(node1).val)


# Problem 3: BST Insert III
def insert_with_duplicates(root, value) -> TreeNode:
   if not root:
      return TreeNode(value)

   current: TreeNode | None = root

   while current:
      if current.val == value:
         if not current.left:
            current.left = TreeNode(value)
            break
         current.left = insert_with_duplicates(current.left, value)
         break
      elif current.val > value:
         if not current.left:
            current.left = TreeNode(value)
            break
         current = current.left
      else:
         if not current.right:
            current.right = TreeNode(value)
            break
         current = current.right
   return root


# node2 = TreeNode(10)
# node2.left = TreeNode(8)
# node2.right = TreeNode(15)
# node2.left.left = TreeNode(1)
# node2.left.right = TreeNode(6)
# insert_with_duplicates(node2, 10)
# print(node2.left.right.right.val)


# Problem 4: BST Remove III
def remove_bst_II(root, key):
   # Locate the node to be removed
   # If the node is a leaf node:
   # Remove the node by redirecting the appropriate child reference of its parent to None
   # If the node has one parent:
   # Replace the node with its child, updating its parent's nodes child reference appropriately
   # If the node has two children:
   # Find the largest node in the node's left subtree.
   # Set the root of the node's right subtree as the right child of the largest node in the node's left subtree.
   # Return the root of the updated tree
   pass
