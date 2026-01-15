import pytest
from unittest.mock import patch, MagicMock
from typing import Generator

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_exchange_rate_prediction() -> Generator[MagicMock, None, None]:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_large_value_expected_more_cryptocurrency(
    mock_exchange_rate_prediction: MagicMock,
) -> None:
    mock_exchange_rate_prediction.return_value = 110
    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"
    mock_exchange_rate_prediction.assert_called_once_with(100)


def test_get_value_expected_sell_cryptocurrency(
    mock_exchange_rate_prediction: MagicMock,
) -> None:
    mock_exchange_rate_prediction.return_value = 90
    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"
    mock_exchange_rate_prediction.assert_called_once_with(100)


def test_get_value_expected_do_nothing(
    mock_exchange_rate_prediction: MagicMock,
) -> None:
    mock_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)

    assert result == "Do nothing"
    mock_exchange_rate_prediction.assert_called_once_with(100)


def test_get_small_value_expected_do_nothing(
    mock_exchange_rate_prediction: MagicMock,
) -> None:
    mock_exchange_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)

    assert result == "Do nothing"
    mock_exchange_rate_prediction.assert_called_once_with(100)
