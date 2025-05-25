import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected",
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (104, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_variants(
    mock_prediction: MagicMock,
    prediction: float,
    expected: str
) -> None:
    mock_prediction.return_value = prediction
    result = cryptocurrency_action(100)
    assert result == expected
