from Node import Node

class Stack:
    def __init__(self, name):
        self.top_item = None
        self.limit = 1000
        self.name = name
        self.size = 0

    # the following function push a new item
    def push(self, value):
        if self.has_space() == True:
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
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
            print("Nothing to see here!")

    # the following function reads the head node
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_node_data()
        else:
            print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_name(self):
        return self.name
  
    def print_items(self):
        pointer = self.top_item
        print_list = []
        while(pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))