class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # head 에 시작하는 Node 를 연결합니다.

    def append(self, data):     # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        cur = self.head
        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다.
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()


