import operator

OPERATION = {
    '*': operator.mul,
    '/': operator.div,
    '-': operator.sub,
    '+': operator.add
}

DIGITS = set('0123456789')


def evaluate_postfix(postfix_expression):
    operand_stack = []

    for token in postfix_expression.split():
        if token in DIGITS:
            operand_stack.append(int(token))
        else:
            b = operand_stack.pop()
            a = operand_stack.pop()
            result = OPERATION[token](a, b)
            operand_stack.append(result)
    return operand_stack.pop()

evaluate_postfix('7 8 + 3 2 + /')  # => 3.0
