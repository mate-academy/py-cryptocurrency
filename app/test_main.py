from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        yield mock_exchange


def test_cryptocurrency_action_buy(mock_prediction: mock.MagicMock) -> None:
    mock_prediction.return_value = 60
    assert cryptocurrency_action(50) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell(mock_prediction: mock.MagicMock) -> None:
    mock_prediction.return_value = 40
    assert cryptocurrency_action(50) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 51
    assert cryptocurrency_action(50) == "Do nothing"


def test_rate_95_percent_do_nothing(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 52.5
    assert cryptocurrency_action(50) == "Do nothing"


def test_rate_105_percent_do_nothing(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 47.5
    assert cryptocurrency_action(50) == "Do nothing"
