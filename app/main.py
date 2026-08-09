def get_exchange_rate_prediction() -> float:
    return 100.0  # Пример значения


def cryptocurrency_action(current_rate: float) -> str:
    predicted_rate = get_exchange_rate_prediction()
    difference = (predicted_rate - current_rate) / current_rate * 100

    if difference > 5:
        return "Buy more cryptocurrency"
    elif difference < -5:
        return "Sell all your cryptocurrency"
    else:
        return "Do nothing"
