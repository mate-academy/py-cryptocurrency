from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.fixture
def mock_exchange_rate_prediction() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_cryptocurrency_action_buy(mock_exchange_rate_prediction: str) -> None:
    mock_exchange_rate_prediction.return_value = 1.05 * 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


def test_cryptocurrency_action_sell(
        mock_exchange_rate_prediction: str
) -> None:
    mock_exchange_rate_prediction.return_value = 0.95 * 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


def test_cryptocurrency_action_do_nothing(
        mock_exchange_rate_prediction: str
) -> None:
    mock_exchange_rate_prediction.return_value = 1.02 * 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
