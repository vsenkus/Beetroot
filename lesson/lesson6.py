dir(dict)
help(''dict().get)

назва caffe.get
import collection
s.split
help(''.split)
# task2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def get_total_stock_products_price(stock: dict, prices: dict):
    total = 0
    for key, value in stock.items():
        if key in prices:
           total += prices(key, 0) * value
    return total

# task3
[]
