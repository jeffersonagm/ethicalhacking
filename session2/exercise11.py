class InvalidGradeError(Exception):
    pass


def validate_grade(grade):
    if grade < 0 or grade > 10:
        raise InvalidGradeError("La nota debe estar entre 0 y 10")
    
    return grade


grade = float(input("Introduce la nota: "))

try:
    validate_grade(grade)
    print("Nota válida")
except InvalidGradeError as e:
    print(e)