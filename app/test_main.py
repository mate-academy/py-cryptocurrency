from unittest import mock
from app.main import cryptocurrency_action
import pytest

@pytest.mark.parametrize(
    "prediction_rate,expected",
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_prediction: mock.MagicMock,
    prediction_rate: float,
    expected: str,
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(100) == expected
