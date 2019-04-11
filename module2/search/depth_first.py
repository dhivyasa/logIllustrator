from collections import deque
import logging

logger = logging.getLogger(__name__)

SEARCH_TYPE = "Depth-First"
logger.info(f"Program {SEARCH_TYPE} is starting")


def do_operation(node, search_node):
    return node.value == search_node.value


def search_depth_first(root_node, search_node):
    stack = deque()
    stack.append(root_node)

    while(len(stack)):
        node = stack.pop()
        adj_list = node.get_adjacency_list()
        logger.info("Processing node %s" % node.value)

        if do_operation(node, search_node):
            return True
        node.visited = True
        for n in adj_list:
            stack.append(n)
    logger.critical(f'DFS failed to find node {search_node.value}')        
    return False