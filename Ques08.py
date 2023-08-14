# Question 08]  Write a program to check if all the brackets are closed in a given code snippet


def are_brackets_balanced(code):
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in code:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if bracket_pairs[top] != char:
                return False

    return len(stack) == 0

# Example usage
code_snippet = "(a + [b * c])"
if are_brackets_balanced(code_snippet):
    print("All brackets are properly closed.")
else:
    print("Brackets are not balanced.")