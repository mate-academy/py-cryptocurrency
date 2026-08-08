from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize("prediction_rate, current_rate, expected", [
    (18, 20, "Sell all your cryptocurrency"),
    (22, 20, "Buy more cryptocurrency"),
    (21, 20, "Do nothing"),
    (21, 21, "Do nothing"),
    (19, 20, "Do nothing")
]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_for_cryptocurrency_actions(mock_get_exchange_rate: mock.MagicMock,
                                    prediction_rate: float,
                                    current_rate: float,
                                    expected: str) -> None:
    mock_get_exchange_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
