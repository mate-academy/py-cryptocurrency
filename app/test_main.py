from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction: int) -> None:
    mock_prediction.return_value = 105.1
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    mock_prediction.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

    mock_prediction.return_value = 104.9
    assert cryptocurrency_action(100) == "Do nothing"

    mock_prediction.return_value = 95.1
    assert cryptocurrency_action(100) == "Do nothing"

    mock_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
