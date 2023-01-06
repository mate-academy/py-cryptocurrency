from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def creating_mocked_prediction() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        yield mocked_prediction


@pytest.mark.parametrize(
    "prediction_rate, current_rate, message",
    [
        (1, 2, "Sell all your cryptocurrency"),
        (1, 1.1, "Sell all your cryptocurrency"),
        (1.1, 1, "Buy more cryptocurrency"),
        (1.1, 1.03, "Buy more cryptocurrency"),
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing")

    ]
)
def test_return_correct_message(
        creating_mocked_prediction: callable,
        prediction_rate: int | float,
        current_rate: int | float,
        message: str
) -> None:
    creating_mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == message
