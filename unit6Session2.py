class Node:

  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# Problem 1: Detect Circular Linked List


def is_circular(head):
  if not head:
    return False

  current = head.next

  while current.next:
    if current == head:
      return True
    current = current.next
  return False


# node3 = Node(3)
# node2 = Node(2, node3)
# node1 = Node(1, node2)
# node3.next = node1
# print(is_circular(node1))

# Problem 2: Find Last Node in a Linked List Cycle


def find_last_node_in_cycle(head) -> Node | None:
  if not head:
    return None
  slow = head
  fast = head

  while fast.next and fast.next.next:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      break
  else: 
    return None

  slow = head
  while slow != fast:
      slow = slow.next
      fast = fast.next


  last_node = slow
  while last_node.next != slow:
      last_node = last_node.next

  return last_node.value

# node4 = Node(4)
# node3 = Node(3, node4)
# node2 = Node(2, node3)
# node1 = Node(1, node2)
# node4.next = node2
# print(find_last_node_in_cycle(node1))
