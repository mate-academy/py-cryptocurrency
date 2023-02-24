from unittest.mock import patch

from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    # Case 1: Predicted exchange rate is 10% higher than current rate
    current_rate = 100
    predicted_rate = 110
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        action = cryptocurrency_action(current_rate)
        assert action == "Buy more cryptocurrency"

    # Case 2: Predicted exchange rate is 10% lower than current rate
    current_rate = 100
    predicted_rate = 90
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        action = cryptocurrency_action(current_rate)
        assert action == "Sell all your cryptocurrency"

    # Case 3: Predicted exchange rate is only 2% higher than current rate
    current_rate = 100
    predicted_rate = 102
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        action = cryptocurrency_action(current_rate)
        assert action == "Do nothing"

    # Case 4: Predicted exchange rate is only 2% lower than current rate
    current_rate = 100
    predicted_rate = 98
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        action = cryptocurrency_action(current_rate)
        assert action == "Do nothing"

    # Case 5: Predicted exchange rate is only 5% higher than current rate
    current_rate = 100
    predicted_rate = 105
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        action = cryptocurrency_action(current_rate)
        assert action == "Do nothing"

    # Case 6: Predicted exchange rate is only 5% lower than current rate
    current_rate = 100
    predicted_rate = 95
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        action = cryptocurrency_action(current_rate)
        assert action == "Do nothing"
