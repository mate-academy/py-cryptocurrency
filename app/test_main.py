from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_buy_more(
        mock_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 150
    mock_get_exchange_rate_prediction.assert_called_with(50)
    assert mock_get_exchange_rate_prediction.return_value == 150


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_sell(
        mock_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mock_get_exchange_rate_prediction.assert_called_with(200)
    assert mock_get_exchange_rate_prediction.return_value == 80


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_do_nothing(
        mock_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    mock_get_exchange_rate_prediction.assert_called_with(100)
    assert mock_get_exchange_rate_prediction.return_value == 105
