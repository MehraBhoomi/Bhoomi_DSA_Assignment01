# Question 07] Write a program to convert prefix expression to infix expression.

def is_operator(char):
    return char in "+-*/"

def prefix_to_infix(prefix):
    stack = []

    for token in reversed(prefix):
        if not is_operator(token):
            stack.append(token)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expr = f"({operand1}{token}{operand2})"
            stack.append(new_expr)

    return stack[0]

# Example usage
prefix_expression = "+*23*45"
infix_expression = prefix_to_infix(prefix_expression)
print("Prefix expression:", prefix_expression)
print("Infix expression:", infix_expression)