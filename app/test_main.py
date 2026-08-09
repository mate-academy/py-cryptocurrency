from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_rate_rises_too_high(mocked_prediction: MagicMock) -> None:
    mocked_prediction.return_value = 110
    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_when_rate_rises_too_low(mocked_prediction: MagicMock) -> None:
    mocked_prediction.return_value = 90
    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_95_percent(mocked_prediction: MagicMock) -> None:
    mocked_prediction.return_value = 95
    result = cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_105_percent(mocked_prediction: MagicMock) -> None:
    mocked_prediction.return_value = 105
    result = cryptocurrency_action(100)

    assert result == "Do nothing"
