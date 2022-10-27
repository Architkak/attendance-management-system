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
