
def construct_expression(parse_tree):
    if parse_tree is None:
        return ''

    left = construct_expression(parse_tree.get('left'))
    right = construct_expression(parse_tree.get('right'))
    val = parse_tree['val']

    if left and right:
        return '({}{}{})'.format(left, val, right)

    return val
