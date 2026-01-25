from unittest.mock import Mock
from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(rate_prediction: Mock) -> None:
    current_rate = [
        (105, "Buy more cryptocurrency"),
        (95, "Sell all your cryptocurrency"),
        (100, "Do nothing")
    ]

    for predicted_rate, expected in current_rate:
        rate_prediction.return_value = predicted_rate
        result = cryptocurrency_action(100)
        assert result == expected
