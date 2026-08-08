import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> mock.MagicMock:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange_rate_prediction:
        yield mock_get_exchange_rate_prediction


def test_buy_more_crypto_when_prediction_rate_is_5_percent_higher(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_crypto_when_prediction_rate_is_5_percent_lower(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_rate_is_within_5_percent(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 1.0
    assert cryptocurrency_action(1) == "Do nothing"
