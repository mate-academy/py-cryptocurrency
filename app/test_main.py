import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "price,prediction,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate(mocked_exchange: object,
                       price: int,
                       prediction: int,
                       expected: str
                       ) -> None:
    mocked_exchange.return_value = prediction
    assert cryptocurrency_action(price) == expected
