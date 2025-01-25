from typing import Union
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction: Union[int, float]) -> None:
    mock_prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"

    mock_prediction.return_value = 20
    assert cryptocurrency_action(30) == "Sell all your cryptocurrency"

    mock_prediction.return_value = 50
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"

    mock_prediction.return_value = 8.4
    assert cryptocurrency_action(8) == "Do nothing"

    mock_prediction.return_value = 3.8
    assert cryptocurrency_action(4) == "Do nothing"
