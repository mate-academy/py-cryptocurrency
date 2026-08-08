import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction() -> mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_return_do_nothing_when_change_less_five_percent(
    mocked_prediction: mock
) -> None:
    mocked_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_returns_buy_when_change_more_than_five_percent_up(
    mocked_prediction: mock
) -> None:
    mocked_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_returns_sell_when_change_more_than_five_percent_down(
    mocked_prediction: mock
) -> None:
    mocked_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_get_exchange_rate_prediction_is_called(
    mocked_prediction: mock
) -> None:
    mocked_prediction.return_value = 100
    cryptocurrency_action(100)
    mocked_prediction.assert_called_once_with(100)
