import random


def get_exchange_rate_prediction(exchange_rate):
    if random.choice(["increase", "decrease"]) == "increase":
        return round(exchange_rate / random.random(), 2)
    else:
        return round(exchange_rate * random.random(), 2)


def cryptocurrency_action(current_rate):
    if get_exchange_rate_prediction(current_rate) / current_rate > 1.05:
        return "Buy more cryptocurrency"
    elif get_exchange_rate_prediction(current_rate)/current_rate < 1.05:
        return "Sell all your cryptocurrency"
    else:
        return "Do nothing"
