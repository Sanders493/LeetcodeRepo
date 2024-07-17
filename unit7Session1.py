# Problem 1: Hello Hello


def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)


# repeat_hello(5)


def repeat_hello_iterative(n):
  for _ in range(n):
    print("Hello")

# repeat_hello_iterative(5)