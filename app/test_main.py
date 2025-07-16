from unittest.mock import MagicMock, patch

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_rate_prediction() -> MagicMock:
    with patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


def test_buy_more_when_prediction_above_5_percent(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_when_prediction_below_5_percent(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_within_5_percent(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_when_prediction_exactly_5_percent(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_when_prediction_exactly_minus_5_percent(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
