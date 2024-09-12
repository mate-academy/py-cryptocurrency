import pytest
from unittest import mock

from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
