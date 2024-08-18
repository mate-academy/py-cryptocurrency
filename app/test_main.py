from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predict_value,current_value,expected",
    [
        (1.06, 1.0, "Buy more cryptocurrency"),
        (0.89, 1.0, "Sell all your cryptocurrency"),
        (0.96, 1.0, "Do nothing"),
        (1.02, 1.0, "Do nothing"),
    ],
)
def test_funk_cryptocurrency_action(
        predict_value: float,
        current_value: float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_val:
        mock_val.return_value = predict_value
        assert cryptocurrency_action(current_value) == expected
