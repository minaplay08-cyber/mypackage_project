"""
Тестирование импорта пакета mypackage.
"""
print("=" * 50)
print("ТЕСТИРОВАНИЕ ИМПОРТА ПАКЕТА")
print("=" * 50)
print("\n1. Импорт пакета:")
import mypackage
print(f" Версия: {mypackage.__version__}")
print(f" Доступные компоненты: {mypackage.__all__}")
print("\n2. Импорт подпакетов:")
from mypackage import models
from mypackage import utils
from mypackage import api
print(" Подпакеты загружены успешно")
print("\n3. Импорт классов:")
from mypackage.models import Student, Group
from mypackage.utils import validate_email, format_student_info
from mypackage.api import APIClient
print(" Классы импортированы успешно")
print("\n4. Тестирование Student:")
student = Student("Тест", "Тестов", 20, "test@example.com")
print(f" Создан студент: {student}")
print(f" ID: {student.student_id}")
student.add_grade(5, "Python")
print(f" Средний балл: {student.get_average_grade()}")
print("\n5. Тестирование Group:")
group = Group("Тест-группа", curator="Профессор")
group.add_student(student)
print(f" Количество студентов: {group.get_students_count()}")
print(f" Средний балл группы: {group.get_group_average()}")
print("\n6. Тестирование валидаторов:")
valid, msg = validate_email("valid@email.com")
print(f" Email 'valid@email.com': {msg}")
valid, msg = validate_email("invalid-email")
print(f" Email 'invalid-email': {msg}")
print("\n" + "=" * 50)
print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО!")
print("=" * 50)
