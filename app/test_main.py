from typing import Union
import pytest
from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, exchange_rate, result", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 104.5, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 95.5, "Do nothing"),
    (100, 100, "Do nothing"),
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mock_get_exchange_rate_prediction: Union[int, float],
        current_rate: Union[int, float],
        exchange_rate: Union[int, float],
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    expected = cryptocurrency_action(current_rate)
    assert expected == result
