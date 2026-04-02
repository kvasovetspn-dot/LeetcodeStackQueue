"""
Implement Queue using Stacks
"""

class MyQueue:
    """
    MyQueue
    """

    def __init__(self):
        """
        __init__
        """

        self.queue = []

    def push(self, x: int) -> None:
        """
        push
        """

        self.queue.append(x)

    def pop(self) -> int:
        """
        pop
        """

        length = len(self.queue)
        new = []
        for _ in range(length - 1):
            new.append(self.queue.pop())
        deleted = self.queue.pop()
        for _ in range(length - 1):
            self.queue.append(new.pop())
        return deleted

    def peek(self) -> int:
        """
        peek
        """

        length = len(self.queue)
        new = []
        for _ in range(length - 1):
            new.append(self.queue.pop())
        first = self.queue.pop()
        new.append(first)
        for _ in range(length):
            self.queue.append(new.pop())
        return first

    def empty(self) -> bool:
        """
        empty
        """

        return not bool(len(self.queue))

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
