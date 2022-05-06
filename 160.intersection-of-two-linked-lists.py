



class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        """
        Time complexity : O(m+n)
        Space complexity : O(1)
        """
        if not headA or not headB:
            return None
        pa = headA      
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa 