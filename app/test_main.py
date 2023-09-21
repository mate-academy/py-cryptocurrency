from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    action = cryptocurrency_action(1000)
    assert action == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    action = cryptocurrency_action(1000)
    assert action == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    action = cryptocurrency_action(1000)
    assert action == "Do nothing"


def test_edge_case_current_rate_zero() -> None:
    action = cryptocurrency_action(0)
    assert action == "Do nothing"
