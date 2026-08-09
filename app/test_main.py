import pytest

from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as exchange_rate:
        yield exchange_rate


@pytest.mark.parametrize(
    "predict_exchange, expected_message",
    [
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
        (0.98, "Do nothing"),
        (0.93, "Sell all your cryptocurrency"),
        (1.34, "Buy more cryptocurrency"),

    ]
)
def test_correct_action(
        mocked_get_exchange_rate_prediction: Callable,
        predict_exchange: float,
        expected_message: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predict_exchange
    assert cryptocurrency_action(1) == expected_message
