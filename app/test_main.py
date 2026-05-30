from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_small_price_difference(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(3.13) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_price_will_go_down(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(3.5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_price_will_go_up(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(2.5) == "Buy more cryptocurrency"
