# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0

        beggining_res = ListNode()
        res = beggining_res

        while l1 and l2:
            if l1.val + l2.val + carry >= 10:
                res.next = ListNode(val = (l1.val + l2.val + carry)%10)
                carry = 1
            else:
                res.next = ListNode(val = l1.val + l2.val + carry)
                carry = 0

            l1 = l1.next
            l2 = l2.next
            res = res.next

        #res.next = l1 or l2

        while l1:
            if l1.val + carry >= 10:
                res.next = ListNode(val = (l1.val + carry)%10)
                carry = 1
            else:
                res.next = ListNode(val = l1.val + carry)
                carry = 0
            l1 = l1.next
            res = res.next

        while l2:
            if l2.val + carry >= 10:
                res.next = ListNode(val = (l2.val + carry)%10)
                carry = 1
            else:
                res.next = ListNode(val = l2.val + carry)
                carry = 0
            l2 = l2.next
            res = res.next
        
        if carry ==1:
            res.next = ListNode(val = 1)


        return beggining_res.next
        

