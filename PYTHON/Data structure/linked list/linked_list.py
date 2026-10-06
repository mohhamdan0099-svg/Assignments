class Node:
    def __init__(self, data):
        self.data = data
        self.next = None





class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_to_start(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self
                        
        new_node.next=self.head
        self.head = new_node
        return self

    def add_to_tail(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head = new_node
            return self
                    
        current=self.head
        while current.next!=None:
            current=current.next
        current.next= new_node
        return self

    def add_after(self,value):
        pass

    def add_to_middle(self,value):
        pass



    def delete_node(self,value):

        if self.head.value==value:
            self.head=self.head.next

        curr=self.head
        while curr:
            if curr.next.value==value:
                break
            curr=curr.next
            curr.next=curr.next.next    











        
                
                
        
            
