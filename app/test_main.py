import pytest
from unittest import mock
from typing import Any
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_rate_prediction):
        yield mock_rate_prediction


def test_get_exchange_rate_predict_has_been_called(
        mocked_rate_prediction: Any
) -> None:
    mocked_rate_prediction.return_value = 100
    cryptocurrency_action(95)
    mocked_rate_prediction.assert_called_once_with(95)


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 70, "Sell all your cryptocurrency"),
        (100, 150, "Buy more cryptocurrency")
    ]
)
def test_cryptocurrency_action_result(
        mocked_rate_prediction: Any,
        current_rate: int,
        prediction_rate: int | float,
        expected_result: str) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
