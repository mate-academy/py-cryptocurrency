# app/test_main.py
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 105.1
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 94.9
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_difference_small(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 102
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exactly_five_percent_increase(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exactly_five_percent_decrease(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
