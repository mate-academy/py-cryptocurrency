from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_exchange_rate_prediction() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_cryptocurrency_action_buy(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 1.06 * 100
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_buy2(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 3.01 * 100
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_buy3(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 3.04 * 100
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"
