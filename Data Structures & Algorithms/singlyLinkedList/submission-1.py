class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
class LinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None

    
    def get(self, index: int) -> int:
        temp = self.head
        count = 0 
        while (temp != None):
            if count == index:
                return temp.val
            temp = temp.next
            count += 1
        return -1


        

    def insertHead(self, val: int) -> None:
        temp = ListNode(val)
        if self.head==None:
            self.head=temp
            self.tail=temp
        else:
            temp.next = self.head
            self.head = temp
        

    def insertTail(self, val: int) -> None:
        temp=ListNode(val)
        if self.tail == None:
            self.head=temp
            self.tail=temp
        else:
            self.tail.next = temp
            self.tail = temp
        

    def remove(self, index: int) -> bool:
        temp = self.head
        prev = None
        count = 0
        while (temp != None):
            if count == index:
                if prev == None:
                    self.head = temp.next
                    if self.head == None:
                        self.tail = None
                else:
                    prev.next = temp.next
                    if temp.next == None:
                        self.tail = prev
                return True
            prev = temp
            temp = temp.next
            count += 1
        return False

        

    def getValues(self) -> List[int]:
        a =[]
        temp = self.head
        while(temp != None):
            a.append(temp.val)
            temp = temp.next
        return a