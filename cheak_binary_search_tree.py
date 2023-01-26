INT_MAX = 10000
INT_MIN = -1


def check_binary_search_tree_(node):
    return check_node(node, INT_MIN, INT_MAX)


def check_node(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (check_node(node.left, mini, node.data - 1) and
            check_node(node.right, node.data + 1, maxi))
