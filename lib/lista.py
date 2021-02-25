class Node:
    def __init__(self, value, n = None):
        self.value = value
        self.next = n
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,value):
        self.value = value

    def setNext(self,n):
        self.next = n

class Lista:
    _length = 0
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self,item):
        tmp = Node(item)
        tmp.setNext(self.top)
        self.top = tmp
        Lista._length+=1
    def size(self):
        return Lista._length
    def peek(self):
        return self.top.getValue()
    def pop(self):
        if not self.isEmpty():
            current = self.top.getValue()
            self.top = self.top.getNext()
            return current