from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_of_100(mocked_get_exchange):
    mocked_get_exchange.return_value = 1040

    cryptocurrency_action(1000)

    mocked_get_exchange.assert_called_once()
