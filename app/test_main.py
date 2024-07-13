import pytest
from unittest import mock
from typing import Union


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "value_exchange, result",
    [
        (94, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing"),
        (106, "Buy more cryptocurrency")
    ], ids=["<95", ">=95", "<106", ">=106"]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange: object, value_exchange: Union[int, float], result: str
) -> None:
    mock_exchange.return_value = value_exchange
    assert cryptocurrency_action(100) == result
