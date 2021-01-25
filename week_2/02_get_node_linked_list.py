# 링크드 리스트에서 index번째 원소를 반환하시오.

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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        cnt = 0

        while cnt < index:
            node = node.next
            cnt += 1

        return node


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(0).data)  # -> 5를 들고 있는 노드를 반환
