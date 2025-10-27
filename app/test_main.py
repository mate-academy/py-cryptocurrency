import app.main


def test_rate_105_percent_do_nothing() -> None:
    app.main.get_exchange_rate_prediction = lambda x: x * 1.05
    assert app.main.cryptocurrency_action(100) == "Do nothing"


def test_rate_95_percent_do_nothing() -> None:
    app.main.get_exchange_rate_prediction = lambda x: x * 0.95
    assert app.main.cryptocurrency_action(100) == "Do nothing"


def test_rate_above_105_buy_more() -> None:
    app.main.get_exchange_rate_prediction = lambda x: x * 1.06
    assert app.main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_rate_below_95_sell_all() -> None:
    app.main.get_exchange_rate_prediction = lambda x: x * 0.94
    assert app.main.cryptocurrency_action(
        100
    ) == "Sell all your cryptocurrency"
