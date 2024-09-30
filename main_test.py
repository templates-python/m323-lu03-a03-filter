import main


def test_filter_by_age():
    sample_students = [
        {'name': 'Alice', 'age': 15, 'class': '10A'},
        {'name': 'Bob', 'age': 16, 'class': '10B'},
        {'name': 'Charlie', 'age': 14, 'class': '9A'},
    ]
    result = main.filter_by_age(sample_students, 15)
    expected = [
        {'name': 'Alice', 'age': 15, 'class': '10A'},
        {'name': 'Bob', 'age': 16, 'class': '10B'},
    ]
    assert result == expected


def test_filter_by_class():
    sample_students = [
        {'name': 'Alice', 'age': 15, 'class': '10A'},
        {'name': 'Bob', 'age': 16, 'class': '10B'},
        {'name': 'Charlie', 'age': 14, 'class': '9A'},
    ]
    result = main.filter_by_class(sample_students, '10A')
    expected = [{'name': 'Alice', 'age': 15, 'class': '10A'}]
    assert result == expected


def test_filter_students():
    sample_students = [
        {'name': 'Alice', 'age': 15, 'class': '10A'},
        {'name': 'Bob', 'age': 16, 'class': '10B'},
        {'name': 'Charlie', 'age': 14, 'class': '9A'},
    ]
    result = main.filter_students(sample_students, main.filter_by_age, 15)
    expected = [
        {'name': 'Alice', 'age': 15, 'class': '10A'},
        {'name': 'Bob', 'age': 16, 'class': '10B'},
    ]
    assert result == expected
