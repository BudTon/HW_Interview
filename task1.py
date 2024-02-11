class Stack :

    def __init__(self):
        self.items = []

    def is_empty(self):
        return (self.items == [])
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if s.size() == 0:
            return None
        item = self.items[-1]
        return item

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(33)
    s.push(333)
    s.push(3333)
    s.push(33333)
    s.push(333333)

    revers = []

    while not s.is_empty():
        print(s.items)
        revers.append(s.peek())
        print(s.pop(),' - pop')
        print(s.size(),'- size')
        print(s.peek(),'- peek')
    print(s.is_empty())
    print(revers)