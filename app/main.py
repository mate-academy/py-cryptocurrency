import random
from typing import Union


def get_exchange_rate_prediction(exchange_rate: Union[int, float]) -> float:
    if random.choice(["increase", "decrease"]) == "increase":
        return round(exchange_rate / random.random(), 2)
    return round(exchange_rate * random.random(), 2)


def cryptocurrency_action(current_rate: Union[int, float]) -> str:
    if not isinstance(current_rate, (int, float)):
        raise TypeError("Current rate must be a number")

    if current_rate <= 0:
        raise ValueError("Current rate must be greater than zero")

    prediction_rate = get_exchange_rate_prediction(current_rate)
    if prediction_rate / current_rate > 1.05:
        return "Buy more cryptocurrency"
    if prediction_rate / current_rate < 0.95:
        return "Sell all your cryptocurrency"
    return "Do nothing"
