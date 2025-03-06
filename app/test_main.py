import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, result",
    [(1.1, 1.2, "Buy more cryptocurrency"),
     (1.2, 1.1, "Sell all your cryptocurrency"),
     (1.1, 1.1, "Do nothing")]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_activity(mocked_exchange_rate: mock.Mock,
                         current_rate: int | float,
                         prediction: int | float,
                         result: str) -> None:
    mocked_exchange_rate.return_value = prediction

    assert cryptocurrency_action(current_rate) == result
