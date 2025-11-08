import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected",
    [
        (0.67, "Sell all your cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1, "Do nothing"),
        (1.05, "Do nothing"),
        (1.06, "Buy more cryptocurrency"),
        (2, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(prediction: int, expected: int) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction):
        result = cryptocurrency_action(1)
        assert result == expected
