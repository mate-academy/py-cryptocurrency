import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate,result",
    [
        (105, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
        (106, "Buy more cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_advice(mock_exchange_rate_prediction: mock.MagicMock,
                    exchange_rate: int, result: str) -> None:
    mock_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(100) == result
