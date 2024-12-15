from typing import Union
import pytest
from unittest.mock import patch


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        pytest.param(10, 9, "Sell all your cryptocurrency",
                     id="should return 'Sell all' for rate less "
                        "than 0.95 and integer values entered"),
        pytest.param(1, 0.94, "Sell all your cryptocurrency",
                     id="should return 'Sell all' for rate less "
                        "than 0.95 and float values entered"),
        pytest.param(1000, 1050, "Do nothing",
                     id="should return 'Do nothing' for rate less 1.05 and "
                        "more than 0.95 and integer values entered"),
        pytest.param(1, 0.95, "Do nothing",
                     id="should return 'Do nothing' for rate less 1.05 and "
                        "more than 0.95 and float values entered"),
        pytest.param(100, 106, "Buy more cryptocurrency",
                     id="should return 'Buy more' for rate > 1.05 "
                        "and integer values entered"),
        pytest.param(0.99, 1.06, "Buy more cryptocurrency",
                     id="should return 'Buy more' for rate > 1.05 "
                        "and float values entered"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Union[int, float],
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
