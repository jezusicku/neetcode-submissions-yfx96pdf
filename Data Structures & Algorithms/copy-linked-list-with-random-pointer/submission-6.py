"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldd = {None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            oldd[curr] = copy
            curr=curr.next

        curr=head
        while curr:
            copy=oldd[curr]
            copy.next=oldd[curr.next]
            copy.random=oldd[curr.random]
            curr=curr.next

        return oldd[head]