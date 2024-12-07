from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: mock.Mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 120.5
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"
    mock_get_exchange_rate_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_exactly_105_do_nothing(
        mock_get_exchange_rate_prediction: mock.Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_exactly_95_do_nothing(
        mock_get_exchange_rate_prediction: mock.Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_nothing_if_minus_five(
        mock_get_exchange_rate_prediction: mock.Mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 97.66
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
    mock_get_exchange_rate_prediction.assert_called_once()
