import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predict_rate,action",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 20, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_rate_prediction: mock.MagicMock,
        current_rate: int,
        predict_rate: int,
        action: str
) -> None:
    mock_exchange_rate_prediction.return_value = predict_rate
    assert cryptocurrency_action(current_rate) == action
