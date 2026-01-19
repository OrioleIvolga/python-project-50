### Hexlet tests and linter status:
[![Actions Status](https://github.com/OrioleIvolga/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/OrioleIvolga/python-project-50/actions)
[![CI](https://github.com/OrioleIvolga/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/OrioleIvolga/python-project-50/actions/workflows/ci.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=OrioleIvolga_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=OrioleIvolga_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=OrioleIvolga_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=OrioleIvolga_python-project-50)

## Пример использования

Сравнение двух JSON-файлов:

Файл1 `file1.json`
```json
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
```

Файл2 `file2.json`
```json
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
```

Запуск утилиты

```bash
gendiff file1.json file2.json
```

Результат

```diff
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

Сравнение двух YAML-файлов

Файл1 `file1.yml`
```yml
host: hexlet.io
proxy: 123.234.53.22
timeout: 50
follow: false
```

Файл2 `file2.yml`
```yml
host: hexlet.io
timeout: 20
verbose: true
```

Запуск утилиты

```bash
gendiff file1.yml file2.yml
```

Результат

```diff
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

Сравнение файлов со вложенными структурами

Файл1 `file1.yml`
```yaml
common:
  setting1: Value 1
  setting2: 200
  setting3: true
  setting6:
    key: value
    doge:
      wow: ""
group1:
  baz: bas
  foo: bar
  nest:
    key: value
group2:
  abc: 12345
  deep:
    id: 45
```

Файл2 `file2.yml`
```yaml
common:
  follow: false
  setting1: Value 1
  setting3: null
  setting4: blah blah
  setting5:
    key5: value5
  setting6:
    key: value
    ops: vops
    doge:
      wow: so much
group1:
  foo: bar
  baz: bars
  nest: str
group3:
  deep:
    id:
      number: 45
  fee: 100500
```

Запуск утилиты

```bash
ggendiff file1.yml file2.yml
```

Результат

```diff
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
```