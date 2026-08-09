import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "prediction, current_rate, expected_result",
    [
        (1.06, 1.0, "Buy more cryptocurrency"),
        (0.94, 1.0, "Sell all your cryptocurrency"),
        (1.05, 1.0, "Do nothing"),
        (0.95, 1.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_exchange_rate: mock,
                               prediction: int,
                               current_rate: int,
                               expected_result: str) -> None:
    mock_exchange_rate.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
