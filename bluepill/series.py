from typing import Any, Sequence

from bluepill.empty import Empty
from bluepill.value import Value


class Series:
    def __init__(self, size: int, index: int) -> None:
        self.index = index
        self._values = [Value() for _ in range(size)]

    def __setitem__(self, index: int, value: Any) -> None:
        self._values[index].value = value

    def __getitem__(self, index: int) -> Any:
        return self._values[index].value
    
    def __delitem__(self, index: int) -> None:
        self[index] = Empty
    
    def __len__(self) -> int:
        return len(self._values)
    
    def __iter__(self) -> Any:
        return iter(self._values)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.values})'
    
    @property
    def values(self) -> list:
        return [slot.value for slot in self._values]
    
    @values.setter
    def values(self, values: Sequence) -> None:
        if len(self) != len(values):
            raise ValueError('Length of values must match length of series')
        for slot, value in zip(self._values, values):
            slot.value = value

    def clear(self) -> None:
        self._values = [Value() for _ in range(len(self))]