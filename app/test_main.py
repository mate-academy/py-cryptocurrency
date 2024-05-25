from app.main import cryptocurrency_action
from unittest import mock


def test_buy_more_cryptocurrency() -> None:
    current_rate = 100.0
    predicted_rate = 106.0  # 6% higher than current_rate

    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    current_rate = 100.0
    predicted_rate = 94.0  # 6% lower than current_rate

    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == ("Sell all your "
                                                       "cryptocurrency")


def test_do_nothing() -> None:
    current_rate = 100.0
    predicted_rate = 102.0  # 2% higher than current_rate

    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_edge_case_upper() -> None:
    current_rate = 100.0
    predicted_rate = 105.0  # Exactly 5% higher than current_rate

    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_edge_case_lower() -> None:
    current_rate = 100.0
    predicted_rate = 95.0  # Exactly 5% lower than current_rate

    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == "Do nothing"
