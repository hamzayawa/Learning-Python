import csv

order_amounts = []

with open('orders.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        order_amounts.append(float(row[2]))

# Get every other order amount starting from the second order
every_other_order_amount = order_amounts[1::2]

# Get the top 5 order amounts
top_order_amounts = order_amounts[:5]

# Get the last 10 order amounts
last_order_amounts = order_amounts[-10:]
