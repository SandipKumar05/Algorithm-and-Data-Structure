# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cur=dummy= ListNode()
        while list1 and list2:
            print(list1.val,list2.val)
            if list1.val < list2.val:
                cur.next=list1
                cur=list1
                list1=list1.next
            else:
                cur.next=list2
                cur=list2
                list2=list2.next
        if list1:
            cur.next=list1
        else:
            cur.next=list2
        return dummy.next