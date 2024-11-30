def to_show_age_students(listr:list) -> dict:
    result = {}
    for item in listr:
        if item['age'] not in result.keys():
            result[item['age']] = [item["name"]]
        else:
            result[item['age']].append(item["name"])
    return result

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 22},
    {"name": "Eve", "age": 21},
]

print(to_show_age_students(students))