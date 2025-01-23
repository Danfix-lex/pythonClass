class list_function:
    def __init__(self):
        self._items = []
        self._size = 0

    def is_empty(self):
        return len(self._items) == 0

    def is_not_empty(self):
        return len(self._items) > 0

    def size(self):
        return len(self._items)

    def add(self, element):
        self._items.append(element)
        self._size += 1

    def remove(self, element):
        if element in self._items:
            self._items.remove(element)
            self._size -= 1

    def index(self, element):
        return self._items.index(element) if element in self._items else -1