import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, expected_rate, expected_result",
    [
        [1, 1.06, "Buy more cryptocurrency"],
        [1, 0.94, "Sell all your cryptocurrency"],
        [1, 1, "Do nothing"],
        [1, 1.05, "Do nothing"],
        [1, 0.95, "Do nothing"]
    ],
    ids=[
        """Should return "Buy more cryptocurrency", if profit > 5%""",
        """Should return "Sell all your cryptocurrency", if loss > 5%""",
        """Should return "Do nothing", if profit = 0%""",
        """Should return "Do nothing", if profit < 5%""",
        """Should return "Do nothing", if loss < 5%""",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_correct_prediction(
        mock_get_exchange_rate_prediction: callable,
        expected_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = expected_rate
    assert cryptocurrency_action(current_rate) == expected_result
