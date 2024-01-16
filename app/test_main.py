import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> mock.MagicMock:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_test_get_exchange_rate_prediction):
        yield mock_test_get_exchange_rate_prediction


def test_not_buy_cryptocurrency(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) != "Buy more cryptocurrency"


def test_not_sell_cryptocurrency(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) != "Sell all your cryptocurrency"
