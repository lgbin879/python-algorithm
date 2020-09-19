

class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item=None):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self._head = node


    def is_empty(self): 
        """链表是否为空"""
        return self._head == None


    def length(self):
        """链表长度"""
        length = 0
        curr = self._head
        while curr != None:
            length += 1
            curr = curr.next

        return length
            

    def travel(self):
        """遍历整个链表"""
        curr = self._head
        while curr != None:
            print(curr.item, end=' ')
            curr = curr.next
        print()


    def add(self, item): 
        """链表头部添加元素"""
        node = SingleNode(item)
        node.next, self._head = self._head, node


    def append(self, item): 
        """链表尾部添加元素"""
        node = SingleNode(item)

        curr = self._head
        if self.is_empty():
            self._head = node
        else:
            while curr.next != None:
                curr = curr.next
            curr.next = node

    def insert(self, pos, item): 
        """指定位置添加元素"""
        node = SingleNode(item)

        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            i = 0
            pre = self._head
            while i < pos-1:
                i += 1
                pre = pre.next

            pre.next, node.next = node, pre.next


    def search(self, item): 
        """查找节点是否存在"""
        curr = self._head
        pos = 0
        while curr != None:
            if curr.item == item:
                print("{0} found in pos-{1}".format(item, pos))
                return pos
            else:
                curr = curr.next
                pos += 1

        print("{0} not found".format(item))
        return -1


    def remove(self, item): 
        """删除节点"""
        if self._head == None:
            return False

        if self._head.item == item:
            self._head = self._head.next
            return True

        pre = self._head
        curr = pre.next

        while curr != None:
            if curr.item == item:
                pre.next = curr.next
                del(curr)
                return True
            else:
                pre, curr = curr, curr.next

        print("{0} not found in list".format(item))
        return False

    def removeNthFromEnd(self, n):
        end = self._head;
        i = 0
        while i < n-1:
            end = end.next
            i += 1

        pre = None
        curr = self._head
        while end.next != None:
            pre, curr, end = curr, curr.next, end.next

        if pre == None: # remove head
                self._head = curr.next
        else:
            pre.next = curr.next

        return self._head

    def reverseList(self):
        """单链表反转，需要双指针和一个临时指针"""
        if self._head is None or self._head.next is None:
            return self._head

        pre = None
        cur = self._head

        while cur:
            rear = cur.next
            cur.next = pre
            pre, cur = cur, rear
            #print(pre.item, cur.item)

        self._head = pre
        return self._head


if __name__ == "__main__":
    l = SingleLinkList()
    # print(l.length())
    # l.travel()

    l.append(0)
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)

    # print(l.length())
    l.travel()

    l.reverseList()
    l.travel()

    # l.add(9)
    # l.travel()

    # l.insert(5, 8)
    # l.travel()

    # l.search(3)
    # l.search(99)

    l.removeNthFromEnd(2)
    l.travel()



