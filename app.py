from fastapi import FastAPI
from dataframe import DataFrame

app = FastAPI()
df = DataFrame.read_csv('orders.csv')


@app.get("/")
def read_root():
    return {"success": "ok"}


@app.get("/count-orders-by-date")
def count_orders_by_date():
    group_by_date = df.group_by_count('OrderDate')
    group_by_month = {}

    for date, count in group_by_date.items():
        # date looks like 1960-08-10 10:00:00
        yyyymm = date[:7] 
        
        if yyyymm in group_by_month.keys():
            group_by_month[yyyymm] = group_by_month[yyyymm] + 1
        else:
            group_by_month[yyyymm] = 1

    return group_by_month


@app.get("/count-orders-by-country")
def count_orders_by_date():
    return df.group_by_count('ShipCountry')
