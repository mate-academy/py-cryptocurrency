import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected",
    [
        (67, "Sell all your cryptocurrency"),
        (1, "Sell all your cryptocurrency"),
        (100, "Do nothing"),
        (101, "Do nothing"),
        (96, "Do nothing"),
        (106, "Buy more cryptocurrency"),
        (222, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(prediction: int, expected: int) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=prediction):
        result = cryptocurrency_action(100)
        assert result == expected