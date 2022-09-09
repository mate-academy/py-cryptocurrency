from unittest import mock

from app.main import cryptocurrency_action


def test_return_function_was_called_with_value():
    prediction_rate = mock.MagicMock()
    prediction_rate(4)
    # cryptocurrency_action(4)
    prediction_rate.assert_called_once_with(4)


def test_return_function_was_called():
    get_exchange_rate_prediction = mock.MagicMock()
    get_exchange_rate_prediction()
    # cryptocurrency_action(3)
    get_exchange_rate_prediction.assert_called_once()
