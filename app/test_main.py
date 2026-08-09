from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_value,predict_value,expected",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 0.89, "Sell all your cryptocurrency"),
        (1.0, 0.95, "Do nothing"),
        (1.0, 1.05, "Do nothing"),
    ],
)
def test_funk_cryptocurrency_action(
        current_value: float,
        predict_value: float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_val:
        mock_val.return_value = predict_value
        assert cryptocurrency_action(current_value) == expected
