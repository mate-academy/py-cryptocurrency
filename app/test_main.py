from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_get_prediction:
        mock_get_prediction.return_value = 6

        result = cryptocurrency_action(5)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_get_prediction:
        mock_get_prediction.return_value = 1

        result = cryptocurrency_action(5)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_get_prediction:
        mock_get_prediction.return_value = 5

        result = cryptocurrency_action(5)
        assert result == "Do nothing"
