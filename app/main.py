import random
from typing import Union


def get_exchange_rate_prediction(exchange_rate: Union[int, float]) -> float:
    if random.choice(["increase", "decrease"]) == "increase":
        rand = random.random()
        return round(exchange_rate / rand, 2)
    else:
        rand = random.random()
        return round(exchange_rate * rand, 2)


def cryptocurrency_action(current_rate: Union[int, float]) -> str:
    prediction_rate = get_exchange_rate_prediction(current_rate)
    if prediction_rate / current_rate > 1.05:
        return "Buy more cryptocurrency"
    if prediction_rate / current_rate < 0.95:
        return "Sell all your cryptocurrency"
    return "Do nothing"
