from unittest import mock
from typing import Generator

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate_prediction() -> Generator[mock.MagicMock, None, None]:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_rate_prediction):
        yield mock_rate_prediction


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(1, 1.06, "Buy more cryptocurrency",
                     id="prediction_rate / current_rate > 1.05"),
        pytest.param(1, 0.94, "Sell all your cryptocurrency",
                     id="prediction_rate / current_rate < 0.95"),
        pytest.param(1, 1.02, "Do nothing",
                     id="0.95 < prediction_rate / current_rate < 1.05"),
        pytest.param(1, 1.05, "Do nothing",
                     id="prediction_rate / current_rate == 1.05"),
        pytest.param(1, 0.95, "Do nothing",
                     id="prediction_rate / current_rate == 0.95")
    ]
)
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock.MagicMock,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
