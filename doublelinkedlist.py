class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class linkedlist:
    def __init__(self):
        self.head=None
    
    # function the add new node
    def append(self,data):
        new_node=node(data)
        
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    # function to display
    def display(self):
        current=self.head
        if current is None:
            print("The list is empty")
        while current:
            print(current.data,end="<=>")
            current=current.next
        print(None)
    # function to traverse from back
    def displayr(self):
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        while curr.prev!=None:
            print(curr.data,end="<=>")
            curr=curr.prev
        print(None)
    #  function to insert into the list
    def inserthead(self,data):
        new_node=node(data)
        temp=self.head
        new_node.next=temp
        self.head=new_node
    #  funtion to insert into the kth position
    def inserttokth(self,data,k):
        new_node=node(data)
        if k==1:
            temp=self.head
            new_node.next=temp
            self.head=new_node
        else:
            cnt=2
            prev1=self.head
            curr=self.head.next
            while cnt<k:
                prev1=prev1.next
                curr=curr.next
                cnt+=1
            new_node.next=curr
            curr.prev=new_node
            new_node.prev=prev1
            prev1.next=new_node
    # funtion to delete the head of the linkedlist
    def deletethehead(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
    
    # function to delete the kth position
    def deletethekth(self,k):
        if k==1:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.head.prev=None
        else:
            cnt=2
            prev1=self.head
            curr=prev1.next
            while cnt<k:
                prev1=prev1.next
                curr=curr.next
                cnt+=1
            prev1.next=curr.next
            curr.next.prev=prev1
            curr.next=curr.prev=None
            print(curr.data, curr.next,curr.prev)
    # funtion to reverse the doubliy linked list using two traverse
    def revs(self):
        stack=[]
        curr=self.head
        while curr:
            stack.append(curr.data)
            curr=curr.next
        print(stack)
        curr=self.head
        while curr:
            d1=stack.pop()
            print(d1)
            curr.data=d1
            curr=curr.next
    # function to reverse the doubly linked list single traverse
    def revss(self):
        curr=self.head
        print(curr.data)
        while curr!=None:
            last=curr.prev
            print(last)
            curr.prev=curr.next
            curr.next=last
            curr=curr.prev
        self.head=last.prev
    # funtion to find the mid
    def midoflist(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
    # funtion to find the tail
    def tail(self):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        return temp
    # function to find the sum of pair matching target
    def findsumpair(self,target):
        arr=[]
        left=self.head
        right=self.tail()
        while(left.data<right.data):
            if(left.data+right.data==target):
                arr.append([left.data,right.data])
                left=left.next
                right=right.next
            elif(left.data+right.data>target):
                right=right.prev
            else:
                left=left.next
        print(arr)
    # funtion to remove the dupicate from sorted DL
    def removetheduplicates(self):
        temp = self.head
        while temp is not None:
            curr = temp.next
            if curr is not None and temp.data == curr.data:
                temp.next = curr.next
                if curr.next is not None:
                    curr.next.prev = temp
                # Disconnect the current node
                curr.next = None
                curr.prev = None
            else:
                temp = temp.next

        
                

l1=linkedlist()
l1.append(1)
l1.append(1)
l1.append(1)
l1.append(2)
l1.append(2)
l1.append(3)
l1.display()
# l1.inserttokth(100,1)
# l1.display()
# l1.deletethekth(3)
# l1.display()
# l1.revss()
# l1.display()
# print(l1.head.data)
# l1.midoflist()
# l1.findsumpair(5)
l1.removetheduplicates()
l1.display()
