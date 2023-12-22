from unittest.mock import patch, Mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected_result",
    [
        pytest.param(
            1.0,
            "Do nothing",
            id="Do nothing when prediction equal 1"
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="Do nothing when prediction equal 0.95"
        ),
        pytest.param(
            1.05,
            "Do nothing",
            id="Do nothing when prediction equal 1.05"
        ),
        pytest.param(
            1.06,
            "Buy more cryptocurrency",
            id="Buy more cryptocurrency case"
        ),
        pytest.param(
            0.94,
            "Sell all your cryptocurrency",
            id="Sell all your cryptocurrency case"
        )
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: Mock,
    prediction: float,
    expected_result: str,
    current_rate: float = 1.0
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
