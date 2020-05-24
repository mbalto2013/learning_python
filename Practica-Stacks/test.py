from LinkedList import LinkedList
from Stack import Stack
#Linked List example
"""
new_linked_list = LinkedList("Alejandro->")
new_linked_list.add_a_new_head_node("Bernal->")
new_linked_list.add_a_new_head_node("Camila->")
new_linked_list.add_a_new_head_node("Daniel->")
new_linked_list.add_a_new_head_node("Ernesto->")
print(new_linked_list.get_linked_list_values())

new_linked_list.delete_node_by_value("Ernesto->")
print(new_linked_list.get_linked_list_values())
"""

# Stack example
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
  
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
#pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
#pizza_stack.pop()