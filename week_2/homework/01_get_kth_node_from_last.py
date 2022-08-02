class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        length = 1
        cur = self.head

        # 시간 복잡도가 같지만 두개가 다른 구현방법, 결국 시간 복잡도를 계산 해보아야함
        # O(N) + O(N - K) 의 시간 복잡도
        # while cur.next is not None:
        # cur = cur.next
        #     length += 1
        # end_length = length - k
        # cur = self.head
        # for i in range(end_length):
        #     cur = cur.next
        # return cur

        # O(N) + O(N - K) 의 시간 복잡도
        # 위와 같이 결국 n만큼 for문이 한번돌고, 나머지 for문은 n-k 만큼 돈다
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
