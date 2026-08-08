import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_func():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        yield mocked_func


@pytest.mark.parametrize("current_rate,prediction_rate,expected",
                         [
                             (1, 1, "Do nothing"),
                             (1, 0.4, "Sell all your cryptocurrency"),
                             (1, 1.5, "Buy more cryptocurrency"),
                             (1, 0.95, "Do nothing"),
                             (1, 1.05, "Do nothing")
                         ]
                         )
def test_cryptocurrency_action(mocked_func,
                               current_rate,
                               prediction_rate,
                               expected):
    mocked_func.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
