from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more_cryptocurrency(mock_get: int) -> None:
    mock_get.return_value = 300
    assert cryptocurrency_action(200) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all_your_cryptocurrency(mock_get: int) -> None:
    mock_get.return_value = 100
    assert cryptocurrency_action(600) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_when_95(mock_get: int) -> None:
    mock_get.return_value = 190
    assert cryptocurrency_action(200) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_when_105(mock_get: int) -> None:
    mock_get.return_value = 210
    assert cryptocurrency_action(200) == "Do nothing"


def test_should_raise_error_if_current_rate_is_str() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("58")
