import pytest
from datetime import datetime
from pages.expense_page import ExpensePage

def test_add_valid_expense(page):
    """
    Тест-кейс: Успешное добавление валидного расхода
    Шаги:
    1. Открыть страницу
    2. Добавить расход: Еда, 100, сегодня
    3. Проверить сообщение об успехе
    4. Проверить, что сумма обновилась
    """
    expense_page = ExpensePage(page)
    expense_page.open()
    
    # Добавляем расход
    today = datetime.now().strftime('%Y-%m-%d')
    expense_page.add_expense('Еда', '100', today)
    
    # Проверяем результат
    assert "Успешно!" in expense_page.get_success_message()
    
    # Возвращаемся на главную и проверяем сумму
    expense_page.open()
    total = expense_page.get_total_amount()
    assert "100" in total  # Сумма должна содержать 100


def test_add_expense_with_zero_amount(page):
    """
    Тест-кейс: Попытка добавить расход с суммой 0
    Ожидаемое поведение: Ошибка валидации
    Примечание: Сейчас это БАГ - система принимает 0
    """
    expense_page = ExpensePage(page)
    expense_page.open()
    
    today = datetime.now().strftime('%Y-%m-%d')
    expense_page.add_expense('Еда', '0', today)
    
    # Проверяем, что появилось сообщение об успехе (это БАГ!)
    success_msg = expense_page.get_success_message()
    # Когда баг будет исправлен, этот тест должен упасть
    # и мы поменяем логику на проверку ошибки
    assert "Успешно!" in success_msg


def test_add_expense_with_negative_amount(page):
    """
    Тест-кейс: Попытка добавить расход с отрицательной суммой
    Ожидаемое поведение: Ошибка валидации
    Примечание: Сейчас это БАГ - система принимает отрицательные числа
    """
    expense_page = ExpensePage(page)
    expense_page.open()
    
    today = datetime.now().strftime('%Y-%m-%d')
    expense_page.add_expense('Еда', '-100', today)
    
    # Проверяем результат
    success_msg = expense_page.get_success_message()
    assert "Успешно!" in success_msg  # Это БАГ!
