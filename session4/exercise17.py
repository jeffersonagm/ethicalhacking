students = [
    {"name": "Jefferson", "grade": 8},
    {"name": "Carlos", "grade": 6},
    {"name": "Ana", "grade": 9},
    {"name": "Luis", "grade": 5}
]

names = [student["name"] for student in students if student["grade"] >= 7]

print(names)