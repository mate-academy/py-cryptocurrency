import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize("current_rate, prediction_rate, expected", [
    (100, 105.1, "Buy more cryptocurrency"),
    (100, 94.9, "Sell all your cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 101, "Do nothing"),
])
def test_cryptocurrency_predictions(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: Union[int | float],
        prediction_rate: Union[int | float],
        expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
