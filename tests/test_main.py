from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction_rate():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


@pytest.mark.parametrize(
    "rate_example", [0, 5, 9.4]
)
def test_should_check_action_if_predict_rate_more_than_5_lower(
        mocked_prediction_rate, rate_example
):
    mocked_prediction_rate.return_value = rate_example
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "rate_example", [9.5, 10, 10.5]
)
def test_should_check_action_if_rate_between_5_higher_and_5_lower(
        mocked_prediction_rate, rate_example
):
    mocked_prediction_rate.return_value = rate_example
    assert cryptocurrency_action(10) == "Do nothing"


@pytest.mark.parametrize(
    "rate_example", [10.6, 50, 1000]
)
def test_should_check_action_if_predict_rate_more_than_5_higher(
        mocked_prediction_rate, rate_example
):
    mocked_prediction_rate.return_value = rate_example
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
