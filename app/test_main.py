import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "value, result",
    [(1.06, "Buy more cryptocurrency"),
     (1.05, "Do nothing"),
     (1.04, "Do nothing"),
     (0.96, "Do nothing"),
     (0.95, "Do nothing"),
     (0.94, "Sell all your cryptocurrency")
     ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock,
        value: float,
        result: str
) -> None:
    current_rate = 46.05
    mock_get_exchange_rate_prediction.return_value = value * current_rate
    assert cryptocurrency_action(current_rate) == result
