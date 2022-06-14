from app.main import cryptocurrency_action

from unittest import mock
import pytest


@pytest.mark.parametrize("exchange_rate, current_rate, result",
                         [
                             pytest.param(10, 5,
                                          "Buy more cryptocurrency"),
                             pytest.param(5, 10,
                                          "Sell all your cryptocurrency"),
                             pytest.param(99.75, 95,
                                          "Do nothing"),
                             pytest.param(95, 100,
                                          "Do nothing"),
                         ]
                         )
@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_we_bye_more(mocked_exchange_func, exchange_rate,
                          current_rate, result):
    mocked_exchange_func.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == result
