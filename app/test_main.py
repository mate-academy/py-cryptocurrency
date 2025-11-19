from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_buying(
        get_exchange_rate_prediction: MagicMock
) -> None:
    get_exchange_rate_prediction.return_value = 1.78
    assert cryptocurrency_action(1.01) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_selling(
        get_exchange_rate_prediction: MagicMock
) -> None:
    get_exchange_rate_prediction.return_value = 0.74
    assert cryptocurrency_action(1.01) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_do_nothing(
        get_exchange_rate_prediction: MagicMock
) -> None:
    get_exchange_rate_prediction.return_value = 0.98
    assert cryptocurrency_action(0.99) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_do_nothing_on_edge_up(
        get_exchange_rate_prediction: MagicMock
) -> None:
    get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1.00) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_do_nothing_on_edge_down(
        get_exchange_rate_prediction: MagicMock
) -> None:
    get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1.00) == "Do nothing"
