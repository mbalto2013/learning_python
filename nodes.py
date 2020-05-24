class Node:
    def __init__(self,data, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, another_node):
        self.next_node  = another_node

class LinkedList:
    def __init__(self, new_node_value):
        self.head_node = Node(new_node_value)
    def get_head_node(self):
        return self.head_node
    def insert_new_node(self, new_node_data):
        new_node = Node(new_node_data)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    def remove_node_by_value(self, node_value):
        head_node = self.get_head_node()
        if head_node.get_data() ==  node_value:
            self.head_node = head_node.get_next_node()
        else:
            while (head_node):
                next_node = head_node.get_next_node()
                if next_node.get_data() == node_value:
                    head_node.set_next_node(next_node.get_next_node())
                    head_node = None
                else:
                    head_node = next_node
    def remove_duplicate_nodes(self, value):
        pass

    def list_values(self):
        head_node = self.get_head_node()
        list_values =[]
        while(head_node):
            head_node_data = head_node.get_data()
            if head_node_data != None:
                list_values.append(head_node_data)
            head_node = head_node.get_next_node()
        return list_values


print('Initial data blocks')
linkedList = LinkedList('data_block1')
linkedList.insert_new_node('data_block2')
linkedList.insert_new_node('data_block3')
linkedList.insert_new_node('data_block4')
linkedList.insert_new_node('data_block5')
linkedList.insert_new_node('data_block6')
print(linkedList.list_values())

linkedList.remove_node_by_value('data_block4')
print('Results after deleting data_block4')
print(linkedList.list_values())
