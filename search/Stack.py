

class Stack(object):

    def __init__(self):
        self.contents = []
        self.content_set = set()
        self.n = 0

    def push(self, elem):
        self.contents.append(elem)
        self.content_set.add(elem)
        self.n += 1

    def pop(self):
        elem = self.contents.pop()
        self.n -= 1
        self.content_set.remove(elem)
        return elem

    def is_empty(self):
        return self.n == 0

    def __len__(self):
        return len(self.contents)

    def __contains__(self, item):
        return item in self.content_set


    def __str__(self):
        temp = map(str, reversed(self.contents))
        return ','.join(temp)

    def __repr__(self):
        return str(self)
