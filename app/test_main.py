import pytest

from unittest import mock
from app.main import get_exchange_rate_prediction, cryptocurrency_action


def test_get_exchange_rate_prediction_returns_float() -> None:
    assert (
        isinstance(get_exchange_rate_prediction(120), float)
    )


def test_get_exchange_rate_prediction_takes_only_numeric() -> None:
    with pytest.raises(TypeError):
        get_exchange_rate_prediction("120")


@pytest.mark.parametrize(
    "current,prediction,expected",
    [
        pytest.param(
            100,
            95,
            "Do nothing",
            id="prediction_rate / current_rate == 0.95"),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="prediction_rate / current_rate == 1.05"),
        pytest.param(
            50,
            100,
            "Buy more cryptocurrency",
            id="prediction_rate / current_rate > 1.05"),
        pytest.param(
            150,
            100,
            "Sell all your cryptocurrency",
            id="prediction_rate / current_rate < 0.95"),
        pytest.param(
            98,
            100,
            "Do nothing",
            id="prediction_rate / current_rate == 1.02"),
    ]
)
def test_cryptocurrency_action_returns_correct_values_depending_on_price(
        current: int,
        prediction: int,
        expected: int) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_exchange_rate:
        mocked_exchange_rate.return_value = prediction
        assert (cryptocurrency_action(current) == expected)
