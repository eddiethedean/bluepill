from queue import Empty
from typing import Any


class Value:
    def __init__(self, value: Any = Empty) -> None:
        self.value = value