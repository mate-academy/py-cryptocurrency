import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "prediction_rate, desired_result",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        prediction_rate: int | float,
        desired_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(1) == desired_result
