from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_prediction:
        yield mock_prediction


def test_should_tell_buy_when_growth_predicted(mock_prediction):
    mock_prediction.return_value = 15
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Buy more cryptocurrency"


def test_should_tell_sell_when_drop_predicted(mock_prediction):
    mock_prediction.return_value = 7
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Sell all your cryptocurrency"


def test_should_tell_do_nothing_when_rate_is_higher_border(mock_prediction):
    mock_prediction.return_value = 10.5
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Do nothing"


def test_should_tell_do_nothing_when_rate_is_on_lower_border(mock_prediction):
    mock_prediction.return_value = 9.5
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Do nothing"
