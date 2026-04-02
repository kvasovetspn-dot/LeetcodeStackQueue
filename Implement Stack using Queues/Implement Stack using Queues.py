"""
Implement Stack using Queues
"""

class MyStack:
    """
    MyStack
    """

    def __init__(self):
        """
        __init__
        """

        self.stack = []

    def push(self, x: int) -> None:
        """
        push
        """

        self.stack.append(x)


    def pop(self) -> int:
        """
        pop
        """

        length = len(self.stack)
        for _ in range(length - 1):
            self.stack.append(self.stack.pop(0))
        return self.stack.pop(0)


    def top(self) -> int:
        """
        top
        """

        length = len(self.stack)
        for _ in range(length - 1):
            self.stack.append(self.stack.pop(0))
        first = self.stack.pop(0)
        self.stack.append(first)
        return first


    def empty(self) -> bool:
        """
        empty
        """

        return not bool(len(self.stack))


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
