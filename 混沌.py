class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def circle(k,nameList):
    queue1=Queue()
    for i in range(len(nameList)):  #将名字列表逐个插入队列
        queue1.enqueue(nameList[i])
    i=1
    while queue1.size()!=1:
        temp=queue1.dequeue()       #叫到哪个将哪个弹出
        if i!=k:
            queue1.enqueue(temp)    #不是第k个再插入
        else :
            i=0                     #是第k个重新计数
        i+=1
    return queue1.dequeue()
#主函数
if __name__=='__main__':
    nameList=["Bill","David","Susan","Jane","Kent","Brad"]
    print(circle(7,nameList))

