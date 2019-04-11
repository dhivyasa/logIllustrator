import logging
import logging.handlers
from search import depth_first
from search import breadth_first
from search.tree_node import Node
import queue

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('search.log', mode="w+")
formatter = logging.Formatter(
    '%(asctime)s - %(name)s -%(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
#========send cases when the result of False DFS searches to this queue
q = queue.Queue()
queue_handler = logging.handlers.QueueHandler(q)
queue_handler.setLevel(logging.CRITICAL)
depth_first_filter = logging.Filter("search.depth_first")
queue_handler.addFilter(depth_first_filter)
logger.addHandler(queue_handler)


def build_tree(input_values, index=0, node=Node()):
    root = None
    left_index = index + (index + 1)
    right_index = index + (index + 2)
    length = len(input_values) - 1
    if index == 0:
        root = Node(input_values[index])
        node = root
    if index == length or left_index > length or right_index > length:
        return

    node.left = Node(input_values[left_index])
    node.right = Node(input_values[right_index])
    build_tree(input_values, left_index, node.left)
    build_tree(input_values, right_index, node.right)
    return root


def print_tree(node):
    print(node.value)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)


def search():
    logger.info("Starting the search module")
    root = build_tree([1, 2, 3, 4, 6, 18, 10, 8, 34, 45, 53, 65])
    logger.info("Built Tree")
    bfs_result = breadth_first.search_breadth_first(root, Node(18))
    print(bfs_result)
    dfs_result = depth_first.search_depth_first(root, Node(18))
    print(dfs_result)
    dfs_result = depth_first.search_depth_first(root, Node(76))
    print(dfs_result)
    check_missed()

def check_missed():
    print("Checking queue")
    log_message = q.get()
    if log_message:
        print(
            f"Message on queue:\nname={log_message.name}, msg={log_message.msg}, level={log_message.levelname}")

if __name__ == '__main__':
    search()
    check_missed()
