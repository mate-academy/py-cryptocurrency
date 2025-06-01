import pytest
from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate,expected",
    [
        pytest.param(
            105,
            "Do nothing",
            id="Should return 'Do nothing'"
        ),
        pytest.param(
            95,
            "Do nothing",
            id="Should return 'Do nothing'"
        ),
        pytest.param(
            106,
            "Buy more cryptocurrency",
            id="Should return 'Buy more cryptocurrency'"
        ),
        pytest.param(
            94,
            "Sell all your cryptocurrency",
            id="Should return 'Sell all your cryptocurrency'"
        ),
        pytest.param(
            100,
            "Do nothing",
            id="Should return 'Do nothing'"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_exchange_rate: mock.MagicMock,
    exchange_rate: Union[int, float],
    expected: str
) -> None:
    mocked_exchange_rate.return_value = exchange_rate
    assert cryptocurrency_action(100) == expected

    mocked_exchange_rate.assert_called_once()
