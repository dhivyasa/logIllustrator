from collections import deque
import logging
logging.basicConfig(level=logging.INFO,
                    filename="search.log",
                    format="%(name)s : %(levelname)s :%(process)s :%(message)s", 
                    filemode="w+")

SEARCH_TYPE="Depth-First"
logging.info("Program %s is starting"% SEARCH_TYPE)
logging.info("Program %s is starting",SEARCH_TYPE)
logging.info(f"Program {SEARCH_TYPE} is starting")

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
        
def build_tree(input_values, index=0, node=Node()):
    root = None
    left_index = index+(index+1)
    right_index = index+(index+2)
    l = len(input_values) - 1
    if index == 0:
        root = Node(input_values[index])
        node = root
    if index == l or left_index > l or right_index > l:
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

def do_operation(node, search_node):
    return node.value == search_node.value 

def search_depth_first(root_node, search_node):
    stack = deque()
    stack.append(root_node)
    
    while(len(stack)):
       node = stack.pop()
       adj_list = node.get_adjacency_list()
       logging.info("Processing node %s"%node.value)

       if do_operation(node, search_node):
           return True
       node.visited = True
       for n in adj_list:
           stack.append(n)
    return False 

if __name__ == "__main__":
        try: 
            root = build_tree([1, 2, d, 4, 6, 18, 10, 8, 34, 45, 53, 65])
            print(search_depth_first(root, Node(18)))
        except Exception:
            logging.exception("Something went wrong")

