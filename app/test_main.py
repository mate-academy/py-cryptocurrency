import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_prediction:
        yield mock_prediction


def test_buy_more_crypto(mocked_exchange_rate_prediction: None) -> None:
    mocked_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


def test_sell_all_crypto(mocked_exchange_rate_prediction: None) -> None:
    mocked_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_exchange_rate_prediction: None) -> None:
    mocked_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1.0) == "Do nothing"
