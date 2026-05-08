from unittest.mock import patch
import app.main as main


def test_buy_more() -> None:
    # prediction > 5% acima → compra
    with patch("app.main.get_exchange_rate_prediction", return_value=110):
        assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all() -> None:
    # prediction > 5% abaixo → vende
    with patch("app.main.get_exchange_rate_prediction", return_value=90):
        assert main.cryptocurrency_action(100) == (
            "Sell all your cryptocurrency"
        )


def test_do_nothing_above() -> None:
    # prediction exatamente 5% acima → não faz nada (precisa ser MAIS que 5%)
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert main.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_below() -> None:
    # prediction exatamente 5% abaixo → não faz nada
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert main.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_inside() -> None:
    # prediction dentro da faixa → não faz nada
    with patch("app.main.get_exchange_rate_prediction", return_value=100):
        assert main.cryptocurrency_action(100) == "Do nothing"
