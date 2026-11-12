from unittest.mock import patch


import pytest


from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        pytest.param(
            100, 106, "Buy more cryptocurrency",
            id="Above +5%"
        ),
        pytest.param(
            100, 105, "Do nothing",
            id="Exactly +5%"
        ),
        pytest.param(
            100, 100, "Do nothing",
            id="No change"
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="Exactly -5%"
        ),
        pytest.param(
            100, 94, "Sell all your cryptocurrency",
            id="below -5%"
        ),
    ],
)
def test_cryptocurrency_action(
        mock_prediction: object,
        current_rate: float | int,
        predicted_rate: float | int,
        expected: str,
) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
