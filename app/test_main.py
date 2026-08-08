import pytest

from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,mocked_exchange_rate,expected",
    [
        pytest.param(
            2,
            2,
            "Do nothing",
            id="should return 'Do nothing' if P.E. rate is 0%",
        ),
        pytest.param(
            2,
            2.1,
            "Do nothing",
            id="should return 'Do nothing' if P.E. rate is 5% higher"
        ),
        pytest.param(
            2,
            1.9,
            "Do nothing",
            id="should return 'Do nothing' if P.E. rate is 5% lower"
        ),
        pytest.param(
            2,
            2.12,
            "Buy more cryptocurrency",
            id="should return 'Buy more...' if P.E. rate is >5% higher"
        ),
        pytest.param(
            2,
            1.88,
            "Sell all your cryptocurrency",
            id="should return 'Sell all your...' if P.E. rate is >5% lower"
        ),
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        mocked_exchange_rate: float,
        expected: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=mocked_exchange_rate
    ):
        assert cryptocurrency_action(current_rate) == expected
