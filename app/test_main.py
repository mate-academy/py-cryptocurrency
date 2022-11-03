from app.main import cryptocurrency_action

from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_crypto_nothing_big(mock_prediction: mock) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_crypto_nothing_small(mock_prediction: mock) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
