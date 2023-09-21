from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency():
    # Передбачення обмінного курсу більше поточного на більше 5%.
    action = cryptocurrency_action(1000)
    assert action == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency():
    # Передбачення обмінного курсу менше поточного на більше 5%.
    action = cryptocurrency_action(1000)
    assert action == "Sell all your cryptocurrency"


def test_do_nothing():
    # Передбачення обмінного курсу змінюється менше ніж на 5% відносно поточного.
    action = cryptocurrency_action(1000)
    assert action == "Do nothing"


def test_edge_case_current_rate_zero():
    # Перевірка для крайнього випадку, коли поточний курс дорівнює нулю.
    action = cryptocurrency_action(0)
    assert action == "Do nothing"
