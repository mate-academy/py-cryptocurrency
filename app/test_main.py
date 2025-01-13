from unittest import mock

from app.main import cryptocurrency_action


def test_cryptocurrency_action_when_rate_increases_more_than_5_percent() \
        -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=110):
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_when_rate_decreases_more_than_5_percent() \
        -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"


def test_cryptocurrency_action_when_rate_changes_less_than_5_percent() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"
