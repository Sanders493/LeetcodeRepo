class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
    
def remove(head: Node | None, val: int) -> Node | None:
  if not head:
    return None
  temp_head: Node = Node("temp", head)
  
  current: Node | None = head
  prev: Node | None = None

  while current:
    if current.value == val:
      prev.next = current.next
      break
    else:
      prev = current
      current = current.next

  return temp_head.next