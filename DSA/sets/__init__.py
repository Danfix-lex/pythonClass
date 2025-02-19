class Set:
    def __init__(self):
        self.elements = []

    def add(self, item):
        if not self.contains(item):
            self.elements += [item]

    def remove(self, item):
        if self.contains(item):
            new_elements = []
            for element in self.elements:
                if element != item:
                    new_elements += [element]
            self.elements = new_elements
        else:
            raise ValueError(f"{item} not found in the set")

    def contains(self, item):
        for element in self.elements:
            if element == item:
                return True
        return False

    def size(self):
        count = 0
        for _ in self.elements:
            count += 1
        return count

    def is_empty(self):
        return self.size() == 0

    def union(self, other_set):
        result = Set()
        for element in self.elements:
            result.add(element)
        for element in other_set.elements:
            result.add(element)
        return result

    def intersection(self, other_set):
        result = Set()
        for element in self.elements:
            if other_set.contains(element):
                result.add(element)
        return result

    def difference(self, other_set):
        result = Set()
        for element in self.elements:
            if not other_set.contains(element):
                result.add(element)
        return result

    def __str__(self):
        return "{" + ", ".join(str(element) for element in self.elements) + "}"