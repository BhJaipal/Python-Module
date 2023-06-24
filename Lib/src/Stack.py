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
            self.list.pop()