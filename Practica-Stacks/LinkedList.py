# Our LinkedList class
from Node import Node
class LinkedList:
    def __init__(self,node_value = None):
        self.head_node = Node(node_value)
    
    def get_head_node(self):
        return self.head_node
    
    def add_a_new_head_node(self, new_node_data):
        new_node = Node(new_node_data)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def delete_head_node(self):
        if self.head_node.get_node_data() != None:
            self.head_node = self.head_node.get_next_node()

    def delete_node_by_value(self, value):
        head_node = self.get_head_node()

        if head_node.get_node_data() == value:
            self.delete_head_node()
        else:
            while(head_node):
                next_node = head_node.get_next_node()
                if next_node.get_node_data() == value:
                    head_node.set_next_node(next_node.get_next_node())
                    head_node = None                    
                else:
                    head_node = next_node
    def count_nodes(self):
        pass
    
    def get_linked_list_values(self):
        values_fromLinkedList  = []
        head_node = self.get_head_node()
        while(head_node):
            head_node_data = head_node.get_node_data()
            if head_node_data != None:
                values_fromLinkedList.append(head_node_data)
            head_node = head_node.get_next_node()

        return values_fromLinkedList

