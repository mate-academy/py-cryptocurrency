from typing import Union
import random


def get_exchange_rate_prediction(exchange_rate: Union[int, float]) -> float:
    if random.choice(["increase", "decrease"]) == "increase":
        return round(exchange_rate / random.random(), 2)
    return round(exchange_rate * random.random(), 2)


def cryptocurrency_action(current_rate: Union[int, float]) -> str:
    prediction_rate = get_exchange_rate_prediction(current_rate)
    ratio = prediction_rate / current_rate

    if ratio > 1.05:
        return "Buy more cryptocurrency"
    if ratio < 0.95:
        return "Sell all your cryptocurrency"
    return "Do nothing"
