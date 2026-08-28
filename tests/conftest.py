import pytest
import subprocess
import time
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", autouse=True)
def run_app():
    """Автоматически запускает наше приложение перед тестами и выключает после"""
    # Запускаем app.py как отдельный фоновый процесс
    server_process = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # Даём серверу 2 секунды на старт
    yield
    # После завершения всех тестов "убиваем" процесс сервера
    server_process.terminate()
    server_process.wait()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # headless=False — браузер будет ВИДЕН на экране
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
