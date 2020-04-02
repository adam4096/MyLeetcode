# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
 
        last = 0 # 表示进位
        prev = head =None #两个指针
        while True:
            if not l1 and not l2 and last == 0:
                break #空表或执行结束跳出
            # 两数相加
            val = last #别漏了，进位需要加上
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val 
                l2 = l2.next
            # 处理进位
            if  val >= 10:
                val = val % 10 
                last = 1  
            else:
                last = 0    
            current = ListNode(val)
            # 插入结点
            if prev is None:
                head = current
            else:
                prev.next = current
            prev = current
        return head
    

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
