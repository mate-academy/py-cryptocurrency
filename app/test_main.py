from unittest.mock import patch, MagicMock
import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_rate: MagicMock,
) -> None:
    mock_rate.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mock_rate: MagicMock,
) -> None:
    mock_rate.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@pytest.mark.parametrize("predicted", [104.9, 105.0, 95.0, 95.1])
@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
    mock_rate: MagicMock,
    predicted: float,
) -> None:
    mock_rate.return_value = predicted
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
