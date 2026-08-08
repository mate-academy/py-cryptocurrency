from app.main import cryptocurrency_action
import pytest
from unittest.mock import patch, MagicMock


@pytest.mark.parametrize(
    "prediction, current, expected_text",
    [
        (110, 110, "Do nothing"),
        (120, 110, "Buy more cryptocurrency"),
        (100.0, 110, "Sell all your cryptocurrency"),
        (150.0, 110, "Buy more cryptocurrency"),
        (100.0, 100.0, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (100, 104.9, "Do nothing"),
        (105.01, 100, "Buy more cryptocurrency"),
        (94.99, 100, "Sell all your cryptocurrency")
    ],
    ids=[
        "110/110 Do nothing",
        "120/110 Buy more cryptocurrency",
        "100.0/110 Sell all your cryptocurrency",
        "150.0/110 Buy more cryptocurrency",
        "100.0/100.0 Do nothing",
        "105/100 Do nothing",
        "95/100 Do nothing",
        "100/104.9 Do nothing",
        "105.01/100 Buy more cryptocurrency",
        "94.99/100 Sell all your cryptocurrency",
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_pred: MagicMock,
        prediction: int | float,
        current: int | float,
        expected_text: str
) -> None:
    mock_exchange_pred.return_value = prediction

    result = cryptocurrency_action(current)

    assert result == expected_text
