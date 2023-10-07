from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: float
) -> None:
    test_data = [
        [105.1, "Buy more cryptocurrency"],
        [94, "Sell all your cryptocurrency"],
        [105, "Do nothing"],
        [95, "Do nothing"],
        [102, "Do nothing"]
    ]
    for (
        mock_get_exchange_rate_prediction.return_value,
        expected_result
    ) in test_data:

        assert cryptocurrency_action(100) == expected_result
