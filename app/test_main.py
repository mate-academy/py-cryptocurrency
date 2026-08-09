import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current_rate, expected_result",
    [
        (110.0, 100.0, "Buy more cryptocurrency"),
        (105.0, 100.0, "Do nothing"),
        (90.0, 100.0, "Sell all your cryptocurrency"),
        (95.0, 100.0, "Do nothing"),
        (102.5, 100.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_various_conditions(
        mocked_action: MagicMock,
        prediction: float,
        current_rate: float,
        expected_result: str) -> None:
    mocked_action.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
    mocked_action.assert_called_once_with(current_rate)
