from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,mock_prediction,expected_result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: mock.MagicMock,
    current_rate: int,
    mock_prediction: int,
    expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = mock_prediction

    assert cryptocurrency_action(current_rate) == expected_result
