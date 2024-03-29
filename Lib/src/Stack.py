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
        # removing last n elements of Stack from back
        popedElemList= []
        for i in range(n):
            popedElemList.append(self.pop())
        return popedElemList
    def length(self)-> int:
        # length of Stack
        return len(self.list)
    def printList(self):
        # a good way to print Stack
        for i in self.list:
            print(i, end=" ")
        print()
    def search(self, element):
        # searches for element, if not found return -1 else index in list
        found = -1
        for i in self.list:
            if i== element:
                found = self.list.index(i)
                break
            else:
                continue
        if found== -1:
            return -1
        else:
            return found
    def extend(self, elemList: list):
        # extends a elements of a list to Stack
        self.list.extend(elemList)
