import pytest
from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, mock_return_value, expected",
    [
        pytest.param(
            2, 2.1, "Do nothing"
        ),
        pytest.param(
            2, 1.9, "Do nothing"
        ),
        pytest.param(
            2, 3., "Buy more cryptocurrency"
        ),
        pytest.param(
            2, 1., "Sell all your cryptocurrency"
        )
    ]
)
def test_cryptocurrency_call_rate_prediction(mocked_exchange_rate: MagicMock,
                                             current_rate: (int | float),
                                             mock_return_value: float,
                                             expected: str) -> None:
    mocked_rate = mocked_exchange_rate
    mocked_rate.return_value = mock_return_value
    assert cryptocurrency_action(current_rate) == expected, expected
    mocked_rate.assert_called_once_with(current_rate)
