import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expect_action",
    [
        pytest.param(100, 110, "Buy more cryptocurrency"),
        pytest.param(100, 90, "Sell all your cryptocurrency"),
        pytest.param(100, 100, "Do nothing"),
        pytest.param(100, 105, "Do nothing"),
        pytest.param(100, 95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expect_action: str
) -> None:

    mock_get_exchange_rate_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)

    assert result == expect_action
