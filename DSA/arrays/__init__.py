class Array:
    def __init__(self):
        self.array = []
        self.length = 0

    def insert(self, item):
        self.array += [None]
        self.array[self.length] = item
        self.length += 1

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            return "Index out of bounds"
        removed_item = self.array[index]
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1
        self.array = self.array[:self.length]
        return removed_item

    def get(self, index):
        if index < 0 or index >= self.length:
            return "Index out of bounds"
        return self.array[index]

    def index_of(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def print_array(self):
        print(f"Array: {self.array[:self.length]}")


arr = Array()
arr.insert(10)
arr.insert(20)
arr.insert(30)
arr.print_array()

print(arr.get(1))
print(arr.remove_at(1))
arr.print_array()

print(arr.index_of(30))
print(arr.size())
print(arr.is_empty())