class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

    def set_data(self,item):
        self.data = item
    
    def get_data (self):
        return self.data

    def set_next(self,item):
        self.next = item

    def get_next(self):
        return self.next

    
class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self,item):
        n = Node(item)
        n.next= self.head
        self.head = n
    
    def remove(self,item):
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        if previous == None:
            self.head = current.next
        elif current == None:
            raise ValueError("Item Not in the list")
        else:
            previous.next = current.next

    def __str__(self):
        current = self.head
        data = []
        while current is not None:
            data.append(current.data)
            current = current.next
        return str(data[::-1])
    
    def search(self,item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def count(self):
        current = self.head
        number = 0
        while current is not None:
            number += 1
            current = current.next
        return number
    





a = UnorderedList()
a.add(2)
a.add(3)
a.add(4)
a.remove(4)
print(a.search(2))
print(a.count())