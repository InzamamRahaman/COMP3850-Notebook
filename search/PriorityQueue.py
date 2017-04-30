import heapq

class PriorityQueue(object):

    def __init__(self):
        self.queue = []
        self.item_set = set()

    def push(self, item, score):
        self.item_set.add(item)
        heapq.heappush(self.queue, (score, item))

    def pop(self):
        item = heapq.heappop(self.queue)
        self.item_set.remove(item[1])
        return item[1]

    def __contains__(self, item):
        return item in self.item_set

    def remove(self, item):
        idx = -1
        for i, elem in enumerate(self.queue):
            if elem == item:
                idx = i
        if idx > -1:
            del self.queue[idx]
            self.item_set.remove(item)

    def reorder(self):
        heapq.heapify(self.queue)


    def __str__(self):
        items = (list(map(lambda x: str(x[1]), self.queue)))
        return '{' + ','.join(items) + '}'

    def is_empty(self):
        if len(self.queue) > 0:
            return False
        return True
