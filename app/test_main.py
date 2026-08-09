from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_exchange_rate_is_higher(
    prediction_rate: mock.MagicMock
) -> None:
    prediction_rate.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_exchange_rate_is_lower(
    prediction_rate: mock.MagicMock
) -> None:
    prediction_rate.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_exchange_rate_has_small_difference(
    prediction_rate: mock.MagicMock
) -> None:
    prediction_rate.return_value = 1.02
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_105_predicted_exchange_rate_do_noting(
    prediction_rate: mock.MagicMock
) -> None:
    prediction_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_95_predicted_exchange_rate_do_noting(
    prediction_rate: mock.MagicMock
) -> None:
    prediction_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
