from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 30

    result = cryptocurrency_action(15)

    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_leave_if_small_decline(mock_get_exchange_rate_prediction:
                                MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 14.25

    result = cryptocurrency_action(15)

    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_leave_if_small_growth(mock_get_exchange_rate_prediction:
                               MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 15.75

    result = cryptocurrency_action(15)

    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_better_to_sell(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 10

    result = cryptocurrency_action(15)

    assert result == "Sell all your cryptocurrency"
