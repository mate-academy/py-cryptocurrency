from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=2.0)
def test_prediction_rate_bigger(mock_rate_prediction: float) -> None:
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.0)
def test_prediction_rate_smaller(mock_rate_prediction: float) -> None:
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_prediction_rate_big_5_percent(mock_rate_prediction: float) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_prediction_rate_small_5_percent(mock_rate_prediction: float) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.0)
def test_prediction_rate_equal(mock_rate_prediction: float) -> None:
    assert cryptocurrency_action(1) == "Do nothing"
