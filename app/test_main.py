# write your code here
def get_exchange_rate_prediction(current_rate: float) -> float:
    """
    Повертає прогнозований курс Matecoin на наступний день.
    В реальній задачі це складна функція або API.
    """
    # тимчасова заглушка
    return current_rate


def cryptocurrency_action(current_rate: float) -> str:
    """
    Повертає рекомендацію: купувати, продавати або нічого не робити,
    залежно від прогнозованого курсу.
    """
    predicted_rate = get_exchange_rate_prediction(current_rate)
    change_percent = (predicted_rate - current_rate) / current_rate * 100

    if change_percent > 5:
        return "Buy more cryptocurrency"
    elif change_percent < -5:
        return "Sell all your cryptocurrency"
    else:
        return "Do nothing"
