from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_has_been_called(
        m_get_exchange_rate_prediction: object
) -> None:
    m_get_exchange_rate_prediction.return_value = 70
    cryptocurrency_action(10)
    m_get_exchange_rate_prediction.assert_called_once_with(10)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_on_buy_more(
        m_get_exchange_rate_prediction: object
) -> None:
    m_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_on_sell_all(
        m_get_exchange_rate_prediction: object
) -> None:
    m_get_exchange_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_on_do_nothing_min_value(
        m_get_exchange_rate_prediction: object
) -> None:
    m_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_on_do_nothing_max_value(
        m_get_exchange_rate_prediction: object
) -> None:
    m_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
