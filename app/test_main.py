import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate_prediction, expected_res",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        exchange_rate_prediction: int | float,
        expected_res: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=exchange_rate_prediction) as mocked_func:
        result = cryptocurrency_action(current_rate)
        mocked_func.assert_called_once_with(current_rate)
        assert result == expected_res
