import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


def test_cryptocurrency_action_buy(
        mocked_get_exchange_rate_prediction: None
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell(
        mocked_get_exchange_rate_prediction: None
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
        mocked_get_exchange_rate_prediction: None
) -> None:
    for return_index in [0.95, 1, 1.05]:
        mocked_get_exchange_rate_prediction.return_value = return_index
        assert cryptocurrency_action(1) == "Do nothing"
