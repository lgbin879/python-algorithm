class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)

# if __name__ == "__main__":
#     q = Queue()
#     q.enqueue("hello")
#     q.enqueue("world")
#     q.enqueue("itcast")
#     print q.size()
#     print q.dequeue()
#     print q.dequeue()
#     print q.dequeue()

class Deque(object):
    """双端队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def add_front(self, item):
        """在队头添加元素"""
        self.items.insert(0,item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.items.append(item)

    def remove_front(self):
        """从队头删除元素"""
        return self.items.pop(0)

    def remove_rear(self):
        """从队尾删除元素"""
        return self.items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.items)


if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print deque.size()
    print deque.remove_front()
    print deque.remove_front()
    print deque.remove_rear()
    print deque.remove_rear()