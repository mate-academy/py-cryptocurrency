import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "expected_prediction,expected_rate,expected_result",
    [
        (0.94, 1, "Sell all your cryptocurrency"),
        (1.90, 2, "Do nothing"),
        (5.25, 5, "Do nothing"),
        (0.53, 0.5, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_correct_string(
        mocked_prediction: mock.MagicMock,
        expected_prediction: int | float,
        expected_rate: int | float,
        expected_result: str
) -> None:
    mocked_prediction.return_value = expected_prediction
    assert cryptocurrency_action(expected_rate) == expected_result
