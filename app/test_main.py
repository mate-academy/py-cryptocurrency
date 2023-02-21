import app.main
import pytest
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto(mock_get_exchange_rate_prediction: object) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert app.main.cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_sell_crypto(mock_get_exchange_rate_prediction: object) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94
    assert app.main.cryptocurrency_action(1) == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "current_rate,predicted_rate",
    [
        (1, 1.01),
        (1, 1.05),
        (1, 0.95),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_crypto(
        mock_get_exchange_rate_prediction: object,
        current_rate: int,
        predicted_rate: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert app.main.cryptocurrency_action(current_rate) == "Do nothing"
