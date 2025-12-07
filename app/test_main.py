from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: pytest.Mock) -> None:
    mock_prediction.return_value = 105
    current_rate: float = 100
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: pytest.Mock) -> None:
    mock_prediction.return_value = 90
    current_rate: float = 100
    assert (
        cryptocurrency_action(current_rate)
        == "Sell all your cryptocurrency"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: pytest.Mock) -> None:
    mock_prediction.return_value = 103
    current_rate: float = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_upper(mock_prediction: pytest.Mock) -> None:
    mock_prediction.return_value = 105
    current_rate: float = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_lower(mock_prediction: pytest.Mock) -> None:
    mock_prediction.return_value = 95
    current_rate: float = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"
