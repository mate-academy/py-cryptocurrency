import pytest
from unittest.mock import patch
from typing import Union
import app.main


@pytest.mark.parametrize(
    "current_rate,mock_return_value,result",
    [
        (1.1, 2, "Buy more cryptocurrency"),
        (2, 2.1, "Do nothing"),
        (2, 1.9, "Do nothing"),
        (5.1, 2, "Sell all your cryptocurrency")
    ],
    ids=[
        "Buy more cryptocurrency when rate 1.05 or more",
        "Do nothing when rate less 1.05",
        "Do nothing when rate more 0.95",
        "Sell all your cryptocurrency when rate 0.95 or less"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_function_has_been_called(mock: callable,
                                  current_rate: Union[int, float],
                                  mock_return_value: Union[int, float],
                                  result: str) -> None:
    mock.return_value = mock_return_value
    assert app.main.cryptocurrency_action(current_rate) == result
