from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_slightly_bigger_price(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(3.15789) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_slightly_lower_price(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(2.85715) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_same_price(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(3) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_price_will_go_down(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(3.5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_price_will_go_up(price_prediction: mock.MagicMock) -> None:
    price_prediction.return_value = 3
    assert cryptocurrency_action(2.4) == "Buy more cryptocurrency"
