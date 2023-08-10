

from collections import deque # deque is a double ended queue it optimizes for insertions and deletions


class Queue:
    def __init__(self):
        self.items = deque() # constructor we are creating a dequeue
    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)
    

if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty()) # should return true because we havent enqueue nothing yet
    q.enqueue("A")
    q.enqueue("K")
    q.enqueue(1)
    q.enqueue(200)
    print(q)
    print(q.dequeue()) # removing A
    print(q.dequeue()) # removing K
    print(q) # This is left with 1 and 200 because we took A and K out the queue
    print(q.size()) # this will return 2 in the queue
    print(q.peek()) # this will show us what is at the head of the queue which is 1
