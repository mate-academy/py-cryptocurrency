from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    # Передбачення обмінного курсу більше поточного на більше 5%.
    action = cryptocurrency_action(1000)
    assert action == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    # Передбачення обмінного курсу менше поточного на більше 5%.
    action = cryptocurrency_action(1000)
    assert action == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    # Передбачення обмінного курсу змінюється менше ніж на 5% відносно поточного.
    action = cryptocurrency_action(1000)
    assert action == "Do nothing"


def test_edge_case_current_rate_zero() -> None:
    # Перевірка для крайнього випадку, коли поточний курс дорівнює нулю.
    action = cryptocurrency_action(0)
    assert action == "Do nothing"
