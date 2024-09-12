from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_(mocked_exchange_rate: callable) -> None:
    mocked_exchange_rate.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"

    mocked_exchange_rate.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

    mocked_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"

    mocked_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
