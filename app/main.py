import random
from typing import Union


def get_exchange_rate_prediction(exchange_rate: Union[int, float]) -> float:
    change_percent = random.uniform(-0.1, 0.1)
    predicted_rate = exchange_rate * (1 + change_percent)
    return round(predicted_rate, 2)


def cryptocurrency_action(current_rate: Union[int, float]) -> str:
    prediction_rate = get_exchange_rate_prediction(current_rate)
    ratio = prediction_rate / current_rate

    if ratio > 1.05:
        return "Buy more cryptocurrency"
    if ratio < 0.95:
        return "Sell all your cryptocurrency"
    return "Do nothing"
