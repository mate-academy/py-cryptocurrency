import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, value",
    [
        (1.00, 1.06, "Buy more cryptocurrency"),
        (1.00, 1.05, "Do nothing"),
        (1.05, 1.00, "Do nothing"),
        (1.01, 1.00, "Do nothing"),
        (1.00, 0.95, "Do nothing"),
        (1.00, 0.75, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: float,
        prediction_rate: float,
        value: str
) -> None:

    mock_get_exchange_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)

    assert result == value
