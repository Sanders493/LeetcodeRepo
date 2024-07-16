class Node:

  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# Problem 1: Detect Circular Linked List
def print_ll(head) -> None:
  current = head
  lst: list[str] = []

  while current:
    lst.append(str(current.value))
    current = current.next

  print(" -> ".join(lst))


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

# Problem 3: Partition List Around Value


def partition(head, val):
  if not head:
    return None

  greater_head = Node(0)
  lesser_head = Node(0)

  less = lesser_head
  great = greater_head

  current = head
  while current:
    if current.value < val:
      less.next = current
      less = less.next
    else:
      great.next = current
      great = great.next
    current = current.next

  if great != greater_head:
    less.next = greater_head.next

  greater_head.next = None
  great.next = None
  return lesser_head.next


# node1 = Node(3, Node(2, Node(1, Node(5, Node(10, Node(5, Node(8)))))))
# 3 -> 2 -> 1 -> 5 -> 10 -> 5 -> 8
# print_ll(partition(node1, 5))

# Problem 4: Convert Binary Number in a Linked List to Integer

def binary_to_int(head):
  length = 0
  total = 0

  current = head
  while current.next:
    length += 1
    current = current.next

  divisor = 2 ** length
  current = head
  while current:
    total += current.value * divisor
    divisor /= 2
    current = current.next

  return int(total)

# node1 = Node(1, Node(0, Node(1, Node(1, Node(1, Node(0, Node(1)))))))
# node2 = Node(1, Node(0, Node(1)))
# print(binary_to_int(node2))
# print(binary_to_int(node1)) 

def add_two_numbers(head_a: Node, head_b: Node) -> Node:
  num1_str: str = ""
  num2_str: str = ""

  current = head_a
  while current:
    num1_str = str(current.value) + num1_str
    current = current.next

  current = head_b
  while current:
    num2_str = str(current.value) + num2_str
    current = current.next

  sum = int(num1_str) + int(num2_str)

  num_list = str(sum).split()
  new_head = Node(num_list.pop(0))
  current = new_head
  for num in num_list:
    current.next = Node(num)
    current = current.next

  return new_head

# node4 = Node(4)
# node3 = Node(3, node4)
# node2 = Node(2, node3)
# node1 = Node(1, node2)

# node5 = Node(1, Node(0, Node(1)))

# print_ll(add_two_numbers(node1, node5))


