import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "prediction, current, action",
    [
        (110, 100, "Buy more cryptocurrency"),
        (80, 100, "Sell all your cryptocurrency"),
        (103, 100, "Do nothing"),
        (99, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
    ],
)
def test_crypto_currency_action(
    prediction: int | float, current: int | float, action: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction"
                    ) as get_exchange_rate_prediction:
        get_exchange_rate_prediction.return_value = prediction
        assert cryptocurrency_action(current) == action
