class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        result = head
        remainder = 0
        while l1 != None or l2 != None:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next;
            if l2 != None:
                sum += l2.val
                l2 = l2.next;
            sum += remainder
            if result == None:
                head = ListNode(sum % 10, None)
                result = head
            else:
                result.next = ListNode(sum % 10, None)
                result = result.next;
            remainder = int(sum / 10)
        if remainder > 0:
            result.next = ListNode(remainder, None)
        return head
