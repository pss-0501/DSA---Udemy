class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = next
        
class Stack:
    def __init__(self, value) -> None:
        newnode = Node(value)
        self.top = newnode
        self.height = 1


my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""