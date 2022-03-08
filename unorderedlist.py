class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    @property
    def size(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

ul = UnorderedList()
ul.add(10)
ul.add(13)
ul.add(11)
ul.add(5)

#list traversing
node = ul.head
while node is not None:
    print(node.value)
    node = node.next

print(ul.size)