import pytest
from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (100, 120, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: float,
        prediction_rate: float,
        expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
