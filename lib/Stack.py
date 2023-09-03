class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i, item in enumerate(reversed(self.items)):
            if item == target:
                return i + 1  # 1-based index from the top of the stack
        return -1  # Element not found


# Test cases for Stack class
def test_stack_methods():
    stack = Stack(limit=5)
    assert stack.isEmpty() == True
    assert stack.full() == False
    assert stack.size() == 0

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.isEmpty() == False
    assert stack.full() == True
    assert stack.size() == 5

    assert stack.pop() == 5
    assert stack.size() == 4
    assert stack.peek() == 4

    assert stack.search(3) == 2
    assert stack.search(6) == -1

if __name__ == "__main__":
    test_stack_methods()
    print("All test cases passed.")
