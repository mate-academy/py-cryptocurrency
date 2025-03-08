from pytest_mock import MockerFixture
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=1.06)
    current_rate = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=0.94)
    current_rate = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_do_nothing(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
    current_rate = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"

    mocker.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
    current_rate = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
