import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (106, 100, "Buy more cryptocurrency"),
        (105.1, 100, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
        (100, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94.9, 100, "Sell all your cryptocurrency"),
        (93, 100, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: mock.MagicMock,
    prediction_rate: float,
    current_rate: float,
    expected_result: str,
) -> None:
    mock_prediction.return_value = prediction_rate
    result = main.cryptocurrency_action(current_rate)
    assert result == expected_result
