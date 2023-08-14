# Question 10] Write a program to find the smallest number using a stack.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            if popped_item == self.min_stack[-1]:
                self.min_stack.pop()
            return popped_item

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def get_min(self):
        if not self.is_empty():
            return self.min_stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# Example usage
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print("Smallest number:", stack.get_min())

stack.pop()

print("Smallest number:", stack.get_min())