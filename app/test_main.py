from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mocked_rate_prediction: mock.Mock
) -> None:
    mocked_rate_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency(
        mocked_rate_prediction: mock.Mock
) -> None:
    mocked_rate_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
        mocked_rate_prediction: mock.Mock
) -> None:
    mocked_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency2(
        mocked_rate_prediction: mock.Mock
) -> None:
    mocked_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
