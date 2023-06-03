# Your solutions to questions from part 3 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.

import numpy as np
from typing import Any, Iterator

class ArrayList:
    def __init__(self):
        self.data = np.empty(1, dtype=object)
        self.size = 0

    def append(self, value: Any) -> None:
        if self.size == len(self.data):
            ndata = np.empty(2 * len(self.data), dtype=object)
            for i in range(len(self.data)):
                ndata[i] = self.data[i]
            self.data = ndata
        self.data[self.size] = value
        self.size += 1

    def __iter__(self) -> Iterator[Any]:
        for i in range(self.size):
            yield self.data[i]

    def __len__(self) -> int:
        return self.size

    def foo(self, value: Any) -> int:
        raise NotImplementedError
