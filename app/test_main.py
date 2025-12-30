import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action

TEST_RATE: float = 100.0


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_get_prediction: MagicMock) -> None:
    predicted_rate: float = TEST_RATE * 1.10
    mock_get_prediction.return_value = predicted_rate

    result: str = cryptocurrency_action(TEST_RATE)

    assert result == "Buy more cryptocurrency"
    mock_get_prediction.assert_called_once_with(TEST_RATE)


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_get_prediction: MagicMock) -> None:
    predicted_rate: float = TEST_RATE * 0.90
    mock_get_prediction.return_value = predicted_rate

    result: str = cryptocurrency_action(TEST_RATE)

    assert result == "Sell all your cryptocurrency"
    mock_get_prediction.assert_called_once_with(TEST_RATE)


@pytest.mark.parametrize("predicted_rate", [
    TEST_RATE * 1.05,
    TEST_RATE * 0.95,
    TEST_RATE * 1.00,
    TEST_RATE * 1.049,
    TEST_RATE * 0.951,
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mock_get_prediction: MagicMock,
        predicted_rate: float
) -> None:
    mock_get_prediction.return_value = predicted_rate

    result: str = cryptocurrency_action(TEST_RATE)

    assert result == "Do nothing"
    mock_get_prediction.assert_called_once_with(TEST_RATE)
