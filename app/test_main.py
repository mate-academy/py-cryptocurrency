from unittest import mock
from app.main import cryptocurrency_action


def test_buy_more_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as gerp:
        gerp.return_value = 110  # 10% більше від 100
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as gerp:
        gerp.return_value = 90  # 10% менше від 100
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as gerp:
        gerp.return_value = 100  # без зміни
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_boundary_conditions_buy() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as gerp:
        gerp.return_value = 105  # рівно 5% більше
        result = cryptocurrency_action(100)
        assert result == "Do nothing"  # Не купуємо


def test_boundary_conditions_sell() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as gerp:
        gerp.return_value = 95  # рівно 5% менше
        result = cryptocurrency_action(100)
        assert result == "Do nothing"  # Не продаємо
