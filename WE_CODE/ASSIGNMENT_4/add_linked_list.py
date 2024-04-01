import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                if current.next is not None:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                new_node.prev = current
                return
            current = current.next
        self.add_to_front(data)

    def remove_first_occurrence(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next
                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev
                return
            current = current.next

    def remove_first(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def display(self):
        current = self.head
        if current is None:
            print("blank")
            return
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    linked_list = LinkedList()
    while True:
        line = sys.stdin.readline().strip().split()

        command = line[0]
        if command == "0":
            linked_list.add_to_front(int(line[1]))
        elif command == "1":
            linked_list.add_to_end(int(line[1]))
        elif command == "2":
            linked_list.insert_after(int(line[1]), int(line[2]))
        elif command == "3":
            linked_list.remove_first_occurrence(int(line[1]))
        elif command == "5":
            linked_list.remove_first()
        elif command == "6":
            break


    linked_list.display()

if __name__ == "__main__":
    main()
