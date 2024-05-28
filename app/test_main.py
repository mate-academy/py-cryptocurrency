from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: object
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 106  # More than 5% higher
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_get_exchange_rate_prediction: object
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 94  # More than 5% lower
    assert (cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency")


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction: object) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 102  # Within 5%
    assert cryptocurrency_action(current_rate) == "Do nothing"

    mock_get_exchange_rate_prediction.return_value = 98  # Within 5%
    assert cryptocurrency_action(current_rate) == "Do nothing"

    mock_get_exchange_rate_prediction.return_value = 105  # Exactly 5% higher
    assert cryptocurrency_action(current_rate) == "Do nothing"

    mock_get_exchange_rate_prediction.return_value = 95  # Exactly 5% lower
    assert cryptocurrency_action(current_rate) == "Do nothing"
