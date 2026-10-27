from unittest import mock
from unittest.mock import MagicMock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "value,result",
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_it_more_than_5(mock_prediction: MagicMock,
                                                 value: int,
                                                 result: str) -> None:
    mock_prediction.return_value = value
    assert cryptocurrency_action(100) == result
