import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        pytest.param(1, 1.25, "Buy more cryptocurrency"),
        pytest.param(1, 1.05, "Do nothing"),
        pytest.param(1, 0.95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_rate(
        mock_function: mock,
        current_rate: int | float,
        prediction_rate: int | float,
        result: str
) -> None:
    mock_function.return_value = prediction_rate
    assert result == cryptocurrency_action(current_rate)
