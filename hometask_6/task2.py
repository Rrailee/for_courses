import json

data = open('purchase_log.txt', encoding="UTF-8")
result_dict = dict()
for line in data:
    line = json.loads(line)
    result_dict[line["user_id"]] = line["category"]

data_orders = open('visit_log.csv', encoding="UTF-8")
orders = []

for line in data_orders:
    line = line.replace('\n', '').split(',')
    if line[0] in result_dict.keys():
        orders.append([line[0], line[1], result_dict[line[0]]])
print(orders[:5])