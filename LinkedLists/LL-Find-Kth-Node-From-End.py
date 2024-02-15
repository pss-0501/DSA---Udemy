class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
    def find_kth_from_end(self, k):
        slow = fast = self.head
        for _ in range(k):          # 1,2
            if fast is None:
                return None
            fast = fast.next
            
        while fast:             # while fast is not null
            slow = slow.next    # 2,3,4
            fast = fast.next    # 3,4,5
        return slow
        
            


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = my_linked_list.find_kth_from_end(k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

