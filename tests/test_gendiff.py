import json
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


def test_generate_diff_yaml():
    result = generate_diff('file1.yml', 'file2.yml')
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert result == expected

def test_generate_diff_nested():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    # Проверьте начало вывода
    assert "common: {" in result
    assert "  + follow: false" in result
    assert "  - setting2: 200" in result

def test_generate_diff_plain():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain')
    expected_lines = [
        "Property 'common.follow' was added with value: false",
        "Property 'common.setting2' was removed",
        "Property 'common.setting3' was updated. From true to null",
        "Property 'common.setting4' was added with value: 'blah blah'",
        "Property 'common.setting5' was added with value: [complex value]",
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'",
        "Property 'common.setting6.ops' was added with value: 'vops'",
        "Property 'group1.baz' was updated. From 'bas' to 'bars'",
        "Property 'group1.nest' was updated. From [complex value] to 'str'",
        "Property 'group2' was removed",
        "Property 'group3' was added with value: [complex value]",
    ]
    result_lines = result.strip().split('\n')
    assert result_lines == expected_lines

def test_generate_diff_json():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json')
    # Проверим, что это валидный JSON и содержит ключевые поля
    parsed = json.loads(result)
    assert isinstance(parsed, list)
    keys = [item['key'] for item in parsed]
    assert 'common' in keys
    assert 'group2' in keys
