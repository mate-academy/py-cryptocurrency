from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_crypto(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.0
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
