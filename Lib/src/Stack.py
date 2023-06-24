class Stack:
    def __init__(self, *args):
        self.list= list(args)
    def push(self, elem):
        # pushing one element to Stack
        self.list.append(elem)
    def pushMany(self, *args):
        # pushing more than one elements to Stack
        self.list.extend(args)
    def pop(self):
        # removing last element out of stack
        if len(self.list) == 0:
            print("Stack is empty, please fill some elements first")
            self.push(input("Enter element: "))
            self.pop()
            # inserting a element to remove it from Stack
        else:
            return self.list.pop()
    def popMany(self, n: int):
        
        popedElemList= []
        for i in range(n):
            popedElemList.append(self.pop())
        return popedElemList
    def length(self)-> int:
        return len(self.list)
    def printList(self):
        for i in self.list:
            print(i, end=" ")
        print()
