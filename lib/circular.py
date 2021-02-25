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

class Circular:
    _length = 0
    def __init__(self):
      self.top = None

    def isEmpty(self):
      return self.top == None

    def pushTop(self,item):
      node = Node(item)
      if self.isEmpty():
        self.top = node
        node.setNext(self.top)
      else:
        current = self.top
        while current.getNext() is not self.top:
            current = current.getNext()
        current.setNext(node)
        node.setNext(self.top)
        self.top = node
      Circular._length+=1
    def pushBot(self, item):
      node = Node(item)
      if self.isEmpty():
        self.top = node
        node.setNext(self.top)
      else:
        current = self.top
        while current.getNext() is not self.top:
          current = current.getNext()
        current.setNext(node)
        node.setNext(self.top)
      Circular._length+=1
    def popTop(self):
      if not self.isEmpty():
        self.top = self.top.getNext()
        Circular._length-=1
    def popBot(self):
      if not self.isEmpty():
        current = self.top
        while current.getNext() != self.top:
          current = current.getNext()
        current.getNext().setNext(self.top)
        Circular._length-=1

    def size(self):
      return Circular._length

    def printElements(self, divider = ' '):
      current = self.top
      string = str(self.top.getValue()) + divider
      while current.getNext() != self.top:
        current = current.getNext()
        string += str(current.getValue())
        string += str(divider)
      print(string)
