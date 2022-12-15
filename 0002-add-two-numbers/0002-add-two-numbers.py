# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def getNumOfLinkedList(self, l):
        num = ""
        while l.next:
            num += str(l.val)
            l = l.next
        num += str(l.val)
        return int(num[::-1])

    def reversedResultatLinkedList(self, numStr):
        restL = ListNode(val=numStr[0], next=None)
        for num in numStr[1:]:
            node = ListNode(val= int(num), next = restL)
            restL= node
        return restL

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest = self.getNumOfLinkedList(l1) + self.getNumOfLinkedList(l2)
        return self.reversedResultatLinkedList(str(rest))
        