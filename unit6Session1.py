# Problem 2: Find Frequency


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def count_element(head: Node, val: object) -> int:
  count: int = 0
  current: Node | None = head
  while current:
    if current.value == val:
      count += 1
    current = current.next

  return count


# node1 = Node(3, Node(1, Node(2, Node(1))))
# print(count_element(node1, 1))
# 3 -> 1 -> 2 -> 1

# Problem 3: Remove Tail


# Helper function to print the linked list
def print_list(node):
  current = node
  while current:
    print(current.value, end=" -> " if current.next else "")
    current = current.next
  print()


# I have a bug!
def remove_tail(head):
  if head is None:  # If the list is empty, return None
    return None
  if head.next is None:  # If there's only one node, removing it leaves the list empty
    return None

# Start from the head and find the second-to-last node
  current = head
  while current.next.next:
    current = current.next

  current.next = None  # Remove the last node by setting second-to-last node to None
  return head


# node1 = Node(1, Node(2, Node(3, Node(4))))
# print_list(node1)
# remove_tail(node1)
# print_list(node1)

# Problem 4: Find the middle


def get_ll_length(head: Node | None) -> int:
  length = 0
  current: Node | None = head
  while current:
    length += 1
    current = current.next
  return length


def find_middle_element(head) -> object:
  length: int = get_ll_length(head)

  fast = head
  slow = head

  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

  return slow.value if length % 2 != 0 else slow.next.value


# node1 = Node(1, Node(2, Node(3)))
# print(find_middle_element(node1))

# Problem 5: Is Palindrome?


def is_palindrome(head: Node | None) -> bool:
  if not head:
    return False

  elements: list[object] = []
  current: Node | None = head

  while current:
    elements.append(current.value)
    current = current.next

  return elements == elements[::-1]


# node1 = Node(1, Node(2, Node(1)))
# print(is_palindrome(node1))

# Problem 6: Put it in Reverse


def reverse(head: Node | None) -> Node | None:
  if not head:
    return None

  elements = []
  current = head

  while current:
    elements.append(current.value)
    current = current.next

  elements.reverse()
  new_head = Node(elements.pop(0))
  current = new_head

  for elem in elements:
    current.next = Node(elem)
    current = current.next

  return new_head

def is_circular(head):
  if not head.next:
    return False
    
  current = head.next

  while current.next:
    if current == head:
      return True
  return False

# node1 = Node(1, Node(2, Node(3, Node(4))))
# print_list(node1)
# new_node1 = reverse(node1)
# print_list(new_node1)
