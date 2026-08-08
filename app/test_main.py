import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, result",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction_rate: mock.MagicMock,
        prediction_rate: int | float,
        result: str
) -> None:
    mock_prediction_rate.return_value = prediction_rate
    assert cryptocurrency_action(1) == result
