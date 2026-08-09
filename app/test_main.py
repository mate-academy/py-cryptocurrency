import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "number, result",
    [
        (50, "Sell all your cryptocurrency"),
        (200, "Buy more cryptocurrency"),
        (101, "Do nothing"),
        (105, "Do nothing"),
        (95, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        mock_prediction: callable,
        number: int, result: int
) -> None:
    mock_prediction.return_value = number
    func_return = cryptocurrency_action(100)
    assert func_return == result
