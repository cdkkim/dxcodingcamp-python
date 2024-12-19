from multipart import file_path


class DataFrame:
    def __init__(self, filepath: str, headers: int = 0):
        self.data = self._read_csv(file_path)

    def _read_csv(self, filepath: str):
        data = []

        with open(filepath, 'r') as f:
            lines = f.read().splitlines()

            for line in lines:
                data.append(line.split(','))

        return data

    @staticmethod
    def read_csv(filepath: str):
        data = []

        with open(filepath, 'r') as f:
            lines = f.read().splitlines()

            for line in lines:
                data.append(line.split(','))

        return DataFrame(data)

