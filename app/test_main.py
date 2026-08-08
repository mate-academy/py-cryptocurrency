from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(get_exchange_rate_prediction: any) -> None:
    get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"

    get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"

    get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    get_exchange_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
