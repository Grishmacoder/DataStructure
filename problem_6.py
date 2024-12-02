from typing import Optional

class Node:

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList:

    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string + "None"

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    # Use a set to store all unique elements
    result_set = set()

    # Create a new linked list to store the union
    result_list = LinkedList()
    node = llist_1.head
    while node:
        if node.value not in result_set:
            result_set.add(node.value)
            result_list.append(node.value)
        node = node.next
    node = llist_2.head
    while node:
        if node.value not in result_set:
            result_set.add(node.value)
            result_list.append(node.value)
        node = node.next
    return result_list

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    if llist_1.size() == 0 or llist_2.size() == 0:
        return LinkedList()
    # Use sets to find the intersection
    set1 = set()

    # Find the intersection of both sets
    intersect_set = set()
    intersect_list = LinkedList()

    # Create a new linked list to store the intersection
    node = llist_1.head
    while node:
        set1.add(node.value)
        node = node.next
    node = llist_2.head
    while node:
        if node.value in set1 and node.value not in intersect_set:
            intersect_set.add(node.value)
            intersect_list.append(node.value)
        node = node.next
    return intersect_list

if __name__ == "__main__":
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: empty

    ## Test case 3 large input
    print("\nTest Case 3:")
    linked_list_8 = LinkedList()
    linked_list_9 = LinkedList()
    element_4 = list(range(1, 101))
    element_5 = list(range(50, 151))
    for i in element_4:
        linked_list_8.append(i)
    for i in element_5:
        linked_list_9.append(i)
    print(union(linked_list_8, linked_list_9))
    print(intersection(linked_list_8, linked_list_9))

