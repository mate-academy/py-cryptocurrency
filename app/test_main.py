import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        pytest.param(
            1, 1.7,
            "Buy more cryptocurrency",
            id="Buy more cryptocurrency"),
        pytest.param(
            1, 0.92,
            "Sell all your cryptocurrency",
            id="Sell all your cryptocurrency"),
        pytest.param(
            1, 1.02,
            "Do nothing",
            id="Do nothing"),
        pytest.param(
            1, 0.95,
            "Do nothing",
            id="Do nothing"),
        pytest.param(
            1, 1.05,
            "Do nothing",
            id="Do nothing when ")
    ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str) -> None:

    mocked_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected
