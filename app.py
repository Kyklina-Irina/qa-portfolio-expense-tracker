from flask import Flask, request
import re

app = Flask(__name__)
# "База данных" в памяти
expenses = [] 

@app.route('/')
def index():
    # Вычисляем общую сумму
    total = sum(exp['amount'] for exp in expenses) 
    
    html = f'''
        <h1>💰 Трекер Расходов</h1>
        <form action="/add" method="POST">
            Категория: <input type="text" name="category" placeholder="Еда, Транспорт..."><br><br>
            Сумма: <input type="text" name="amount" placeholder="Введите число"><br><br>
            Дата: <input type="date" name="date"><br><br>
            <button type="submit">Добавить расход</button>
        </form>
        <hr>
        <h2>Итого за текущий месяц: {total}</h2>
    '''
    return html

@app.route('/add', methods=['POST'])
def add():
    category = request.form.get('category')
    amount_str = request.form.get('amount')
    date = request.form.get('date')

    # "Умная" очистка суммы от символов (например, если ввели "100$")
    digits = re.sub(r'[^\d.]', '', amount_str)
    amount = float(digits) if digits else 0.0 

    expenses.append({
        'category': category, 
        'amount': amount, 
        'date': date
    })
    
    return '<h3>Успешно!</h3> <a href="/">Вернуться назад</a>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
