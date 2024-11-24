class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def insert_row(self, row_index, row):
        if len(row) != self.cols:
            raise ValueError("Row length must match matrix columns")
        self.data.insert(row_index, row)
        self.rows += 1

    def delete_row(self, row_index):
        del self.data[row_index]
        self.rows -= 1

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
