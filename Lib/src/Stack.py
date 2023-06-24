class Stack:
    def __init__(self):
        self.list= list()
    def push(self, elem):
        self.list.append(elem)
    def pushMany(self, *args):
        self.list.extend(args)
    def pop(self):
        if len(self.list) == 0:
            print("Stack is empty, please fill some elements first")
            self.push(input("Enter element: "))
        else:
            return self.list.pop()
    def popMany(self, n: int):
        popedElemList= []
        for i in range(n):
            if self.pop()
            popedElemList.append(self.pop())
        return popedElemList
    def length(self)-> int:
        return len(self.list)
    def printList(self):
        for i in self.list:
            print(i, end=" ")
        print("")
Stack().popMany()