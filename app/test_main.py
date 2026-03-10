from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("prediction_to_current, action", [
    (1.06, "Buy more cryptocurrency"),
    (1.05, "Do nothing"),
    (1.00, "Do nothing"),
    (0.95, "Do nothing"),
    (0.94, "Sell all your cryptocurrency")
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        prediction_to_current: float,
        action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_to_current
    assert cryptocurrency_action(1) == action
