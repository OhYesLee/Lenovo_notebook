class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self, item):
        self.list.append(item)
    def dequeue(self):
        return self.list.pop(0)
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())