import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mocked_value, expected_result",
    [
        (110, "Buy more cryptocurrency"),
        (80, "Sell all your cryptocurrency"),
        (99, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing")
    ]
)
def test_cryptocurrency_action(mocked_value: int,
                               expected_result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = mocked_value
        result = cryptocurrency_action(100)
        assert result == expected_result
