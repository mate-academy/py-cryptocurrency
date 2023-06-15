from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.Mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
