from unittest.mock import patch, Mock

import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_should_call_get_exchange_rate_prediction(
        mocked_exchange_rate_prediction: Mock
) -> None:
    mocked_exchange_rate_prediction.return_value = 1
    cryptocurrency_action(1.5)
    mocked_exchange_rate_prediction.assert_called_with(1.5)


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        (1, 2, "Buy more cryptocurrency"),
        (0.66, 0.96, "Buy more cryptocurrency"),
        (-150, -167.7, "Buy more cryptocurrency"),
        (0.1, 0.09, "Sell all your cryptocurrency"),
        (-5, -1.65, "Sell all your cryptocurrency"),
        (1000, 770, "Sell all your cryptocurrency"),
        (-3.3, -3.25, "Do nothing"),
        (43, 41.75, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (30, 31.5, "Do nothing")
    ]
)
def test_should_return_correct_statement(
    mocked_exchange_rate_prediction: Mock,
    current_rate: int,
    prediction_rate: int,
    expected_result: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
