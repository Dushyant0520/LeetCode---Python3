


#==================================================================
#Name       : Odd_Even_Linked_List.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================


class ListNode:
 def __init__(self, val=0, next=None):
     self.val = val
     self.next = next

class Solution:

    def oddEvenList(self, head):
        for_odd = ListNode(0)
        for_even = ListNode(0)
        odd_Head = for_odd
        even_Head = for_even
        isodd = True
        while head:
            if isodd:
                for_odd.next = head
                for_odd = for_odd.next
            else:
                for_even.next = head
                for_even = for_even.next

            isodd = not isodd
            head = head.next
        for_even.next = None
        for_odd.next = even_Head.next
        #return odd_Head.next

        #For printing output
        temp = self.head
        while (temp):
            print temp.val
            temp = temp.next

        #print(odd_Head.val)

#For printing the input in "main"
"""
    def printList(self):
        temp = self.head
        while (temp):
            print temp.val
            temp = temp.next
"""


if __name__=='__main__':
    # Start with the empty list
    #First create an instance of the Class
    llist = Solution()

    llist.head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    four = ListNode(4)
    five = ListNode (5)

    llist.head.next = second # Link first node with second
    second.next = third # Link second node with the third node
    third.next = four
    four.next = five

    #For running the logic of oddEvenList and printing output - call the method oddEvenList
    llist.oddEvenList(llist.head)

    #For printing input - call the method "printList"
    #llist.printList()


"""
Youtube Code for def OddEvenList method only
Runtime: 40 ms
Memory Usage: 15.7 MB
"""
