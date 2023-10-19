from unittest import mock
import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_predicted_exchange_rate_much_less_than_current(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 110
    assert cryptocurrency_action(132) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_predicted_exchange_rate_much_bigger_than_current(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 105.3
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_predicted_exchange_rate_little_less_than_current(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 1050
    assert cryptocurrency_action(1000) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_predicted_exchange_rate_little_bigger_than_current(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_predicted_exchange_rate_equal_current(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_error_when_current_rate_zero(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 0
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
