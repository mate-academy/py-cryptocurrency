from unittest.mock import patch

from app.main import cryptocurrency_action


def test_should_buy_when_prediction_more_than_5_percent_higher() -> None:
    current_rate = 100

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=106,
    ):
        assert (
            cryptocurrency_action(current_rate)
            == "Buy more cryptocurrency"
        )


def test_should_sell_when_prediction_more_than_5_percent_lower() -> None:
    current_rate = 100

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=94,
    ):
        assert (
            cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency"
        )


def test_should_do_nothing_when_prediction_within_upper_bound() -> None:
    current_rate = 100

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=105,
    ):
        assert cryptocurrency_action(current_rate) == "Do nothing"


def test_should_do_nothing_when_prediction_within_lower_bound() -> None:
    current_rate = 100

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=95,
    ):
        assert cryptocurrency_action(current_rate) == "Do nothing"


def test_should_do_nothing_when_prediction_equal_to_current() -> None:
    current_rate = 100

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=100,
    ):
        assert cryptocurrency_action(current_rate) == "Do nothing"
