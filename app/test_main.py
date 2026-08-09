import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected",
    [
        (1050, 1000, "Do nothing"),
        (1150, 1000, "Buy more cryptocurrency"),
        (900, 1000, "Sell all your cryptocurrency"),
        (950, 1000, "Do nothing"),
        (1051, 1000, "Buy more cryptocurrency"),
        (949, 1000, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(prediction_rate: float,
                               current_rate: float,
                               expected: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        result = cryptocurrency_action(current_rate)
        assert result == expected
