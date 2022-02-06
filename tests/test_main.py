import pytest
from unittest import mock


from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction():
    with mock.patch('app.main.get_exchange_rate_prediction') as mocked:
        yield mocked


@pytest.mark.parametrize(
    'current_rate, exchange_rate_prediction, awaited_result',
    [
        pytest.param(
            1.0,
            1.1,
            "Buy more cryptocurrency",
            id="Test when rate is more than +0.05"
        ),
        pytest.param(
            1.0,
            0.9,
            'Sell all your cryptocurrency',
            id="Test when next rate lower than -0.05"
        ),
        pytest.param(
            1.0,
            1.01,
            'Do nothing',
            id='Test when next rate in between 0 and +0.05'
        ),
        pytest.param(
            1.0,
            0.97,
            "Do nothing",
            id='Test when next rate in between -0.05 and 0'
        )
    ],
)
def test_cryptocurrency(
        mocked_get_exchange_rate_prediction,
        exchange_rate_prediction,
        current_rate,
        awaited_result,
):
    mocked_get_exchange_rate_prediction.return_value = exchange_rate_prediction

    assert cryptocurrency_action(current_rate) == awaited_result
