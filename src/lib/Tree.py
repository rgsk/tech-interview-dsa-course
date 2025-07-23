from typing import List, Optional


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if node.right is None and node.left is None:
        line = '%s' % node.data
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = '%s' % node.data
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def displayTree(node):
    lines, *_ = _display_aux(node)
    for line in lines:
        print(line)


def formTree(values: list[int | None]):
    def is_null(val):
        return val is None or val == -1

    if not values or is_null(values[0]):
        return None

    root = Node(values[0])
    queue: list[Optional[Node]] = [root]
    i = 1

    while i < len(values):
        top = queue.pop(0)
        if top:
            # Left child
            if i < len(values) and not is_null(values[i]):
                top.left = Node(values[i])
            queue.append(top.left if i < len(values) else None)
            i += 1

            # Right child
            if i < len(values) and not is_null(values[i]):
                top.right = Node(values[i])
            queue.append(top.right if i < len(values) else None)
            i += 1
    return root
