"""
Модуль validators - функции для валидации данных.
"""
import re

def validate_email(email):
    if not email:
        return False, "Email не может быть пустым"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, "Email корректен"
    else:
        return False, "Некорректный формат email"

def validate_age(age):
    if not isinstance(age, (int, float)):
        return False, "Возраст должен быть числом"
    if age < 16:
        return False, "Студент должен быть старше 16 лет"
    if age > 100:
        return False, "Некорректный возраст"
    return True, "Возраст корректен"

def validate_grade(grade):
    if not isinstance(grade, (int, float)):
        return False, "Оценка должна быть числом"
    if grade < 2 or grade > 5:
        return False, "Оценка должна быть от 2 до 5"
    return True, "Оценка корректна"

def validate_name(name):
    if not name or not isinstance(name, str):
        return False, "Имя не может быть пустым"
    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"
    if not name.replace('-', '').replace(' ', '').isalpha():
        return False, "Имя должно содержать только буквы"
    return True, "Имя корректно"

def validate_student_name(first_name, last_name):
    if not first_name or not isinstance(first_name, str) or first_name.strip() == "":
        return False, "Имя не может быть пустым"
    if not last_name or not isinstance(last_name, str) or last_name.strip() == "":
        return False, "Фамилия не может быть пустой"
    if not first_name.istitle():
        return False, "Имя должно начинаться с заглавной буквы"
    if not last_name.istitle():
        return False, "Фамилия должна начинаться с заглавной буквы"
    name_without_hyphen = first_name.replace('-', '').replace(' ', '')
    if not name_without_hyphen.isalpha():
        return False, "Имя должно содержать только буквы"
    last_without_hyphen = last_name.replace('-', '').replace(' ', '')
    if not last_without_hyphen.isalpha():
        return False, "Фамилия должна содержать только буквы"
    return True, "Имя и фамилия корректны"

if __name__ == "__main__":
    test_emails = ["test@example.com", "invalid-email", "user@domain", "a@b.c"]
    for email in test_emails:
        valid, msg = validate_email(email)
        print(f"{email}: {msg}")
