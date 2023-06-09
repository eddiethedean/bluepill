from typing import List, Sequence, Tuple

from bluepill.column import Column
from bluepill.row import Row


class Matrix:
    def __init__(self, shape: Tuple[int, int]) -> None:
        self.columns = [Column(shape[0], index) for index in range(shape[1])]
        self.rows = rows_from_columns(self.columns)


def rows_from_columns(columns: Sequence[Column]) -> List[Row]:
    """
    Using the Values objects from the columns, create a list of Rows.
    This allows us to access the same values in the rows as we do in the columns.
    """
    ...