import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@pytest.fixture
def mock_get_exchange_rate_prediction() -> MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        yield mock_func


def test_rate_95_percent_do_nothing(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95

    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing", (
        "You should not sell cryptocurrency when "
        "prediction_rate / current_rate == 0.95"
    )


def test_rate_105_percent_do_nothing(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105

    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing", (
        "You should not buy cryptocurrency when "
        "prediction_rate / current_rate == 1.05"
    )
