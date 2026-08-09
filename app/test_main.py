import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_rate", [
    (100, 100, "Do nothing"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 106, "Buy more cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_correct_prediction(mock_get_exchange_rate_prediction: mock.MagicMock,
                            current_rate: int,
                            predicted_rate: int,
                            expected_rate: str) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_rate
