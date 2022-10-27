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
    yn=int(input("\nIf u want to continue or exit?\n1-Continue\n2-Exit\n==>"))
    if(yn==1):
        print("Enter the Marks of the sudents:")
        while i<10:
            a=int(input("==>"))
            s.Append(a)
            i+=1
        print("The marks have been successfully entered into the list!\n Now You may")
        what=int(input("\nSelect\n1-Stack out \n2-Queue out\n->"))
        if(what==1):
            j=0
            while j<10:
                a=s.pop()
                print("Output in Stack No {} is : {}".format(j+1,a))
                j+=1
        elif(what==2):
            k=0
            while k<10:
                a=s.dequeue()
                print("Output in Queue NO {} is : {} ".format(k+1,a))
                k+=1
        else:
            print("Enter a Valid Input")
    elif(yn==2):
        value=False
        print("Arigato Gozaimus")
