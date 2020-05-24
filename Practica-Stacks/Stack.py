from Node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    
    # the following function push a new item
    def push(self, value):
        if self.has_space() == True:
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size = self.size +1
            print("Adding {} to the pizza stack!".format(value))

    # the following fuctions returns and remove the head node    
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size = self.size -1
            print("Delivering " + item_to_remove.get_node_data())
            return item_to_remove.get_node_data()
            
        else:
            print("The stack is empty")
    # the following function reads the head node
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_node_data()
        else:
            print("The stack is empty")
    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

