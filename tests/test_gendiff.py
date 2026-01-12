import os
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)


def read(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read(get_fixture_path('expected_diff.txt')).strip()

    result = generate_diff(file1, file2)

    assert result.strip() == expected
