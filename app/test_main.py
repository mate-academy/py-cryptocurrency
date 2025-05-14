from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def  test_buy_more(most_get_product: Mock) -> None:
    most_get_product.return_value = 105
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(most_get_product: Mock) -> None:
    most_get_product.return_value = 95
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_noting(most_get_product: Mock) -> None:
    most_get_product.return_value = 104
    assert cryptocurrency_action(100) == "Do nothing"
