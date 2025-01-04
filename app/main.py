def get_exchange_rate_prediction() -> float:
    pass


def cryptocurrency_action(current_rate: float) -> str:
    predicted_rate = get_exchange_rate_prediction()
    increase_threshold = current_rate * 1.05
    decrease_threshold = current_rate * 0.95

    if predicted_rate > increase_threshold:
        return "Buy more cryptocurrency"
    elif predicted_rate < decrease_threshold:
        return "Sell all your cryptocurrency"
    else:
        return "Do nothing"

