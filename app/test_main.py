from app.main import cryptocurrency_action


def test_cryptocurrency_action(mocker: callable) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=0.95)
    assert cryptocurrency_action(1) == "Do nothing"
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=1.05)
    assert cryptocurrency_action(1) == "Do nothing"
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=1)
    assert cryptocurrency_action(1) == "Do nothing"
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=1.06)
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=0.94)
    assert cryptocurrency_action(1) == \
           "Sell all your cryptocurrency"
