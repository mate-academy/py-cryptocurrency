from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_higher(
        mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.10
    cryptocurrency_action(1.00)
    mocked_get_exchange_rate_prediction.assert_called_with(1.00)
    assert cryptocurrency_action(1.00) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_lower(
        mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.90
    cryptocurrency_action(1.00)
    mocked_get_exchange_rate_prediction.assert_called_with(1.00)
    assert cryptocurrency_action(1.00) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_stay(
        mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.00
    cryptocurrency_action(1.00)
    mocked_get_exchange_rate_prediction.assert_called_with(1.00)
    assert cryptocurrency_action(1.00) == "Do nothing"
