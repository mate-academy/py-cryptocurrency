import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange():
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_test_exchange:
        yield mock_test_exchange


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(
            1, 1.06, "Buy more cryptocurrency",
            id="Should return 'Buy more cryptocurrency'"
               " if difference > +5%"
        ),
        pytest.param(
            1, 0.94, "Sell all your cryptocurrency",
            id="Should return 'Sell all your cryptocurrency'"
               " if difference < -5%"
        ),
        pytest.param(
            1, 1, "Do nothing",
            id="Should return 'Do nothing' if rates are equal"
        ),
        pytest.param(
            1, 1.05, "Do nothing",
            id="Should return 'Do nothing' if difference < +5%"
        ),
        pytest.param(
            1, 0.95, "Do nothing",
            id="Should return 'Do nothing' if difference < -5%"
        ),
    ]
)
def test_cryptocurrency_action(
        mocked_exchange,
        current_rate,
        prediction_rate,
        expected
):
    mocked_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
