# Cryptocurrency

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

You have some amount of cryptocurrency "Matecoin" in your online wallet.
You also bought a program (function `get_exchange_rate_prediction`) that
can predict the exchange rate of your cryptocurrency for the next day.

Inside `app/test_main.py`, write tests for `cryptocurrency_action` function. This function 
takes `current_rate` - current exchange rate of cryptocurrency. This
function should return:
- `"Buy more cryptocurrency"`, if predicted exchange rate is more than 
5% higher from the current.
- `"Sell all your cryptocurrency"`, if predicted exchange rate is more than 
5% lower from the current.
- `"Do nothing"`, if difference is not that much.

Mock `get_exchange_rate_prediction` function.

Run `pytest app/` to check if function pass your tests.

Run `pytest --numprocesses=auto tests/` to check if your tests cover all boundary conditions
and pass task tests.


У вашому онлайн-гаманці є певна кількість криптовалюти «Matecoin».
Ви також купили програму (функцію `get_exchange_rate_prediction`), яка
можна передбачити курс вашої криптовалюти на наступний день.

Усередині `app/test_main.py` напишіть тести для функції `cryptocurrency_action`. Ця функція
приймає `current_rate` - поточний курс обміну криптовалюти. Це
функція повинна повернути:
- `"Купити більше криптовалюти", якщо прогнозований курс більше ніж
на 5% вище від поточного.
- `"Продати всю свою криптовалюту", якщо прогнозований курс перевищує ніж
на 5% нижче від поточного.
- `"Нічого не робити", якщо різниця не така велика.

Підроблена функція `get_exchange_rate_prediction`.

Запустіть `pytest app/`, щоб перевірити, чи функція пройшла ваші тести.

Виконайте `pytest --numprocesses=auto tests/`, щоб перевірити, чи охоплюють ваші тести всі граничні умови
та пройдіть тести завдань.