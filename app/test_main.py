from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_called_func_once(rate_prediction: mock.MagicMock) -> None:
    rate_prediction.return_value = 1.02
    cryptocurrency_action(2.0)
    rate_prediction.assert_called_once_with(2.0)


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,prediction,result",
    [
        (80, 85, "Buy more cryptocurrency"),
        (80, 50, "Sell all your cryptocurrency"),
        (80, 79, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
def test_correct_crypto_prediction(
        rate_prediction: mock.MagicMock,
        current_rate: int,
        prediction: int,
        result: str
) -> None:
    rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == result
