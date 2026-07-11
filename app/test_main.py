from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_to_buy(mocked_predict: mock.MagicMock) -> None:
    mocked_predict.return_value = 106.0
    result = cryptocurrency_action(100.0)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_to_sell(mocked_predict: mock.MagicMock) -> None:
    mocked_predict.return_value = 94.0
    result = cryptocurrency_action(100.0)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing(mocked_predict: mock.MagicMock) -> None:
    mocked_predict.return_value = 102.0
    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"
    mocked_predict.return_value = 105.0
    assert cryptocurrency_action(100.0) == "Do nothing"
    mocked_predict.return_value = 95.0
    assert cryptocurrency_action(100.0) == "Do nothing"
