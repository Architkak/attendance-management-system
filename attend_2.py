class Stack_Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def Append(self,a):
        self.items.insert(0,a)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop(0)
    def Clean(self):
        self.items.clear()

def inp(x):
    if(x==1):
        n=int(input("\n Enter the value to be appended: "))
        return n
    
    elif(x==2):
        a=int(input("\n Enter the value to be inserted: "))
        return a
    elif(x==3):
        b=int(input("\n Enter the index at which insertion is to be performed: "))
        return b

s=Stack_Queue()
value=True
while(value):
    i=0
    s.Clean()
