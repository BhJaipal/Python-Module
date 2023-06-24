class Stack:
    def __init__(self):
        self.list= list()
    def push(self, elem):
        self.list.append(elem)
    def pushMany(self, *args):
        self.list.extend(s)