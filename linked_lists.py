class Node:
    prev = None
    prox = None
    value = None

def append(node, value):
    while node.prox != None:
        node = node.prox

    new_node = Node()
    new_node.value = value
    node.prox = new_node

def print_linked_list(node):
    if node != None:
        print(node.value)
        print_linked_list(node.prox)


first_node = Node()
first_node.value = 1

append(first_node, 2)
append(first_node, 'b')
append(first_node, 'foo')
append(first_node, 123)
print_linked_list(first_node)
    
