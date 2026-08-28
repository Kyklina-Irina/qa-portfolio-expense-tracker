import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Запускаем браузер один раз на все тесты"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Без графического интерфейса
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    """Создаём новую страницу для каждого теста"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
