from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        yield mock_prediction


def test_should_recommend_buy_when_growth_predicted(mocked_prediction):
    mocked_prediction.return_value = 15
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Buy more cryptocurrency"


def test_should_recommend_sell_when_drop_predicted(mocked_prediction):
    mocked_prediction.return_value = 7
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Sell all your cryptocurrency"


def test_should_recommend_do_nothing_when_rate_is_on_higher_border(mocked_prediction):
    mocked_prediction.return_value = 10.5
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Do nothing"


def test_should_recommend_do_nothing_when_rate_is_on_lower_border(mocked_prediction):
    mocked_prediction.return_value = 9.5
    recommendation = cryptocurrency_action(10)
    assert recommendation == "Do nothing"
