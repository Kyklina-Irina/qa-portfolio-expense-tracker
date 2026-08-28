import os
import subprocess
import time

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session", autouse=True)
def run_app():
    """Сам запускает приложение перед тестами и выключает после"""
    server_process = subprocess.Popen(["python", "app.py"])
    time.sleep(2)
    yield
    server_process.terminate()
    server_process.wait()


@pytest.fixture(scope="session")
def browser():
    # Дома: HEADLESS=false python -m pytest tests/ -v  (браузер виден)
    # В CI: по умолчанию headless=True (браузер невидим)
    headless = os.getenv("HEADLESS", "true").lower() != "false"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
