class Node:
    def __init__(self, data, link_to_next_node = None):
        self.data = data
        self.link_to_next_node = link_to_next_node

    def get_node_data(self):
        return self.data

    def get_next_node(self):
        return self.link_to_next_node

    def set_next_node(self,another_node):
        self.link_to_next_node = another_node
    