import pytest

from app.main import cryptocurrency_action
from unittest import mock
from typing import Union


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_prediction:
        yield mock_prediction


@pytest.mark.parametrize(
    "current_rate,return_value,expected_result",
    [
        pytest.param(1, 1.06, "Buy more cryptocurrency",
                     id="should return 'buy...' when value == 1.06"),
        pytest.param(1, 0.94, "Sell all your cryptocurrency",
                     id="should return 'sell...' when value == 0.94"),
        pytest.param(1, 1.01, "Do nothing",
                     id="should return 'Do nothing...' "
                        "when value in the specified range"),
        pytest.param(1, 0.95, "Do nothing",
                     id="should return 'Do nothing...' with value == 0.95"),
        pytest.param(1, 1.05, "Do nothing",
                     id="should return 'Do nothing...' with value == 1.05"),
    ]
)
def test_cryptocurrency_actions(current_rate: Union[int, float],
                                return_value: Union[int, float],
                                expected_result: str,
                                mocked_get_exchange_rate_prediction:
                                [int, float]) -> None:
    mocked_get_exchange_rate_prediction.return_value = return_value
    assert cryptocurrency_action(current_rate) == expected_result
