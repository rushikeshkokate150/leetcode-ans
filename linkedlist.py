class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None #start with empty list
    
    # function to add new node
    def append(self,data):
        new_node=node(data)
        
        if self.head is None:
            self.head=new_node
            return
        
        # else traverse to the end of list
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    
    # function to display
    def display(self):
        current=self.head
        if current is None:
            print("The list is empty")
        while current:
            print(current.data,end="->")
            current=current.next
        print(None)
    
    # Function to delete the head
    def deletehead(self):
        curr=self.head
        self.head=curr.next
    # Function to delete the tail or last node
    def deletetail(self):
        curr=self.head
        while(curr.next.next != None):
            curr=curr.next
        curr.next=None
    # Function to delete the Kth position
    def deletekth(self,k):
        cnt=2
        prev=self.head
        curr=prev.next
        if k==1:
            temp=self.head
            self.head=temp.next
        else:
            while cnt<k:
                curr=curr.next
                prev=prev.next
                cnt+=1
            if(curr!=None):
                prev.next=curr.next
                print(curr.next)##None
    # Function to insert yhe node at head
    def inserttohead(self,data):
        new_node=node(data)
        temp=self.head
        new_node.next=temp
        self.head=new_node
    # Function to insert the node at last
    def inserttotail(self,data):
        new_node=node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
    # function to insert the node at kth position
    def inserttokth(self,data,k):
        cnt=2
        new_node=node(data)
        prev=self.head
        curr=prev.next
        if k==1:
            temp=self.head
            new_node.next=temp
            self.head=new_node
        while cnt<k:
            curr=curr.next
            prev=prev.next
            cnt+=1
        prev.next=new_node
        new_node.next=curr
    # funtion to reverse the list using stack
    def rev(self,head):
        stack=[]
        temp=head
        while(temp!=None):
            stack.append(temp.data)
            temp=temp.next
        temp=self.head
        while(temp!=None):
            d1=stack.pop()
            temp.data=d1
            temp=temp.next
    # function to put each node in dictionary
    def toput(self):
        a={}
        cnt=1
        temp=self.head
        while(temp!=None):
            if temp in a.keys():
                ans=a[temp]-cnt
                print(ans)
                break
            a[temp]=cnt
            cnt+=1
            temp=temp.next
        print("Not present")
        print(a)
    # funtion to mid positioin
    def midoflist(self):
            slow=self.head
            fast=self.head
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
            return slow
    def sorto12(self):
        cnt0=0
        cnt1=0
        cnt2=0
        temp=self.head
        while temp:
            if temp.data==0:
                cnt0+=1
            elif temp.data==1:
                cnt1+=1
            else:
                cnt2+=1
            temp=temp.next
        temp=self.head
        while temp:
            if cnt0!=0:
                temp.data=0
                cnt0-=1
            elif cnt1!=0:
                temp.data=1
                cnt1-=1
            else:
                temp.data=2
                cnt2-=1
            temp=temp.next 
        
l1=linkedlist()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.append(60)
l1.display()
l1.deletekth(3)
