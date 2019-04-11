class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.visited = False

    def get_adjacency_list(self):
        return list(filter(None, [self.left, self.right]))

    def __equals__(self, node):
        return node.value == self.value