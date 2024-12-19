

class DataFrame:
    def __init__(self, data: list[list[str]], headers: int = 0, columns: list[str] = None):
        self.rows = data[1:]
        headers_index = {}
        if columns is not None:
          self.columns = columns
        else:
          self.columns = data[headers]
        self.indexes = range(len(self.rows))
        self.key_values = {}
        self.current = 0

        for i, header in enumerate(self.columns):
            self.key_values[header] = []
            headers_index[i] = header

        for row in self.rows:
            for i, col in enumerate(row):
                self.key_values[headers_index[i]].append(col)

    def __repr__(self) -> str:
        s = '\t'.join(self.columns) + '\n'

        for row in self.rows[:6]:
          s += '\t'.join(row) + '\n'

        return s

    def __getitem__(self, key: str) -> list[str]:
        if key in self.columns:
            return self.key_values[key]

        raise KeyError(f"Invalid key {key}")

    def __str__(self) -> str:
        return f'DataFrame({len(self.rows)}, {len(self.columns)})'

    def __eq__(self, other) -> bool:
        for i, row in enumerate(self.rows):
          for j, col in enumerate(row):
            if col != other[i][j]:
              return False
        return True

    def __len__(self) -> int:
        return len(self.indexes)

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.indexes), len(self.columns))

    def head(self, n: int = 6):
        return DataFrame(data=self.rows[:n], columns=self.columns)

    def tail(self, n: int = 6):
        return DataFrame(data=self.rows[:-(n + 1):-1], columns=self.columns)

    def group_by_count(self, key: str) -> dict:
        counts = {}

        for item in self.key_values[key]:
            if item in counts.keys():
                counts[item] += 1
            else:
                counts[item] = 1
        return counts

    def __iter__(self):
        return self

    def iterrows(self):
        #for index, rows in zip(self.indexes, self.rows):
        #  yield index, rows
        return enumerate(self.rows)

    def __next__(self):
        if self.current >= len(self.rows):
          raise StopIteration

        current_value = self.rows[self.current]
        self.current += 1
        return current_value

    def sum(self, key: str) -> float:
        return round(sum(map(float, self.key_values[key])), 2)

    def mean(self, key: str) -> float:
        return round(self.sum(key) / self.shape[0], 2)

    def median(self, key: str) -> float:
        sorted_arr = sorted(map(float, df.key_values[key]))
        return sorted_arr[int(len(sorted_arr) / 2)]

    def to_csv(self, filename: str, delimeter: str = ','):
        with open(filename, 'w') as f:
          f.write(','.join(self.columns) + '\n')
          for row in self.rows:
            f.write(','.join(row) + '\n')
        print(f"Successfully saved to {filename}")

    @staticmethod
    def read_csv(filepath: str, delimiter: str = ',', headers: int = 0):
        data = []

        with open(filepath, 'r') as f:
            lines = f.read().splitlines()

            for line in lines:
                data.append(line.split(delimiter))

        df = DataFrame(data, headers=headers)
        print(f"Finshed reading orders.csv. Shape: {df.shape}")
        return df


if __name__ == '__main__':
    df = DataFrame.read_csv('orders.csv')
    print(df.group_by_count('ShipCountry'))

