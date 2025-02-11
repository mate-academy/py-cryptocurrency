from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_works_correctly(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 10.6
    assert (cryptocurrency_action(10) == "Buy more cryptocurrency")
    mock_get_exchange_rate_prediction.return_value = 9.4
    assert (cryptocurrency_action(10) == "Sell all your cryptocurrency")
    mock_get_exchange_rate_prediction.return_value = 10.5
    assert (cryptocurrency_action(10) == "Do nothing")
    mock_get_exchange_rate_prediction.return_value = 9.5
    assert (cryptocurrency_action(10) == "Do nothing")
