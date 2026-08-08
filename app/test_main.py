import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "curr_rate, pred_rate, expected",
    [
        (1, 1, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 2.74, "Buy more cryptocurrency"),
        (2, 1.03, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        curr_rate: int | float,
        pred_rate: int | float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = pred_rate
        assert cryptocurrency_action(curr_rate) == expected
