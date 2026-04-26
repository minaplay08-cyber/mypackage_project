# Лабораторная работа 9: Создание своего пакета и работа с внешними библиотеками

## Описание
Пакет `mypackage` для работы с данными о студентах и внешними API.

## Структура пакета
```
mypackage/
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── student.py
│   └── group.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   └── formatters.py
├── api/
│   ├── __init__.py
│   └── client.py
└── data/
```

## Установка
```bash
pip install -r requirements.txt
```

## Использование
```python
from mypackage import Student, Group, APIClient

# Работа со студентами
student = Student("Иван", "Петров", 19)
student.add_grade(5, "Python")

# Работа с группами
group = Group("ПИН-231")
group.add_student(student)

# Работа с API
client = APIClient()
posts = client.get_posts()
```

## Запуск
```bash
python main.py
python test_import.py
```

## Версия
1.0.0
