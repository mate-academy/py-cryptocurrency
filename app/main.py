import random
from typing import Union


def get_exchange_rate_prediction(exchange_rate: Union[int, float]) -> float:
    """Предсказывает курс на основе случайного выбора."""
    if random.choice(["increase", "decrease"]) == "increase":
        return round(exchange_rate / random.uniform(0.5, 1.5), 2)
    return round(exchange_rate * random.uniform(0.5, 1.5), 2)


def cryptocurrency_action(current_rate: Union[int, float]) -> str:
    """Принимает решение на основе предсказанного курса."""
    prediction_rate = get_exchange_rate_prediction(current_rate)

    change_ratio = prediction_rate / current_rate
    if change_ratio > 1.05:
        return "Buy more cryptocurrency"
    if change_ratio < 0.95:
        return "Sell all your cryptocurrency"
    return "Do nothing"
