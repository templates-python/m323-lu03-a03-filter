def filter_by_age(students, min_age):
    result = []
    for student in students:
        if student['age'] >= min_age:
            result.append(student)
    return result


def filter_by_class(students, class_name):
    result = []
    for student in students:
        if student['class'] == class_name:
            result.append(student)
    return result


def filter_students(students, filter_function, *args):
    return filter_function(students, *args)


if __name__ == '__main__':
    students = [
        {'name': 'Alice', 'age': 15, 'class': '10A'},
        {'name': 'Bob', 'age': 16, 'class': '10B'},
        {'name': 'Charlie', 'age': 14, 'class': '9A'},
    ]

    filtered_by_age = filter_students(students, filter_by_age, 15)
    print('Filtered by age:', filtered_by_age)

    filtered_by_class = filter_students(students, filter_by_class, '10A')
    print('Filtered by class:', filtered_by_class)
