from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: any) -> None:
    test_cases = [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 100.1, "Do nothing"),
    ]

    for current_rate, predicted_rate, expected_action in test_cases:

        mock_get_exchange_rate_prediction.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)

        assert result == expected_action

        mock_get_exchange_rate_prediction.assert_called_with(current_rate)
