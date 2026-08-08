from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.fixture
def current_rate() -> int:
    return 1


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_prediction: mock.Mock, current_rate: int
) -> None:
    mock_prediction.return_value = 1.06
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency(
    mock_prediction: mock.Mock, current_rate: int
) -> None:
    mock_prediction.return_value = 0.94
    assert (cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
    mock_prediction: mock.Mock, current_rate: int
) -> None:
    mock_prediction.return_value = 1.05
    assert cryptocurrency_action(current_rate) == "Do nothing"

    mock_prediction.return_value = 0.95
    assert cryptocurrency_action(current_rate) == "Do nothing"
