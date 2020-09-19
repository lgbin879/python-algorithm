

class DualNode(object):
    """单链表的结点"""
    def __init__(self,item=None):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.prev = None
        self.next = None

class DLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self._head = node
        if node:
            node.prev = None
            node.next = None


    def is_empty(self): 
        """链表是否为空"""
        return self._head == None


    def length(self):
        """链表长度"""
        curr = self._head
        if curr == None:
            return 0

        length = 1
        while curr.next != self._head:
            length += 1
            curr = curr.next

        return length
            

    def travel(self):
        """遍历整个链表"""
        curr = self._head
        if curr == None:
            return 0

        while curr.next != self._head:
            print(curr.item, end=' ')
            curr = curr.next

        print(curr.item)


    def add(self, item): 
        """链表头部添加元素"""
        node = DualNode(item)
        end = self._head

        if end == None:
            node.prev = None
            node.next = node
            self._head = node
        else:
            while end.next != self._head:
                end = end.next
            end.next, node.next, self._head = node, self._head, node


    def append(self, item): 
        """链表尾部添加元素"""
        node = DualNode(item)

        end = self._head
        if end == None:
            self._head = node
            node.next = node
        else:
            while end.next != self._head:
                end = end.next
            end.next, node.next = node, self._head


    def insert(self, pos, item): 
        """指定位置添加元素"""
        node = DualNode(item)

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
        if curr == None:
            return -1

        pos = 0
        while curr.next != self._head:
            if curr.item == item:
                print("{0} found in pos-{1}".format(item, pos))
                return pos
            else:
                curr = curr.next
                pos += 1

        if curr.item == item:
            print("{0} found in pos-{1}".format(item, pos))
            return pos
            
        print("{0} not found".format(item))
        return -1


    def remove(self, item): 
        """删除节点"""
        if self._head == None:
            return False

        if self._head.item == item:
            end = self._head
            while end.next != self._head:
                end = end.next

            self._head = self._head.next
            end.next = self._head
            return True

        pre = self._head
        curr = pre.next

        while curr.next != self._head:
            if curr.item == item:
                pre.next = curr.next
                return True
            else:
                pre, curr = curr, curr.next

        if curr.item == item:
            pre.next = curr.next
            return True
        else:
            print("{0} not found in list".format(item))
            return False



if __name__ == "__main__":
    l = DLinkList()
    print(l.length())
    l.travel()

    l.append(0)
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)

    print(l.length())
    l.travel()

    l.add(9)
    l.append(7)
    l.travel()

    l.insert(5, 8)
    l.travel()

    l.search(3)
    l.search(99)

    l.remove(8)
    l.travel()

    #l.removeNthFromEnd(2)
    #l.travel()



