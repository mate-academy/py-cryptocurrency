import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        pytest.param(
            100,
            95,
            "Do nothing",
            id="not buy"
        ),
        pytest.param(
            100,
            110,
            "Buy more cryptocurrency",
            id="the percentage is increasing"
        ),
        pytest.param(
            100,
            80,
            "Sell all your cryptocurrency",
            id="the percentage is decrease"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="not sell"
        ),
    ]
)
def test_cryptocurrency(
        mocked_rate_prediction: mock,
        current_rate: int,
        prediction_rate: int,
        result: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    res = cryptocurrency_action(current_rate)
    mocked_rate_prediction.assert_called_once_with(current_rate)
    assert res == result
