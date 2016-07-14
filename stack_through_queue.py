__author__ = 'rameshho'

class Queue(object):

 #   counter = 0

    def __init__(self):
        self.queue = []
        self.queue_counter = 0
#       counter += 1

    def enqueue(self, item):
            self.queue.append(item)
            self.queue_counter += 1

    def dequeue(self):
        if not self.queue_counter:
            print("queue is empty, dequeue is not possible")
        else:
            ret = self.queue[0]
            self.queue_counter -= 1
            del(self.queue[0])
            return ret
        return -1

    def isempty(self):
        if not self.queue_counter:
            return True

    def size(self):
        return self.queue_counter

class Stack(Queue):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.enqueue(item)

    def pop(self):
        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())

        popped_item = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return popped_item

    def display(self):
        while self.q1.size() >= 1:
            item = self.q1.dequeue()
            print(item)
            self.q2.enqueue(item)

        self.q1, self.q2 = self.q2, self.q1

if __name__ == "__main__":
    my_stack = Stack()
    while 1:
        choice = input("Enter the choice: 1 push, 2 pop, 3 Display : ")
        switcher = {
            1: "push",
            2: "pop",
            3: "display"
        }

        func_name = switcher.get(choice, "nothing")
        print("func_name = "+func_name)
        if func_name == "nothing":
            print("Invalid option")
            break
        func = getattr(my_stack, func_name )
        print(func)
        if func_name == "pop":
            print("popped item = %d", func())
        elif func_name == "push":
            item = input("Enter item to insert : ")
            func(item)
        elif func_name == "display":
            func()
        else:
            print("Invalid Option")
            break
