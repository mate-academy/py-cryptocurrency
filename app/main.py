import random
from typing import Union


def get_exchange_rate_prediction(exchange_rate: Union[int, float]) -> float:
    """
    Predict the next day's cryptocurrency exchange rate.
    Randomly increases or decreases the current rate.
    """
    if random.choice(["increase", "decrease"]) == "increase":
        return round(exchange_rate / random.random(), 2)
    return round(exchange_rate * random.random(), 2)


def cryptocurrency_action(current_rate: Union[int, float]) -> str:
    """
    Decide cryptocurrency action based on predicted exchange rate.

    Returns:
        - "Buy more cryptocurrency" if prediction > +5% of current rate
        - "Sell all your cryptocurrency" if prediction < -5% of current rate
        - "Do nothing" otherwise
    """
    if current_rate <= 0:
        raise ValueError("Current rate must be a positive number.")

    prediction_rate: float = get_exchange_rate_prediction(current_rate)
    rate_ratio: float = prediction_rate / current_rate

    if rate_ratio > 1.05:
        return "Buy more cryptocurrency"
    if rate_ratio < 0.95:
        return "Sell all your cryptocurrency"
    return "Do nothing"
