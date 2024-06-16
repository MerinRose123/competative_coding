"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""
"""
Trick : Iterate and reverse each k node set
"""
class Solution:
    def reverseLinkedList(self, head, k):
        prev_node, current = None, head
        while k:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
            k -= 1
        new_head = prev_node
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        current = head
        ktail = None
        prev_node = None
        while current:
            count = 0
            current = head
            while count < k and current:
                current = current.next
                count += 1
            if count == k:
                revHead = self.reverseLinkedList(head, k)
                if not prev_node:
                    prev_node = revHead
                  
                if ktail:
                    ktail.next = revHead

                ktail = head
                head = current

        if ktail:
            ktail.next = head
          
        new_head = prev_node
        return new_head if new_head else head
