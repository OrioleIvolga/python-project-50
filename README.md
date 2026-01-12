### Hexlet tests and linter status:
[![Actions Status](https://github.com/OrioleIvolga/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/OrioleIvolga/python-project-50/actions)

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