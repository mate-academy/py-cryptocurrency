import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predict_rate, decision",
    [
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.7, "Sell all your cryptocurrency"),
        (1, 1.2, "Buy more cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: int | float,
        predict_rate: float,
        decision: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predict_rate

    assert cryptocurrency_action(current_rate) == decision
