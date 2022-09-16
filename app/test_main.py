from unittest import mock

import pytest

from app.main import cryptocurrency_action  # , get_exchange_rate_prediction


@pytest.fixture()
def mocked_rate():
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=20) as f:
        yield f


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=20)
def test_should_return_sell_all_crypto(mocked_rate):
    assert cryptocurrency_action(30) == "Sell all your cryptocurrency"


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=20)
def test_should_return_buy_more_crypto(mocked_rate):
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=20)
def test_should_return_do_nothing(mocked_rate):
    assert cryptocurrency_action(20) == "Do nothing"


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=20)
def test_should_raise_zero_division(mocked_rate):
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=20)
def test_should_raise_type_error(mocked_rate):
    with pytest.raises(TypeError):
        cryptocurrency_action("One")


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=20)
def test_get_rate_should_called_once(mocked_rate):
    cryptocurrency_action(20)
    mocked_rate.assert_called_once()


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_five_percent_hither(mocked_rate):
    mocked_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


# @mock.patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_five_percent_lower(mocked_rate):
    mocked_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
