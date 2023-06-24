from Lib.Stack import *

newStack= Stack()
newStack.push(4)
newStack.pushMany(3, 4, 2, 7)
print(f"3 poped elements are: {newStack.popMany(3)}")
print("R")