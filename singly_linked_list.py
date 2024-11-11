class Node:
    def __init__(self, data: any, next: any = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'[{self.data}]->{self.next}'


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        return str(self.head)

    def lenght(self) -> int:
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_at_begin(self, data: any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node

    def remove_at_begin(self) -> None:
        if not self.head:
            return
        self.head = self.head.next

    def remove_at_end(self) -> None:
        if not self.head:
            return
        tmp = self.head
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None

    def reverse_list(self) -> Node:
        if not self.head:
            return self.head
        tmp = self.head
        reversed_list = Node(tmp.data)
        while tmp.next:
            tmp = tmp.next
            reversed_list = Node(tmp.data, reversed_list)
        return reversed_list

    def insert_at_index(self, data: any, index: int) -> None:
        if index == 0:
            self.insert_at_begin(data)

        pos = 0
        curr_node = self.head
        while (pos+1 != index and curr_node != None):
            pos += 1
            curr_node = curr_node.next

        if curr_node != None:
            new_node = Node(data)
            new_node.next = curr_node.next
            curr_node.next = new_node
        else:
            return

    def remove_at_index(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.remove_at_begin()
        else:
            curr_node = self.head
            pos = 0
            while (pos != index-1 and curr_node != None):
                pos += 1
                curr_node = curr_node.next
            if curr_node.next != None:
                curr_node.next = curr_node.next.next

    def update_node(self, data: any, new_data: any) -> None:
        if not self.head:
            return

        curr_node = self.head
        while curr_node != None and curr_node.data != data:
            curr_node = curr_node.next
        if curr_node != None:
            curr_node.data = new_data

    def get_node_value_by_index(self, index: int) -> any:
        if not self.head:
            return None

        pos = 0
        curr_node = self.head
        while curr_node != None and pos != index:
            curr_node = curr_node.next
            pos += 1

        if curr_node != None and pos == index:
            return curr_node.data
        return None

    def get_node_index_by_value(self, value: any) -> int | None:
        if not self.head:
            None

        index = 0
        curr_node = self.head
        while curr_node != None and curr_node.data != value:
            curr_node = curr_node.next
            index += 1

        if curr_node != None and curr_node.data == value:
            return index
        return None


linkedlist = LinkedList()
tmp = Node(1)
linkedlist.head = tmp
for i in range(2, 11):
    tmp.next = Node(i)
    tmp = tmp.next

print(linkedlist)
print(linkedlist.lenght())
linkedlist.insert_at_begin('Hello')
linkedlist.insert_at_end('Bye')
print(linkedlist)
linkedlist.remove_at_begin()
linkedlist.remove_at_end()
print(linkedlist)
print(linkedlist.reverse_list())
linkedlist.insert_at_index('Inserted data', 5)
print(linkedlist)
linkedlist.remove_at_index(5)
print(linkedlist)
linkedlist.update_node(10, 11)
print(linkedlist)
print(linkedlist.get_node_value_by_index(9))
print(linkedlist.get_node_index_by_value(11))
