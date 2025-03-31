import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current, result",
    [
        (110, 100, "Buy more cryptocurrency"),
        (90, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ]
)
def test_crypto_action(prediction: int | float,
                       current: int | float,
                       result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction):
        assert cryptocurrency_action(current) == result
