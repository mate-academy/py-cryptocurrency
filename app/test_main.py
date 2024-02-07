import pytest
from unittest import mock
from unittest.mock import patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected_action",
    [
        (100.01, "Buy more cryptocurrency"),
        (10.01, "Sell all your cryptocurrency"),
        (51, "Do nothing"),
        (47.5, "Do nothing"),
        (52.5, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock,
        predicted_rate: Union[int, float],
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    assert cryptocurrency_action(current_rate=50.00) == expected_action
