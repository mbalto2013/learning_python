from Node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.current_size = 0
  
  def enqueue(self, node_value):
    item_to_add = Node(node_value)
    if self.has_space():
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.current_size +=1
      print(f"Adding: {node_value}")
    else:
        print('There is no room')
  
  def dequeue(self):
    if self.get_current_size() > 0:
        item_to_remove = self.head
        if self.get_current_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next_node()
        self.current_size = self.current_size - 1
        print(f"Removing: {item_to_remove.get_node_data()}")
        return item_to_remove.get_node_data()
    else:
        return

  def get_current_size(self):
    return self.current_size
  
  def is_empty(self):
    return self.current_size ==0

  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.current_size
   
my_queue = Queue(5)
my_queue.enqueue("Order #1")
my_queue.enqueue("Order #2")
my_queue.enqueue("Order #3")
my_queue.enqueue("Order #4")
my_queue.enqueue("Order #5")
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

