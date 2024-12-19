from fastapi import FastAPI

app = FastAPI()


def read_csv(filepath: str):
    data = []

    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

        for line in lines:
            data.append(line.split(','))

    return data


class Orders:
    def __init__(self, file_path: str, headers: int = 0):
        orders = read_csv(file_path)
        self.headers = orders[0]
        self.data = orders[1:]

    def count_orders_ship_to_germany(self):
        count = 0

        for order in self.data:
            ship_country = order[13]

            if ship_country == 'Germany':
                count += 1

        return count

    def count_orders_by_country(self):
        counts = {}

        for order in self.data:
            ship_country = order[13]

            if ship_country in counts.keys():
                counts[ship_country] += 1
            else:
                counts[ship_country] = 1

        return counts

    def count_orders_by_date(self):
        counts = {}

        for order in self.data:
            order_id = order[0]
            order_date = order[3][:7]

            if order_date in counts.keys():
                counts[order_date] += 1
            else:
                counts[order_date] = 1

        return counts


orders_db = Orders('orders.csv')


@app.get("/")
def read_root():
    return {"success": "ok"}


@app.get("/count-orders-ship-to-germany")
def count_orders_ship_to_germany():
    return {
        'data': orders_db.count_orders_ship_to_germany()
    }


@app.get("/count-orders-by-date")
def count_orders_by_date():
    return orders_db.count_orders_by_date()


@app.get("/count-orders-by-country")
def count_orders_by_date():
    return orders_db.count_orders_by_country()
