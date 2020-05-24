from LinkedList import LinkedList
#Linked List example

new_linked_list = LinkedList("Alejandro->")
new_linked_list.add_a_new_head_node("Bernal->")
new_linked_list.add_a_new_head_node("Camila->")
new_linked_list.add_a_new_head_node("Daniel->")
new_linked_list.add_a_new_head_node("Ernesto->")
print(new_linked_list.get_linked_list_values())

new_linked_list.delete_node_by_value("Ernesto->")
print(new_linked_list.get_linked_list_values())
