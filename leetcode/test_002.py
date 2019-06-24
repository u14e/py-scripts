###############################################################################
# https://leetcode.com/problems/add-two-numbers/
###############################################################################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)

def add_two_numbers(l1, l2):
    l = Node('head')
    tmp = l
    step = 0
    while (l1.next is not None) or (l2.next is not None):
        two_sum = step
        step = 0
        if l1.next is not None:
            two_sum += l1.next.value
            l1 = l1.next
        if l2.next is not None:
            two_sum += l2.next.value
            l2 = l2.next
        if two_sum > 9:
            step = 1
            two_sum -= 10
        print(two_sum)
        tmp.next = Node(two_sum)
        tmp = tmp.next
    return l

def print_linked_list(l):
    s = ''
    while l.next:
        s += (str(l.next) + ' -> ')
        l = l.next
    return s

def test_add_two_numbers():
    l1 = Node('head')
    l1.next = Node(2)
    l1.next.next = Node(4)
    l1.next.next.next = Node(3)

    l2 = Node('head')
    l2.next = Node(5)
    l2.next.next = Node(6)
    l2.next.next.next = Node(4)

    l = add_two_numbers(l1, l2)
    assert print_linked_list(l) == '7 -> 0 -> 8 -> '