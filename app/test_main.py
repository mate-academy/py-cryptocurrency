import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [

        (1, 1.1, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (1, 1.04, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),

    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_get_exchange_rate_prediction
    ):
        mock_get_exchange_rate_prediction.return_value = prediction_rate

        assert cryptocurrency_action(current_rate) == expected
