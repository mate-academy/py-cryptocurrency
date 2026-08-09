import pytest
from unittest.mock import patch
from app import main


@pytest.mark.parametrize(
    "prediction,current,expected",
    [
        (105.1, 100, "Buy more cryptocurrency"),
        (105.0, 100, "Do nothing"),
        (100.0, 100, "Do nothing"),
        (95.0, 100, "Do nothing"),
        (94.9, 100, "Sell all your cryptocurrency"),
    ])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_logic(mock_prediction: float,
                                     prediction: float,
                                     current: float,
                                     expected: float) -> None:
    mock_prediction.return_value = prediction
    assert main.cryptocurrency_action(current) == expected
