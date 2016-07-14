__author__ = 'rameshho'

class Stack(object):
    def __init__(self, stacksize):
            self.stack = []
            self.stacksize = stacksize
            self.counter = 0

    def push(self, item):
        if self.counter < self.stacksize:
            self.stack.append(item)
            self.counter += 1
        else:
            print("Stack is full, cannot perform push operation")
        return

    def pop(self):
        if self.counter:
            self.counter -= 1
            return self.stack.pop()
        else:
            return -1

    def display(self):
        if counter:
            for i in self.stack:
                print(i)
        else:
            print("Stack is empty")

if __name__ == "__main__":

    stacksize = input("Enter the stack size : ")
    my_stack = Stack(stacksize)
    while 1:
        choice = input("Enter the choice #1 : Push, #2 : Pop, #3 to display :- ")
        switcher = {
            1: "push",
            2: "pop",
            3: "display"
        }

        func_name = switcher.get(choice, "nothing")

        if func_name == "nothing":
            break
        func = getattr(my_stack, func_name )

        if func_name == "push":
            item = input("Item to be inserted in a list : ")
            func(item)
        elif func_name == "pop":
            popped_item = func()
            if popped_item == -1:
                print("Stack is empty")
            else:
                print("Item popped out : ", popped_item)