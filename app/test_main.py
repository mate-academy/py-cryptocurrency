from unittest import mock
from unittest.mock import Mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency(mock_action: Mock) -> None:
    mock_action.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
    mock_action.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
    mock_action.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
    mock_action.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
