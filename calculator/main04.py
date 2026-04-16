orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

result = []

for order in orders:
    if order[0] % 2 == 0:
        result.append(order)

print(result)