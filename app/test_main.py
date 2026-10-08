from unittest import mock
from unittest.mock import Mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(
        mock_get_exchange_rate_prediction: Mock
    ) -> None:
    mock_get_exchange_rate_prediction.return_value = 3
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(
        mock_get_exchange_rate_prediction: Mock
    ) -> None:
    mock_get_exchange_rate_prediction.return_value = 2
    assert cryptocurrency_action(3) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_none(
        mock_get_exchange_rate_prediction: Mock
    ) -> None:
    mock_get_exchange_rate_prediction.return_value = 3
    assert cryptocurrency_action(3) == "Do nothing"
