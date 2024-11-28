from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action(mocked_prediction: mock.Mock):
    cryptocurrency_action(5)
    mocked_prediction.assert_called()