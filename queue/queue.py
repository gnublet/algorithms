class Queue:
    def __init__(self):
        self.items = []

    # check whether items is empty
    def is_empty(self):
        return self.items == []

    # add element to queue FIFO
    def enqueue(self, item):
        self.items.insert(0, item)

    # remove element from queue FIFO
    def dequeue(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)

def main():
    q = Queue()
    q.enqueue('a')
    q.enqueue(2)
    q.enqueue('cc')
    q.dequeue()
    print(q)

main()