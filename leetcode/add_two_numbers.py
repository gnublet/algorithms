from typing import * # type hinting
# from copy import deepcopy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Explanation: res and temp_res both initialzed to point to ListNode(0).
        We'll use temp_res as a cursor to add new results while res remains pointing at the head
        Finally, we'll return res.next. ListNode(0) was just a dummy ListNode.
        carry takes into account over 10 additions (see elementary school)
        We wanted to traverse each LinkedList individually since they may be of different sizes
        """
        res = temp_res = ListNode(0)
        carry = 0
        res_val = 0
        while l1 or l2 or carry:
            l1_val = 0
            l2_val = 0
            if l1 != None:
                l1_val = l1.val
                l1 = l1.next
            if l2 != None:
                l2_val = l2.val
                l2 = l2.next
            res_val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            print('res_val' + str(res_val) + str(type(res_val)))
            temp_res.next = ListNode(res_val)

            # print(temp_res)
            # print(res)
            # print(res.next)
            temp_res = temp_res.next
        return res.next

def print_ListNode(l):
    while l != None:
        # print(str(l.val))
        print(l.val, end=' > ')
        # print(str(l.val) + ' > ')
        l = l.next

if __name__ == '__main__':
    s = Solution()
    # construct 2 example linked lists
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # run algorithm
    ans = s.addTwoNumbers(l1, l2)
    print_ListNode(ans)