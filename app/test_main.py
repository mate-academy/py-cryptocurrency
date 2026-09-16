from unittest.mock import MagicMock, patch

import pytest

from app import main


@pytest.mark.parametrize(
    "prediction_rate, expected_result",
    [
        (106, "Buy more cryptocurrency"),
        (105.01, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94.99, "Sell all your cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
    ],
    ids=[
        "prediction_more_than_5_percent_higher",
        "prediction_just_above_buy_boundary",
        "prediction_exactly_on_buy_boundary_is_do_nothing",
        "prediction_equal_to_current_rate",
        "prediction_exactly_on_sell_boundary_is_do_nothing",
        "prediction_just_below_sell_boundary",
        "prediction_more_than_5_percent_lower",
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    prediction_rate: float,
    expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate

    result = main.cryptocurrency_action(100)

    assert result == expected_result
