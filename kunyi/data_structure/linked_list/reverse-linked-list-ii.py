class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # get the m_node and m_prev 
        # head -> node 
        if head is None:
            return 
        m_prev, m_node = None, head
        for i in range(m-1):
            if m_prev is None:
                m_prev = m_node
            else:
                m_prev = m_prev.next 
            m_node = m_node.next
            
        cur, last = m_node, None 
        for i in range(n - m + 1):
            cur_next = cur.next 
            cur.next= last 
            cur, last = cur_next, cur 
        
        #  m_prev --   last -- m_node 
        m_node.next = cur     
        if m_prev:
            m_prev.next = last 
            return head 
        
        return last 
        
        
################## dummy node ##############
class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def findk(self, head, k):
        for i in range(k):
            if head is None:
                return None
            head = head.next
        return head
        
    def reverse(self, head):
        prev, curr = None, head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    
    def reverseBetween(self, head, m, n):
        # write your code here
        # keep track for the node in m index, and n index
        # reverse the m -n list
        # connect again, mth_prev.next = nth, mth.next = nth_next
        if head is None:
            return
        dummy = ListNode(-1, head)
        # n th
        mth_prev = self.findk(dummy, m-1) # 1 node
        mth = mth_prev.next # 2 node
        nth = self.findk(dummy, n)
        nth_next = nth.next
        nth.next = None  # extract one sub linked list
        
        mth_prev.next = self.reverse(mth)
        mth.next = nth_next
        return dummy.next
