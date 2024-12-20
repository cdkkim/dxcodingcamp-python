import pdb


class DataFrame:
    def __init__(self, rows: list[list[str]], headers: int = 0):
        self.data = {}
        headers_index = {}
        self.columns = rows[0]

        for i, header in enumerate(self.columns):
            self.data[header] = []
            headers_index[i] = header

        for row in rows[1:]:
            for i, col in enumerate(row):
                self.data[headers_index[i]].append(col)

    def __repr__(self):
        return f'DataFrame({len(self.data)}, {len(self.columns)})'

    def __getitem__(self, key: str):
        if key in self.data.keys():
            return self.data[key]

        raise KeyError(f"Invalid key {key}")

    def __str__(self):
        return f'DataFrame({len(self.data)})'

    def __eq__(self, other):
        return len(self.data) == len(other) and len(self.columns) and len(other.columns)

    def __len__(self):
        return len(self.data.keys())

    def size(self):
        return (len(self.data.keys()), len(self.columns))

    def add_row(self):
        pass

    def add_column(self):
        pass

    def __iter__():
        pass

    def __next__():
        pass

    def iter_rows(self):
        pass

    def group_by_count(self, key: str):
        counts = {}

        for item in self.data[key]:
            if item in counts.keys():
                counts[item] += 1
            else:
                counts[item] = 1
        return counts

    @staticmethod
    def read_csv(filepath: str, delimiter: str = ',', headers: int = 0):
        data = []

        with open(filepath, 'r') as f:
            lines = f.read().splitlines()

            for line in lines:
                data.append(line.split(delimiter))

        return DataFrame(data, headers=headers)


df = DataFrame.read_csv('orders.csv')
df.group_by_count('ShipCountry')
pdb.set_trace()
