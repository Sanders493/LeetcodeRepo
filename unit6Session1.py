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


node1 = Node(3, Node(1, Node(2, Node(1))))
print(count_element(node1, 1))
# 3 -> 1 -> 2 -> 1
