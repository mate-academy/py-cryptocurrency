import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, expected",
    [
        pytest.param(
            10.0 , 10.6, "Buy more cryptocurrency",
            id="Above top edge"
        ),
        pytest.param(
            10.0, 10.5, "Do nothing",
            id="On the top edge"
        ),
        pytest.param(
            10.0, 10.4, "Do nothing",
            id="Under top edge"
        ),
        pytest.param(
            10.0, 9.6, "Do nothing",
            id="Above bottom edge"
        ),
        pytest.param(
            10.0, 9.5, "Do nothing",
            id="On the bottom edge"
        ),
        pytest.param(
            10.0, 9.4, "Sell all your cryptocurrency",
            id="Under bottom edge"
        ),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: float,
        current_rate: float,
        prediction: float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected
