def search_element(numbers: list[int], target: int) -> int:
    for index, num in enumerate(numbers):
        if num == target:
            return index
    return TypeError
