__author__ = 'rameshho'

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        #self.head = Node()

    def InsertFront(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def InsertBack(self, data):
        new_node = Node(data)
        if not self.head:
            return self.head = new_node
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()



    def Search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                break
            current = current.get_next()

        return True

    def DeleteNode(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            previous.set_next(current.get_next())
            del current

    def Display(self):
        current = self.head
        while current:
            print("Info of node = %d", current.get_data())
            current = current.get_next()

if __name__ == "__main__":
    linkedlist = SinglyLinkedList()

    while 1:
        choice = eval(input("Enter the choice, 1 insert, 2 delete, 3 search, 4 display : "))
        switcher = {
            1: "InsertNode",
            2: "DeleteNode",
            3: "Search",
            4: "Display"
        }

        func_name = switcher.get(choice, "Nothing")

        if func_name == "Nothing":
            break
        if func_name == "InsertNode" or func_name == "DeleteNode" or func_name == "Search":
            item = input("Enter the item : ")
            print("func_name = %s" %func_name)
            #func = eval("linkedlist.func_name(item)")
            func = eval("linkedlist.%s(%s)" %(func_name, item))
        else:
            func = eval("linkedlist.%s()" %func_name)