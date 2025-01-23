class set_function:
    def __init__(self):
        self._items = {}
        self._size = 0

    def set_items(self, items):
        self._items = items
        self._size += len(items)
        return self._items

    def get_items(self):
        return self._items

    def set_size(self, size):
        self._size = size
        return self._size

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def add(self, name):
        self._items.add(name)
        return self._size







