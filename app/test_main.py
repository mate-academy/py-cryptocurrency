from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_when_rate_increases(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
    mocked_get_exchange_rate_prediction.assert_called_once_with(1)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_when_rate_decreases(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
    mocked_get_exchange_rate_prediction.assert_called_once_with(1)


@pytest.mark.parametrize(
    "rate_prediction",
    [
        pytest.param(0.95, id="rate is not small enough"),
        pytest.param(1.0, id="rate is the same"),
        pytest.param(1.05, id="rate is not big enough"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_when_difference_is_small(
    mocked_get_exchange_rate_prediction: mock.MagicMock, rate_prediction: float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = rate_prediction

    assert cryptocurrency_action(1) == "Do nothing"
    mocked_get_exchange_rate_prediction.assert_called_once_with(1)
