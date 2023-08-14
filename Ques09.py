# Question 09]  Write a program to reverse a stack.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def reverse(self):
        aux_stack = Stack()

        while not self.is_empty():
            aux_stack.push(self.pop())

        while not aux_stack.is_empty():
            self.push(aux_stack.pop())


# Example usage
original_stack = Stack()
original_stack.push(1)
original_stack.push(2)
original_stack.push(3)
original_stack.push(4)
original_stack.push(5)

print("Original Stack:", original_stack.items)

original_stack.reverse()

print("Reversed Stack:", original_stack.items)