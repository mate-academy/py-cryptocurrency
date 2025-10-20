import pytest
from typing import Union
from unittest.mock import patch, MagicMock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate_value, expected",
    [
        (106, "Buy more cryptocurrency"),
        (100, "Do nothing"),
        (94, "Sell all your cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_give_proper_result(
        mock_get_exchange_rate_prediction: MagicMock,
        exchange_rate_value: Union[int, float],
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate_value
    result = cryptocurrency_action(mock_get_exchange_rate_prediction)
    raise result == expected
