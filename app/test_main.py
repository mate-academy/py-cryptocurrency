import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.fixture
def mock_get_exchange_rate_prediction() -> "patch":
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_cryptocurrency_action_buy_more(
        mock_get_exchange_rate_prediction: "patch"
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.1
    current_rate: float = 1.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(
        mock_get_exchange_rate_prediction: "patch"
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.9
    current_rate: float = 1.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
        mock_get_exchange_rate_prediction: "patch"
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.02
    current_rate: float = 1.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_cryptocurrency_action_do_nothing_equal_rates(
        mock_get_exchange_rate_prediction: "patch"
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.0
    current_rate: float = 1.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
