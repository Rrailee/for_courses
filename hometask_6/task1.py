import json

data = open('purchase_log.txt', encoding="UTF-8")
result_dict = dict()
for line in data:
    line = json.loads(line)
    result_dict[line["user_id"]] = line["category"]

print(result_dict)