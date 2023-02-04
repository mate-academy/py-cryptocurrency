from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_response_nothing(mocked_get_predict: float) -> None:
    mocked_get_predict.return_value = 10.5
    assert cryptocurrency_action(10.5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_response_sell(mocked_get_predict: float) -> None:
    mocked_get_predict.return_value = 7.1
    assert cryptocurrency_action(10.5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_response_buy(mocked_get_predict: float) -> None:
    mocked_get_predict.return_value = 12
    assert cryptocurrency_action(10.5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_response_sell_if_predict_105(
        mocked_get_predict: float
) -> None:
    mocked_get_predict.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_response_sell_if_predict_095(
        mocked_get_predict: float
) -> None:
    mocked_get_predict.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
