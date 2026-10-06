from unittest.mock import MagicMock, patch

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_prediction() -> MagicMock:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_buy_more_cryptocurrency(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 106

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 94

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 100

    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_5_percent_higher(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_5_percent_lower(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"
