"""
Maximum Frequency Stack
"""

from collections import deque, defaultdict

class FreqStack:
    """
    FreqStack
    """

    def __init__(self):
        """
        __init__
        """

        self.stack = deque()
        self.group = defaultdict(int)
        self.max_val = 0
        self.freq = defaultdict(int)


    def push(self, val: int) -> None:
        """
        push
        """

        self.freq[val] += 1
        f = self.freq[val]
        if not self.group[f]:
            self.group[f] = deque()
        self.group[f].append(val)
        self.max_val = max(self.max_val, f)


    def pop(self) -> int:
        """
        pop
        """

        deleted = self.group[self.max_val].pop()
        self.freq[deleted] -= 1

        if not self.group[self.max_val]:
            self.max_val -= 1

        return deleted


