
PRECEDENCE = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1
}

CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
LEFT_PAREN = '('
RIGHT_PAREN = ')'


def infix_to_postfix(infix_expression):
    operation_stack = []
    postfix = []
    tokens = infix_expression.split()

    for token in tokens:
        if token in CHARACTERS or token in DIGITS:
            postfix.append(token)
        elif token == LEFT_PAREN:
            operation_stack.append(token)
        elif token == RIGHT_PAREN:
            top_token = operation_stack.pop()
            while top_token != LEFT_PAREN:
                postfix.append(top_token)
                top_token = operation_stack.pop()
        else:
            while operation_stack and \
                    (PRECEDENCE[operation_stack[-1]] >= PRECEDENCE[token]):
                postfix.append(operation_stack.pop())
            operation_stack.append(token)

    while operation_stack:
        postfix.append(operation_stack.pop())
    return ' '.join(postfix)

infix_to_postfix('A * B + C * D')  # => 'A B * C D * +'
infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )')
# => 'A B + C * D E - F G + * -'
infix_to_postfix('( A + B ) * ( C + D )')  # => 'A B + C D + *'
infix_to_postfix('( A + B ) * C')  # => 'A B + C *'
infix_to_postfix('A + B * C')  # => 'A B C * +'
