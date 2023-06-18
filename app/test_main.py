from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_crypto(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.1
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.9
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"
