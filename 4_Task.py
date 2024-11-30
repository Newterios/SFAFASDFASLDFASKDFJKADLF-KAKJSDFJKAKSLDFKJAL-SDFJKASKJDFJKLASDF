def main(listr:list) -> str:
    max_category = dict()
    total = 0
    for item in listr:
        if item['category'] not in max_category:
            max_category[item['category']] = item['amount']
            total += item['amount']
        else:
            max_category[item['category']] += item['amount']
            total += item['amount']
    max = [None, -float('inf')]
    for i in max_category:
        if max[1] < max_category[i]:
            max[1] = max_category[i]
            max[0] = i
    return f'Total: {total} \nmax_category: {max[0]}'

expenses = [
    {"category": "food", "amount": 120.5},
    {"category": "transport", "amount": 55.3},
    {"category": "food", "amount": 80.2},
    {"category": "entertainment", "amount": 200},
    {"category": "transport", "amount": 45.1},
]
print(main(expenses))