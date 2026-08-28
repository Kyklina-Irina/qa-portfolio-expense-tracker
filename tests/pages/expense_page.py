from playwright.sync_api import Page

class ExpensePage:
    """Page Object для страницы трекера расходов"""
    
    def __init__(self, page: Page):
        self.page = page
        self.url = "http://127.0.0.1:5000"
        
    def open(self):
        """Открыть главную страницу"""
        self.page.goto(self.url)
        
    def add_expense(self, category: str, amount: str, date: str):
        """Заполнить форму и добавить расход"""
        self.page.fill('input[name="category"]', category)
        self.page.fill('input[name="amount"]', amount)
        self.page.fill('input[name="date"]', date)
        self.page.click('button[type="submit"]')
        
    def get_total_amount(self) -> str:
        """Получить текст с итоговой суммой"""
        # Находим h2 с текстом "Итого..."
        total_element = self.page.locator('h2').first
        return total_element.text_content()
        
    def get_success_message(self) -> str:
        """Получить сообщение об успехе"""
        return self.page.locator('h3').text_content()
