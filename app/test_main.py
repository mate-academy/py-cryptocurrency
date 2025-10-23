from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.06)
def test_return_buy_when_persent_bigger(
        mock_prediction: mock.MagicMock
) -> None:
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_return_do_nothing_when_persent_is_1_05(
        mock_prediction: mock.MagicMock
) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_return_do_nothing_when_persent_is_0_95(
        mock_prediction: mock.MagicMock
) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.8)
def test_return_sell_when_persent_lower(
        mock_prediction: mock.MagicMock
) -> None:
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
