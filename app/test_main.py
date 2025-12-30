from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    rate = 1
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(rate) == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(rate) == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(rate) == "Buy more cryptocurrency"
    mock_get_exchange_rate_prediction.return_value = 0.94
    assert (cryptocurrency_action(rate) == "Sell all your cryptocurrency")
