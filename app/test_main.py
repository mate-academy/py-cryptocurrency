from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction() -> mock.Mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_function:
        yield mock_function


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected_action",
    [
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.Mock,
        predicted_rate: int | float,
        current_rate: int | float,
        expected_action: str | float,
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    assert cryptocurrency_action(current_rate) == expected_action
