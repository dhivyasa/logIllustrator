from collections import deque
import logging


logger = logging.getLogger(__name__)

SEARCH_TYPE = "Breadth-First"
logger.info(f"Program {SEARCH_TYPE} is starting")


def do_operation(node, search_node):
    return node.value == search_node.value

def search_breadth_first(root_node, search_node):
    logger.info("Starting to search Breadth-First")
    queue = deque()
    queue.append(root_node)

    while(len(queue)):
        node = queue.popleft()
        adj_list = node.get_adjacency_list()
        logger.info("Processing node %s" % node.value)

        if do_operation(node, search_node):
            return True
        node.visited = True
        for n in adj_list:
            queue.append(n)
    return False