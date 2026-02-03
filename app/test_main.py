# write your code here
def cryptocurrency_action(current_rate: float) -> str:
    predicted = get_exchange_rate_prediction(current_rate)
    if predicted > current_rate * 1.05:
        return "Buy more cryptocurrency"
    elif predicted < current_rate * 0.95:
        return "Sell all your cryptocurrency"
    else:
        return "Do nothing"
