import random


def get_exchange_rate_prediction(exchange_rate):
    if random.choice(["increase", "decrease"]) == "increase":
        return round(exchange_rate / random.random(), 2)
    else:
        return round(exchange_rate * random.random(), 2)


def cryptocurrency_action(current_rate):
    prediction_rate = get_exchange_rate_prediction(current_rate)
    if prediction_rate / current_rate > 1.05:
        print(prediction_rate, current_rate)
        print(prediction_rate / current_rate)
        return "Buy more cryptocurrency"
    if prediction_rate / current_rate < 0.95:
        print(prediction_rate, current_rate)
        print(prediction_rate / current_rate)
        return "Sell all your cryptocurrency"
    print(prediction_rate, current_rate)
    print(prediction_rate / current_rate)
    return "Do nothing"


if __name__ == "__main__":
    print(cryptocurrency_action(10))


