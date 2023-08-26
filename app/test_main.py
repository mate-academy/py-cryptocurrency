import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("prediction_rate", "current_rate", "expected_output"),
    [(110, 100, "Buy more cryptocurrency"),
     (120, 50, "Buy more cryptocurrency"),
     (90, 100, "Sell all your cryptocurrency"),
     (95, 105, "Sell all your cryptocurrency"),
     (95, 100, "Do nothing"),
     (105, 100, "Do nothing"),
     (99, 100, "Do nothing"),
     ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_prediction: mock.Mock,
                               prediction_rate: float,
                               current_rate: float,
                               expected_output: str) -> None:
    mock_get_exchange_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_output
