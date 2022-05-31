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
Run `pytest tests/` to check if your tests cover all boundary conditions
and pass task tests.