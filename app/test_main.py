from unittest import mock

from .main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 106
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 94
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 105
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
        mocked_prediction.return_value = 95
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
