import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_answer",
    [
        pytest.param(100, 200, "Buy more cryptocurrency", id=""),
        pytest.param(100, 50, "Sell all your cryptocurrency", id=""),
        pytest.param(100, 105, "Do nothing", id=""),
        pytest.param(100, 95, "Do nothing", id="")
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected_answer: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate

    assert cryptocurrency_action(current_rate) == expected_answer
