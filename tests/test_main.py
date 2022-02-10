from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_more_than_5_percent_higher(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 10.6

    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_more_than_5_percent_lower(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 9.4

    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(15) == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "exchange_rate,current_rate, expected",
    [
        (1, 0.953, "Do nothing"),
        (1, 1.052, "Do nothing"),
        (1, 1.03, "Do nothing"),
        (1, 0.952, "Buy more cryptocurrency"),
        (1, 1.053, "Sell all your cryptocurrency")

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_difference_is_only_5_percent(
        mocked_get_exchange_rate_prediction,
        exchange_rate,
        current_rate,
        expected
):
    mocked_get_exchange_rate_prediction.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == expected
