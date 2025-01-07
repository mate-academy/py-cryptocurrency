import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,prediction",
    [
        (50, 52.6, "Buy more cryptocurrency"),
        (50, 52.5, "Do nothing"),
        (50, 47.4, "Sell all your cryptocurrency"),
        (50, 47.5, "Do nothing"),
        (50, 49, "Do nothing"),
        (100, 300, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 11, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 103, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_exchange_rate_prediction: mock.MagicMock,
                               current_rate: int,
                               prediction_rate: float,
                               prediction: str
                               ) -> None:
    mock_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == prediction
