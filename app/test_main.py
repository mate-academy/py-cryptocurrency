import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_advice",
    [
        (1000, 1000.0, "Do nothing"),
        (1000, 1050.0 , "Do nothing"),
        (1000, 950.0, "Do nothing"),
        (1000, 1051.0, "Buy more cryptocurrency"),
        (1000, 949.0, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate_prediction: mock.MagicMock,
        current_rate: int,
        prediction_rate: float,
        expected_advice: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_advice
