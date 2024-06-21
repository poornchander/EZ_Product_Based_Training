"""1221
2325
3120
520
3121

"""













class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end="->")
            t=t.next
    def addfront(self,val):
        t=self.head
        n=node(val)
        if self.head is None:
            self.head=n
        else:
            n.next=t
            self.head=n
    def addend(self,val):
         t=self.head
         n=node(val)
         if self.head is None:
            self.head=n
         else:
            while(t.next!=None):
                t=t.next
            t.next=n
    def pos(self,val,p):
        
        t=self.head
        n=node(val)
        if self.head is None:
            self.head=n
        else:
            for i in range(p-2):
                t=t.next
            n.next=t.next
            t.next=n
    def search(self,val):
        if self.head is None:
            return -1
        temp=self.head
        c=0
        while temp:
            if temp.data==val:
                return c
            temp=temp.next
            c+=1
        return -1
    def middle_node_search(self):
        if self.head is None:
            return -1
        elif self.head.next is None:
            return self.head.data
        prev_temp=None
        slow_temp=self.head
        fast_temp=self.head
        while fast_temp and fast_temp.next:
            prev_temp=slow_temp
            slow_temp=slow_temp.next
            fast_temp=fast_temp.next.next
        if not fast_temp:
            return prev_temp.data,slow_temp.data
        else:
            return slow_temp.data
    def list_length(self):
        if self.head is None:
            return 0
        length=1
        temp=self.head
        while temp and temp.next:
            temp=temp.next.next
            length+=2
        if not temp:
            return length-1
        return length
    def consecutive_length(self):
        if self.head is None:
            return 0
        temp=self.head
        max_len=1
        length=1
        while temp.next:
            if temp.data==temp.next.data-1:
                length+=1
            else:
                if max_len<length:
                    max_len=length
                length=1
            temp=temp.next
        if max_len<length:
            max_len=length
        return max_len








l1=sll()
l1.addfront(6)
l1.addfront(5)
l1.addfront(4)
l1.addfront(3)
l1.addfront(2)
l1.addfront(1)
l1.display()
print()
l1.addend(100)
l1.addend(200)
l1.addend(300)
l1.display()
l1.pos(1000,3)
print()
l1.display()
print()
print(l1.search(400))
print(l1.middle_node_search())
print(l1.list_length())
print(l1.consecutive_length())