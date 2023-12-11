class Queue:
    """
    Queue data structure using list
    """
    def __init__(self,value):
        """
        Class initializer: Produces a queue with a single value or a list of values
        """
        self._items = []
        if type(value)==list:
            for v in value:
                self._items.append(v)
            self._length = len(value)
        else:
            self._items.append(value)
            self._length = 1
        
    def dequeue(self):
        if self._length == 0:
            print ("Queue is empty. Nothing to dequeue.")
            return None
        else:
            self._length -=1
            return self._items.pop(0)
    
    def enqueue(self,value):
        self._length +=1
        self._items.append(value)
        
    def isEmpty(self):
        return self._length==0
    
    def draw(self):
        if self.isEmpty():
            print('Empty queue')
            pass
            return None
        else:
            n=self._length
            for i in range(n-1):
                print('['+str(self._items[i])+']-',end='')
            print('['+str(self._items[n-1])+']')


q = Queue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.draw()
q.dequeue()
q.draw()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.draw()








            

