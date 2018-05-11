class stack():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop(-1)

    def peek(self):
        return self.items[-1]


# s = stack()
# print (s.items)
#
# s.push(1)
# s.push(2)
# s.push(5)
#
# print (s.items)
#
# s.pop()
# print(s.items)
#
# print(s.peek())