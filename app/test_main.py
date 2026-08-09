import pytest
from unittest import mock
from app.main import cryptocurrency_action


test_data = [
    (100, 105.1, "Buy more cryptocurrency"),
    (100, 105.0, "Do nothing"),
    (100, 120, "Buy more cryptocurrency"),
    (100, 94.9, "Sell all your cryptocurrency"),
    (100, 95.0, "Do nothing"),
    (100, 80, "Sell all your cryptocurrency"),
    (100, 100, "Do nothing"),
]


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    test_data
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: mock.MagicMock,
    current_rate: float,
    prediction_rate: float,
    expected: str
) -> None:

    mock_prediction.return_value = prediction_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected
