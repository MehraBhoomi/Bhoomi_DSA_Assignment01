# Question 06] Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def postfix_to_prefix(postfix):
    stack = []

    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = token + operand1 + operand2
            stack.append(new_expr)

    return stack[0]

# Example usage
postfix_expression = "23+45*+"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Postfix expression:", postfix_expression)
print("Prefix expression:", prefix_expression)